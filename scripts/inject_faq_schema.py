#!/usr/bin/env python3
"""Inject translated FAQPage schema into the existing DE/ES plant pages.

The EN plant pages already carry a four-question FAQPage (light, toxicity,
difficulty, watering). This adds the same four questions, translated, to the
DE and ES pages by editing the built HTML in place -- the generators are NOT
re-run, so every other improvement on those pages is left untouched.

The question wording and phrase tables live in generate_german.py /
generate_spanish.py, and are imported here rather than duplicated, so the
injected markup and a future regeneration stay in agreement.

Safe to run repeatedly: an existing FAQPage block is replaced, not appended.
"""

import importlib.util
import json
import os
import re
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLANTS_FILE = os.path.join(BASE_DIR, "data/plants.json")

LANGS = {
    "de": {
        "pages": os.path.join(BASE_DIR, "de/plants"),
        "generator": os.path.join(BASE_DIR, "generate_german.py"),
        "translations": os.path.join(BASE_DIR, "data/plants_de.json"),
    },
    "es": {
        "pages": os.path.join(BASE_DIR, "es/plants"),
        "generator": os.path.join(BASE_DIR, "generate_spanish.py"),
        "translations": os.path.join(BASE_DIR, "data/plants_es.json"),
    },
}

# The FAQ block sits after the breadcrumb schema and before the analytics tag,
# matching where it sits on the EN pages.
ANCHOR = '<script src="https://analytics.ahrefs.com/analytics.js"'

H1_RE = re.compile(
    r'<h1 class="text-3xl md:text-4xl font-bold text-slate-900 mb-2">([^<]*)</h1>'
)
CANONICAL_RE = re.compile(r'<link rel="canonical" href="[^"]*/plants/([^/"]+)/"')
ARTICLE_RE = re.compile(
    r'<script type="application/ld\+json">\s*(\{.*?"@type":\s*"Article".*?\})\s*</script>',
    re.S,
)
FAQ_BLOCK_RE = re.compile(
    r'\n?[ \t]*<!-- FAQ Schema -->\s*'
    r'<script type="application/ld\+json">\s*\{.*?"@type":\s*"FAQPage".*?\}\s*</script>',
    re.S,
)


def load_generator(path):
    """Load a generator module without running its main()."""
    name = os.path.splitext(os.path.basename(path))[0]
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def page_plant_data(html, plants_by_id, translations):
    """Recover the data the FAQ needs from an existing page.

    The Article schema identifies the plant and carries its display name, but
    not the numeric care ratings the questions are built from, so those are
    read from data/plants.json keyed on the slug in the canonical URL.
    """
    slug_match = CANONICAL_RE.search(html)
    if not slug_match:
        return None, None, "no canonical URL"
    slug = slug_match.group(1)

    plant = plants_by_id.get(slug)
    if plant is None:
        return None, None, f"no plant data for {slug!r}"

    article_match = ARTICLE_RE.search(html)
    if not article_match:
        return None, None, "no Article schema"
    try:
        article = json.loads(article_match.group(1))
    except ValueError as exc:
        return None, None, f"unparseable Article schema: {exc}"

    # Prefer the page's own <h1>; fall back to the Article schema's subject.
    h1_match = H1_RE.search(html)
    name = h1_match.group(1).strip() if h1_match else None
    if not name:
        name = article.get("about", {}).get("name")
    if not name:
        return None, None, "no display name"

    # Care tips are the translated sentence the light/watering answers quote.
    plant = dict(plant)
    translated = translations.get(slug, {})
    if "care_tips" in translated:
        plant["care_tips"] = translated["care_tips"]

    return plant, name, None


def inject(html, faq_block):
    """Replace an existing FAQ block, or insert one before the analytics tag."""
    if FAQ_BLOCK_RE.search(html):
        return FAQ_BLOCK_RE.sub("\n" + faq_block, html, count=1), "replaced"
    if ANCHOR not in html:
        return html, None
    return html.replace(ANCHOR, faq_block + "\n" + ANCHOR, 1), "inserted"


def main():
    with open(PLANTS_FILE, encoding="utf-8") as f:
        plants_by_id = {p["id"]: p for p in json.load(f)}

    total_changed = 0
    problems = []

    for lang, cfg in LANGS.items():
        generator = load_generator(cfg["generator"])
        with open(cfg["translations"], encoding="utf-8") as f:
            translations = json.load(f)

        changed = inserted = replaced = 0
        for slug in sorted(os.listdir(cfg["pages"])):
            path = os.path.join(cfg["pages"], slug, "index.html")
            if not os.path.isfile(path):
                continue

            with open(path, encoding="utf-8") as f:
                html = f.read()

            plant, name, error = page_plant_data(html, plants_by_id, translations)
            if error:
                problems.append(f"{lang}/{slug}: {error}")
                continue

            qa = generator.build_faq_schema(plant, name)
            faq_block = generator.render_faq_schema(qa)

            # Fail loudly rather than writing malformed JSON-LD into a page.
            json.loads(re.search(r"(\{.*\})", faq_block, re.S).group(1))

            new_html, how = inject(html, faq_block)
            if how is None:
                problems.append(f"{lang}/{slug}: no injection point")
                continue
            if new_html != html:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(new_html)
                changed += 1
                if how == "inserted":
                    inserted += 1
                else:
                    replaced += 1

        total_changed += changed
        print(f"{lang}: {changed} pages updated ({inserted} inserted, {replaced} replaced)")

    for problem in problems:
        print(f"  ! {problem}", file=sys.stderr)
    print(f"\nTotal pages updated: {total_changed}")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
