#!/usr/bin/env python3
"""Render the per-plant long-form care content into the built EN plant pages.

Content lives in data/plant_content.json, one entry per plant id, written by
hand rather than derived from the care ratings -- the whole point is that the
propagation method, the failure modes and the repotting advice differ by
species. Plants with no entry are skipped, so this can be run while the
content is still being filled in.

The generators are NOT used; this edits the built HTML directly.
Safe to re-run: everything between the markers is replaced.
"""

import html as html_mod
import json
import os
import re
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT_FILE = os.path.join(BASE_DIR, "data/plant_content.json")
PLANTS_DIR = os.path.join(BASE_DIR, "plants")

START = "        <!-- DEEPCARE:START (scripts/inject_plant_content.py) -->"
END = "        <!-- DEEPCARE:END -->"
BLOCK_RE = re.compile(re.escape(START) + r".*?" + re.escape(END) + r"\n?", re.S)

# Inserted before the "Is This Plant Right for You?" section.
ANCHOR = '        <!-- Is This Plant Right for You? -->'

CARD = ('<section class="bg-white rounded-2xl shadow-sm border border-slate-200 '
        'p-6 md:p-8 mb-8">')


def e(text):
    return html_mod.escape(text, quote=False)


def paragraphs(items):
    return "\n".join(
        f'            <p class="text-slate-600 leading-relaxed mb-4">{e(p)}</p>'
        for p in items)


def render(name, c):
    out = [START]

    # --- Care in depth: light / water / soil ---
    care = c.get("care", {})
    if care:
        out.append(CARD)
        out.append(f'            <h2 class="text-xl font-bold text-slate-900 mb-4">'
                   f'{e(name)} Care in Depth</h2>')
        for key, heading, icon in (("light", "Light", "sun"),
                                   ("water", "Watering through the year", "droplets"),
                                   ("soil", "Soil and potting mix", "layers")):
            if care.get(key):
                out.append('            <h3 class="font-bold text-slate-800 mt-6 mb-2 '
                           'flex items-center gap-2">'
                           f'<i data-lucide="{icon}" class="w-5 h-5 text-emerald-600"></i>'
                           f'{e(heading)}</h3>')
                out.append(paragraphs(care[key] if isinstance(care[key], list) else [care[key]]))
        out.append('        </section>')

    # --- Propagation ---
    if c.get("propagation"):
        out.append(CARD)
        out.append(f'            <h2 class="text-xl font-bold text-slate-900 mb-4">'
                   f'How to Propagate {e(name)}</h2>')
        out.append(paragraphs(c["propagation"]))
        out.append('        </section>')

    # --- Common problems ---
    if c.get("problems"):
        out.append(CARD)
        out.append('            <h2 class="text-xl font-bold text-slate-900 mb-6">'
                   f'Common {e(name)} Problems &amp; Fixes</h2>')
        out.append('            <div class="space-y-4">')
        for p in c["problems"]:
            out.append(
                '                <div class="border border-slate-200 rounded-xl p-5">\n'
                f'                    <h3 class="font-bold text-slate-900 mb-1">{e(p["symptom"])}</h3>\n'
                f'                    <p class="text-slate-600 mb-2"><strong class="text-slate-700">Usually means:</strong> {e(p["cause"])}</p>\n'
                f'                    <p class="text-slate-600"><strong class="text-slate-700">What to do:</strong> {e(p["fix"])}</p>\n'
                '                </div>')
        out.append('            </div>')
        out.append('        </section>')

    # --- Repotting ---
    if c.get("repotting"):
        out.append(CARD)
        out.append(f'            <h2 class="text-xl font-bold text-slate-900 mb-4">'
                   f'Repotting {e(name)}</h2>')
        out.append(paragraphs(c["repotting"]))
        out.append('        </section>')

    # --- Varieties ---
    if c.get("varieties"):
        out.append(CARD)
        out.append('            <h2 class="text-xl font-bold text-slate-900 mb-4">'
                   f'{e(name)} Varieties to Look For</h2>')
        out.append(paragraphs(c["varieties"]))
        out.append('        </section>')

    out.append(END)
    return "\n".join(out) + "\n"


def main():
    with open(CONTENT_FILE, encoding="utf-8") as f:
        content = json.load(f)
    with open(os.path.join(BASE_DIR, "data/plants.json"), encoding="utf-8") as f:
        names = {p["id"]: p["name"] for p in json.load(f)}

    written = skipped = 0
    problems = []
    for slug, c in content.items():
        path = os.path.join(PLANTS_DIR, slug, "index.html")
        if not os.path.isfile(path):
            problems.append(f"{slug}: no page"); continue
        s = open(path, encoding="utf-8").read()
        block = render(names.get(slug, slug), c)

        if BLOCK_RE.search(s):
            s = BLOCK_RE.sub(block, s, count=1)
        elif ANCHOR in s:
            s = s.replace(ANCHOR, block + ANCHOR, 1)
        else:
            problems.append(f"{slug}: no insertion point"); continue

        open(path, "w", encoding="utf-8").write(s)
        written += 1

    skipped = len(names) - written
    print(f"content injected into {written} plant pages ({skipped} still without content)")
    for p in problems:
        print("  !", p, file=sys.stderr)
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
