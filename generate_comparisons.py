#!/usr/bin/env python3
"""Generate static head-to-head comparison pages under /compare/<a>-vs-<b>/.

Each page answers one comparison query ("pothos vs philodendron") with a real,
data-backed answer in the title, the meta description and the first paragraph,
instead of pointing at the generic compare tool.

Run from the repo root:  python3 generate_comparisons.py
"""
import html
import json
import os
import re
from datetime import date

from comparison_pairs import DESCRIPTIONS, PAIRS, SLUG_OVERRIDES

BASE = "https://plantfinder.org"
TODAY = date.today().isoformat()
OUT_ROOT = "compare"

# ---------------------------------------------------------------- data ------

with open("data/plants.json") as f:
    PLANTS = {p["id"]: p for p in json.load(f)}


def norm_difficulty(p):
    d = (p.get("difficulty") or "").lower()
    return "medium" if d == "moderate" else d


DIFF_RANK = {"easy": 0, "medium": 1, "hard": 2}
SIZE_RANK = {"small": 0, "medium": 1, "large": 2}
GROWTH_RANK = {"slow": 0, "moderate": 1, "fast": 2}

LIGHT = {
    1: ("Low light", "survives in a dim corner away from any window"),
    2: ("Low to medium light", "fine a few metres back from a window"),
    3: ("Medium indirect light", "near a bright window, out of direct sun"),
    4: ("Bright indirect light", "beside a bright window, no midday sun on the leaves"),
    5: ("Very bright light", "a south or west window with some direct sun"),
}
WATER = {
    1: ("Very low", "water every 2-3 weeks, once the pot is bone dry"),
    2: ("Low", "water when the top 3-5 cm of soil has dried out"),
    3: ("Moderate", "water when the top 2-3 cm is dry, roughly weekly"),
    4: ("High", "keep the soil evenly moist, never fully dry"),
    5: ("Very high", "never let the soil dry out, even briefly"),
}
HUMIDITY = {
    1: ("Low", "ordinary dry room air is fine"),
    2: ("Low", "ordinary room air is fine"),
    3: ("Average", "normal household humidity works"),
    4: ("Above average", "group plants or run a humidifier in winter"),
    5: ("High", "needs a humidifier, a terrarium or a steamy bathroom"),
}
SIZE = {
    "small": ("Small", "15-30 cm (6-12 in)", "a shelf or desk"),
    "medium": ("Medium", "30-90 cm (1-3 ft)", "a side table or plant stand"),
    "large": ("Large", "90-180+ cm (3-6+ ft)", "the floor"),
}
GROWTH = {"slow": "Slow", "moderate": "Moderate", "fast": "Fast"}


def slug_of(pid):
    if pid in SLUG_OVERRIDES:
        return SLUG_OVERRIDES[pid]
    name = PLANTS[pid]["name"].lower().replace("'", "").replace("\u2019", "")
    return re.sub(r"[^a-z0-9]+", "-", name).strip("-")


def pair_slug(a, b):
    return f"{slug_of(a)}-vs-{slug_of(b)}"


def toxic_phrase(p):
    t = p.get("toxic_to") or []
    if not t:
        return "cats and dogs"
    if len(t) == 1:
        return t[0]
    return " and ".join([", ".join(t[:-1]), t[-1]])


def e(s):
    return html.escape(str(s), quote=True)


# ------------------------------------------------------- difference model ---

def differences(a, b):
    """Ranked, human-readable differences between two plants.

    Each entry: (axis, headline, detail, winner_id_or_None).
    Ordered by how much a searcher comparing the two actually cares.
    """
    out = []
    na, nb = a["name"], b["name"]

    # Pet safety is the single most decisive attribute when it differs.
    if a["pet_safe"] != b["pet_safe"]:
        safe, tox = (a, b) if a["pet_safe"] else (b, a)
        out.append((
            "pets",
            f"{safe['name']} is pet-safe, {tox['name']} is not",
            f"{safe['name']} is non-toxic to cats and dogs. {tox['name']} is toxic to "
            f"{toxic_phrase(tox)} if chewed, so it needs a shelf pets cannot reach.",
            safe["id"],
        ))

    da, db = norm_difficulty(a), norm_difficulty(b)
    if da != db:
        easier, harder = (a, b) if DIFF_RANK[da] < DIFF_RANK[db] else (b, a)
        eh = norm_difficulty(harder)
        out.append((
            "difficulty",
            f"{easier['name']} is the easier plant",
            f"{easier['name']} is rated {norm_difficulty(easier)} to care for, "
            f"{harder['name']} {eh}. If this is an early houseplant or the spot is "
            f"hard to get right, start with the {easier['name']}.",
            easier["id"],
        ))

    gap = abs(a["light"] - b["light"])
    if gap:
        lower, higher = (a, b) if a["light"] < b["light"] else (b, a)
        out.append((
            "light",
            f"{lower['name']} copes with {'much ' if gap >= 2 else ''}less light",
            f"{lower['name']} needs {LIGHT[lower['light']][0].lower()} ({lower['light']}/5) - "
            f"{LIGHT[lower['light']][1]}. {higher['name']} wants "
            f"{LIGHT[higher['light']][0].lower()} ({higher['light']}/5), "
            f"{LIGHT[higher['light']][1]}.",
            lower["id"],
        ))

    gap = abs(a["water"] - b["water"])
    if gap:
        lower, higher = (a, b) if a["water"] < b["water"] else (b, a)
        out.append((
            "water",
            f"{higher['name']} drinks {'far ' if gap >= 2 else ''}more",
            f"{lower['name']} wants {WATER[lower['water']][0].lower()} watering "
            f"({lower['water']}/5) - {WATER[lower['water']][1]}. {higher['name']} needs "
            f"{WATER[higher['water']][0].lower()} watering ({higher['water']}/5): "
            f"{WATER[higher['water']][1]}.",
            lower["id"],
        ))

    gap = abs(a["humidity"] - b["humidity"])
    if gap:
        lower, higher = (a, b) if a["humidity"] < b["humidity"] else (b, a)
        out.append((
            "humidity",
            f"{higher['name']} needs damper air",
            f"{higher['name']} rates {higher['humidity']}/5 for humidity - "
            f"{HUMIDITY[higher['humidity']][1]}. {lower['name']} rates "
            f"{lower['humidity']}/5, so {HUMIDITY[lower['humidity']][1]}.",
            lower["id"] if gap >= 2 else None,
        ))

    if a["size"] != b["size"]:
        small, big = ((a, b) if SIZE_RANK[a["size"]] < SIZE_RANK[b["size"]] else (b, a))
        out.append((
            "size",
            f"{big['name']} is the bigger plant",
            f"{big['name']} reaches {SIZE[big['size']][1]} and belongs on "
            f"{SIZE[big['size']][2]}. {small['name']} tops out around "
            f"{SIZE[small['size']][1]}, so it suits {SIZE[small['size']][2]}.",
            None,
        ))

    ga, gb = a.get("growth_rate"), b.get("growth_rate")
    if ga and gb and ga != gb:
        fast, slow = ((a, b) if GROWTH_RANK[ga] > GROWTH_RANK[gb] else (b, a))
        out.append((
            "growth",
            f"{fast['name']} fills out faster",
            f"{fast['name']} is a {fast['growth_rate']} grower and gives you cuttings "
            f"or a full pot sooner. {slow['name']} is {slow['growth_rate']}, which means "
            f"less pruning and repotting but a longer wait.",
            None,
        ))

    if a.get("air_purifying") != b.get("air_purifying"):
        yes = a if a.get("air_purifying") else b
        no = b if a.get("air_purifying") else a
        out.append((
            "air",
            f"{yes['name']} is the air-purifying one",
            f"{yes['name']} appears on the common indoor air-purifying lists; "
            f"{no['name']} does not. In a normal room the effect of either is modest, "
            f"so treat it as a tiebreaker rather than a reason to buy.",
            None,
        ))

    if a["category"] != b["category"]:
        out.append((
            "type",
            f"Different plant types: {a['category']} vs {b['category']}",
            f"{na} is a {a['category']} plant and {nb} is a {b['category']} plant, so "
            f"they fill different jobs in a room even when their care overlaps.",
            None,
        ))

    if (a.get("origin") and b.get("origin") and a["origin"] != b["origin"]):
        out.append((
            "origin",
            "They come from different habitats",
            f"{na} originates in {a['origin']}; {nb} in {b['origin']}. Matching the "
            f"original habitat is the quickest way to guess what each one wants indoors.",
            None,
        ))

    if not out:
        # Genuinely interchangeable on care -- say so rather than inventing a gap.
        out.append((
            "same",
            "Care is identical - the difference is how they look",
            f"On every axis we track - light, water, humidity, difficulty, mature size "
            f"and growth speed - {na} and {nb} are the same plant to live with, so "
            f"neither is the safer bet. {na}: {a['description']} {nb}: {b['description']}",
            None,
        ))

    return out


def same_notes(a, b):
    """What the two plants agree on -- used to keep the copy honest."""
    same = []
    if a["pet_safe"] == b["pet_safe"]:
        same.append("both are pet-safe" if a["pet_safe"]
                    else "both are toxic to cats and dogs")
    if norm_difficulty(a) == norm_difficulty(b):
        same.append(f"both are rated {norm_difficulty(a)}")
    if a["light"] == b["light"]:
        same.append(f"both want {LIGHT[a['light']][0].lower()}")
    if a["water"] == b["water"]:
        same.append(f"both take {WATER[a['water']][0].lower()} watering")
    if a["humidity"] == b["humidity"]:
        same.append("both are happy in the same humidity")
    if a["size"] == b["size"]:
        same.append(f"both stay {SIZE[a['size']][0].lower()}")
    return same


# ----------------------------------------------------------- copywriting ----

def meta_description(a, b, diffs):
    """The hand-written, answer-first description for this pair."""
    return DESCRIPTIONS[(a["id"], b["id"])]


def title_of(a, b, diffs):
    """Front-load the query, then the angle that actually separates the two."""
    top = diffs[0][0] if diffs else "same"
    angles = {
        "pets": "Care, Pet Safety & Light Compared",
        "difficulty": "Which Is Easier to Grow?",
        "light": "Light, Water & Care Compared",
        "water": "Water, Light & Care Compared",
        "humidity": "Humidity, Light & Care Compared",
        "size": "Size, Care & Light Compared",
        "growth": "Care, Growth & Light Compared",
    }
    query = f"{a['name']} vs {b['name']}"
    for angle in (angles.get(top, "Care, Light & Water Compared"), "Care Compared"):
        title = f"{query} \u2014 {angle} | PlantFinder"
        if len(title) <= 70:
            return title
    return f"{query} \u2014 Care Compared | PlantFinder"


def lede(a, b, diffs, same):
    """(answer, evidence) -- the search snippet's answer, then what backs it up."""
    answer = DESCRIPTIONS[(a["id"], b["id"])]
    evidence = " ".join(detail for _axis, _head, detail, _w in diffs[:2])
    return answer, evidence


def pick_reasons(p, other):
    """Concrete 'choose this one if' bullets, all traceable to the data."""
    r = []
    if p["light"] < other["light"]:
        r.append(f"your spot is the dimmer of the two - it manages on {LIGHT[p['light']][0].lower()}")
    elif p["light"] > other["light"]:
        r.append(f"you have a bright window to give it ({LIGHT[p['light']][0].lower()})")
    if p["water"] < other["water"]:
        r.append("you forget to water - it prefers to dry out between drinks")
    elif p["water"] > other["water"]:
        r.append("you like a plant that asks for attention on a schedule")
    if p["humidity"] < other["humidity"]:
        r.append("your home runs dry in winter and you will not add a humidifier")
    elif p["humidity"] > other["humidity"]:
        r.append("it will live in a bathroom, kitchen or a humidified room")
    if DIFF_RANK[norm_difficulty(p)] < DIFF_RANK[norm_difficulty(other)]:
        r.append("you want the lower-risk plant of the two")
    elif DIFF_RANK[norm_difficulty(p)] > DIFF_RANK[norm_difficulty(other)]:
        r.append("you are happy to fuss a little for the better-looking leaves")
    if p["pet_safe"] and not other["pet_safe"]:
        r.append("cats or dogs chew your plants - this one is non-toxic")
    elif other["pet_safe"] and not p["pet_safe"]:
        r.append("it can go somewhere pets genuinely cannot reach")
    if SIZE_RANK[p["size"]] > SIZE_RANK[other["size"]]:
        r.append(f"you want a floor-filling plant ({SIZE[p['size']][1]})")
    elif SIZE_RANK[p["size"]] < SIZE_RANK[other["size"]]:
        r.append(f"shelf space is what you have ({SIZE[p['size']][1]})")
    if p.get("growth_rate") and other.get("growth_rate"):
        if GROWTH_RANK[p["growth_rate"]] > GROWTH_RANK[other["growth_rate"]]:
            r.append("you want visible growth and free cuttings quickly")
        elif GROWTH_RANK[p["growth_rate"]] < GROWTH_RANK[other["growth_rate"]]:
            r.append("you would rather not prune and repot often")
    if p.get("air_purifying") and not other.get("air_purifying"):
        r.append("air-purifying credentials are a tiebreaker for you")
    if len(r) < 3:
        r.append(f"the look is what you are after: {p['description']}")
    return r[:5]


def faqs(a, b, diffs, note, same):
    q = []
    top_detail = diffs[0][2] if diffs else ""
    q.append((
        f"What is the difference between {a['name']} and {b['name']}?",
        f"{note} On care, {top_detail[0].lower() + top_detail[1:]}",
    ))

    da, db = norm_difficulty(a), norm_difficulty(b)
    if da != db:
        easier = a if DIFF_RANK[da] < DIFF_RANK[db] else b
        harder = b if easier is a else a
        ans = (f"{easier['name']}. It is rated {norm_difficulty(easier)} while "
               f"{harder['name']} is {norm_difficulty(harder)}, and it is more "
               f"forgiving about light and watering mistakes.")
    else:
        ans = (f"Neither - both are rated {da}. The practical difference is "
               f"{diffs[0][1].lower() if diffs else 'mostly cosmetic'}.")
    q.append((f"Which is easier to care for, {a['name']} or {b['name']}?", ans))

    if a["pet_safe"] != b["pet_safe"]:
        safe = a if a["pet_safe"] else b
        tox = b if safe is a else a
        ans = (f"{safe['name']} is non-toxic to cats and dogs. {tox['name']} is toxic "
               f"to {toxic_phrase(tox)} if chewed, so keep it out of reach or choose "
               f"the {safe['name']}.")
    elif a["pet_safe"]:
        ans = (f"Both are safe. {a['name']} and {b['name']} are each non-toxic to cats "
               f"and dogs, so either works in a home with animals.")
    else:
        ans = (f"Neither. {a['name']} is toxic to {toxic_phrase(a)} and {b['name']} is "
               f"toxic to {toxic_phrase(b)}. Both need a spot pets cannot reach.")
    q.append((f"Is {a['name']} or {b['name']} safe for cats and dogs?", ans))

    if a["light"] != b["light"]:
        lower = a if a["light"] < b["light"] else b
        higher = b if lower is a else a
        ans = (f"{lower['name']}. It scores {lower['light']}/5 for light and "
               f"{LIGHT[lower['light']][1]}. {higher['name']} scores "
               f"{higher['light']}/5 and {LIGHT[higher['light']][1]}.")
    else:
        ans = (f"They are the same. Both score {a['light']}/5 for light, meaning "
               f"{LIGHT[a['light']][1]}.")
    q.append((f"Which needs less light, {a['name']} or {b['name']}?", ans))

    if a["water"] != b["water"]:
        higher = a if a["water"] > b["water"] else b
        lower = b if higher is a else a
        ans = (f"{higher['name']}, at {higher['water']}/5 - "
               f"{WATER[higher['water']][1]}. {lower['name']} scores "
               f"{lower['water']}/5: {WATER[lower['water']][1]}.")
    else:
        ans = (f"Neither - both score {a['water']}/5. For each one, "
               f"{WATER[a['water']][1]}.")
    q.append((f"Which needs more water, {a['name']} or {b['name']}?", ans))
    return q


# ------------------------------------------------------------- rendering ---

NAV = """    <nav class="bg-white/80 backdrop-blur-md border-b border-slate-200 sticky top-0 z-50">
        <div class="max-w-5xl mx-auto px-4 py-4">
            <div class="flex items-center justify-between">
                <a href="/" class="flex items-center gap-2">
                    <svg class="w-7 h-7 text-emerald-600" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M7 20h10"/>
                        <path d="M10 20c5.5-2.5.8-6.4 3-10"/>
                        <path d="M9.5 9.4c1.1.8 1.8 2.2 2.3 3.7-2 .4-3.5.4-4.8-.3-1.2-.6-2.3-1.9-3-4.2 2.8-.5 4.4 0 5.5.8z"/>
                        <path d="M14.1 6a7 7 0 0 0-1.1 4c1.9-.1 3.3-.6 4.3-1.4 1-1 1.6-2.3 1.7-4.6-2.7.1-4 1-4.9 2z"/>
                    </svg>
                    <span class="font-bold text-xl bg-gradient-to-r from-emerald-600 to-teal-600 bg-clip-text text-transparent">PlantFinder</span>
                </a>
                <div class="flex items-center gap-4 md:gap-6 text-sm">
                    <a href="/search/" class="text-slate-600 hover:text-slate-900 font-medium hidden sm:block">Browse</a>
                    <a href="/quiz/" class="text-slate-600 hover:text-slate-900 font-medium hidden sm:block">Quiz</a>
                    <a href="/compare/" class="text-emerald-700 font-semibold">Compare</a>
                </div>
            </div>
        </div>
    </nav>
"""

FOOTER = """    <footer class="bg-slate-900 text-slate-400 py-12 mt-16">
        <div class="max-w-5xl mx-auto px-4">
            <div class="flex flex-col md:flex-row justify-between items-center gap-4">
                <div class="flex items-center gap-2">
                    <svg class="w-6 h-6 text-emerald-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M7 20h10"/>
                        <path d="M10 20c5.5-2.5.8-6.4 3-10"/>
                        <path d="M9.5 9.4c1.1.8 1.8 2.2 2.3 3.7-2 .4-3.5.4-4.8-.3-1.2-.6-2.3-1.9-3-4.2 2.8-.5 4.4 0 5.5.8z"/>
                        <path d="M14.1 6a7 7 0 0 0-1.1 4c1.9-.1 3.3-.6 4.3-1.4 1-1 1.6-2.3 1.7-4.6-2.7.1-4 1-4.9 2z"/>
                    </svg>
                    <span class="font-bold text-white">PlantFinder</span>
                </div>
                <div class="flex gap-6 text-sm">
                    <a href="/search/" class="hover:text-white">Browse</a>
                    <a href="/quiz/" class="hover:text-white">Quiz</a>
                    <a href="/compare/" class="hover:text-white">Compare</a>
                    <a href="/faq/" class="hover:text-white">FAQ</a>
                    <a href="/privacy/" class="hover:text-white">Privacy</a>
                </div>
                <p class="text-sm">&copy; 2026 PlantFinder</p>
            </div>
        </div>
    </footer>
"""

GA = ('<script async src="https://www.googletagmanager.com/gtag/js?id=G-J2JW25BZPF"></script>'
      '<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}'
      'gtag("js",new Date());gtag("config","G-J2JW25BZPF");</script>')


def dots(value):
    filled = "●" * value
    empty = "○" * (5 - value)
    return (f'<span class="text-emerald-600">{filled}</span>'
            f'<span class="text-slate-300">{empty}</span> '
            f'<span class="text-slate-500 text-sm">{value}/5</span>')


def diff_badge(a_val, b_val, lower_is_easier=True):
    if a_val == b_val:
        return '<span class="text-slate-400 text-sm">Same</span>'
    return ""


def yesno(flag, yes="Yes", no="No"):
    if flag:
        return f'<span class="text-emerald-700 font-semibold">{yes}</span>'
    return f'<span class="text-rose-600 font-semibold">{no}</span>'


def table_rows(a, b):
    rows = [
        ("Plant type", a["category"].capitalize(), b["category"].capitalize()),
        ("Difficulty",
         f'<span class="inline-block px-2 py-1 rounded-full text-sm font-medium bg-{{c}}">{norm_difficulty(a)}</span>'.replace(
             "{c}", {"easy": "emerald-100 text-emerald-700", "medium": "amber-100 text-amber-700",
                     "hard": "rose-100 text-rose-700"}[norm_difficulty(a)]),
         f'<span class="inline-block px-2 py-1 rounded-full text-sm font-medium bg-{{c}}">{norm_difficulty(b)}</span>'.replace(
             "{c}", {"easy": "emerald-100 text-emerald-700", "medium": "amber-100 text-amber-700",
                     "hard": "rose-100 text-rose-700"}[norm_difficulty(b)])),
        ("Light", f'{dots(a["light"])}<div class="text-sm text-slate-500 mt-1">{e(LIGHT[a["light"]][0])}</div>',
         f'{dots(b["light"])}<div class="text-sm text-slate-500 mt-1">{e(LIGHT[b["light"]][0])}</div>'),
        ("Water", f'{dots(a["water"])}<div class="text-sm text-slate-500 mt-1">{e(WATER[a["water"]][0])}</div>',
         f'{dots(b["water"])}<div class="text-sm text-slate-500 mt-1">{e(WATER[b["water"]][0])}</div>'),
        ("Humidity", f'{dots(a["humidity"])}<div class="text-sm text-slate-500 mt-1">{e(HUMIDITY[a["humidity"]][0])}</div>',
         f'{dots(b["humidity"])}<div class="text-sm text-slate-500 mt-1">{e(HUMIDITY[b["humidity"]][0])}</div>'),
        ("Pet safe",
         yesno(a["pet_safe"], "Safe", f"Toxic to {toxic_phrase(a)}"),
         yesno(b["pet_safe"], "Safe", f"Toxic to {toxic_phrase(b)}")),
        ("Mature size", f'{SIZE[a["size"]][0]}<div class="text-sm text-slate-500 mt-1">{SIZE[a["size"]][1]}</div>',
         f'{SIZE[b["size"]][0]}<div class="text-sm text-slate-500 mt-1">{SIZE[b["size"]][1]}</div>'),
        ("Growth rate", GROWTH.get(a.get("growth_rate"), "-"), GROWTH.get(b.get("growth_rate"), "-")),
        ("Air purifying", yesno(a.get("air_purifying")), yesno(b.get("air_purifying"))),
        ("Native to", e(a.get("origin") or "-"), e(b.get("origin") or "-")),
    ]
    out = []
    for i, (label, va, vb) in enumerate(rows):
        shade = "bg-slate-50/70" if i % 2 == 0 else ""
        out.append(f"""                    <tr class="{shade} border-b border-slate-100 last:border-0">
                        <th scope="row" class="p-4 text-left text-slate-600 font-medium align-top">{e(label)}</th>
                        <td class="p-4 text-center align-top">{va}</td>
                        <td class="p-4 text-center align-top">{vb}</td>
                    </tr>""")
    return "\n".join(out)


def plant_card(p):
    return f"""            <div class="bg-white rounded-2xl border border-slate-200 p-6">
                <div class="flex items-center gap-4 mb-4">
                    <img src="/images/plants/{e(p['id'])}.webp" alt="{e(p['name'])}" width="64" height="64" loading="lazy" class="w-16 h-16 rounded-xl object-cover bg-emerald-50">
                    <div>
                        <h3 class="font-bold text-slate-900 text-lg"><a href="/plants/{e(p['id'])}/" class="hover:text-emerald-700">{e(p['name'])}</a></h3>
                        <p class="text-sm text-slate-500">{e(', '.join(p.get('common_names') or []) or p['category'].capitalize())}</p>
                    </div>
                </div>
                <p class="text-slate-600 leading-relaxed mb-3">{e(p['description'])}</p>
                <p class="text-slate-600 leading-relaxed"><strong class="text-slate-800">Care in one line:</strong> {e(p.get('care_tips') or '')}</p>
                <a href="/plants/{e(p['id'])}/" class="inline-block mt-4 text-emerald-700 font-semibold hover:underline">Full {e(p['name'])} care guide &rarr;</a>
            </div>"""


def related_for(idx, a_id, b_id):
    out = []
    for j, (x, y, _n) in enumerate(PAIRS):
        if j == idx:
            continue
        if x in (a_id, b_id) or y in (a_id, b_id):
            out.append((x, y))
        if len(out) == 6:
            break
    return out


def render(idx, a_id, b_id, note):
    a, b = PLANTS[a_id], PLANTS[b_id]
    diffs = differences(a, b)
    same = same_notes(a, b)
    slug = pair_slug(a_id, b_id)
    url = f"{BASE}/compare/{slug}/"
    title = title_of(a, b, diffs)
    desc = meta_description(a, b, diffs)
    heading = f"{a['name']} vs {b['name']}"

    diff_html = "\n".join(
        f"""                <div class="border-l-4 border-emerald-400 pl-4 py-1">
                    <h3 class="font-bold text-slate-900 mb-1">{e(head)}</h3>
                    <p class="text-slate-600 leading-relaxed">{e(detail)}</p>
                </div>""" for _axis, head, detail, _w in diffs
    )

    a_reasons = "\n".join(
        f'                        <li class="flex items-start gap-2"><span class="text-emerald-600 font-bold mt-0.5">&check;</span><span>{e(r)}</span></li>'
        for r in pick_reasons(a, b))
    b_reasons = "\n".join(
        f'                        <li class="flex items-start gap-2"><span class="text-teal-600 font-bold mt-0.5">&check;</span><span>{e(r)}</span></li>'
        for r in pick_reasons(b, a))

    lede_answer, lede_evidence = lede(a, b, diffs, same)
    qa = faqs(a, b, diffs, note, same)
    faq_html = "\n".join(
        f"""                <details class="bg-white rounded-xl border border-slate-200 p-5 group">
                    <summary class="font-semibold text-slate-900 cursor-pointer list-none flex justify-between items-center gap-4">
                        <span>{e(q)}</span>
                        <span class="text-emerald-600 text-xl leading-none group-open:rotate-45 transition-transform">+</span>
                    </summary>
                    <p class="text-slate-600 leading-relaxed mt-3">{e(ans)}</p>
                </details>""" for q, ans in qa
    )

    rel = related_for(idx, a_id, b_id)
    rel_html = "\n".join(
        f"""                <a href="/compare/{pair_slug(x, y)}/" class="block bg-white rounded-xl border border-slate-200 p-4 hover:shadow-md hover:border-emerald-200 transition">
                    <span class="font-semibold text-slate-900">{e(PLANTS[x]['name'])} vs {e(PLANTS[y]['name'])}</span>
                </a>""" for x, y in rel)

    faq_schema = json.dumps({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": ans}} for q, ans in qa
        ],
    }, indent=4)

    breadcrumb = json.dumps({
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{BASE}/"},
            {"@type": "ListItem", "position": 2, "name": "Compare Plants",
             "item": f"{BASE}/compare/"},
            {"@type": "ListItem", "position": 3, "name": heading},
        ],
    }, indent=4)

    article = json.dumps({
        "@context": "https://schema.org",
        "@type": "Article",
        "mainEntityOfPage": {"@type": "WebPage", "@id": url},
        "headline": f"{heading}: Care, Light and Water Compared",
        "description": desc,
        "author": {"@type": "Organization", "name": "PlantFinder", "url": f"{BASE}/"},
        "publisher": {
            "@type": "Organization", "name": "PlantFinder",
            "logo": {"@type": "ImageObject",
                     "url": f"{BASE}/logos/logo-icon-512x512.png"},
        },
        "image": [f"{BASE}/images/plants/{a_id}.webp",
                  f"{BASE}/images/plants/{b_id}.webp"],
        "inLanguage": "en",
        "datePublished": TODAY,
        "dateModified": TODAY,
        "about": [{"@type": "Thing", "name": a["name"]},
                  {"@type": "Thing", "name": b["name"]}],
    }, indent=4)

    same_line = ""
    if same:
        joined = same[0] if len(same) == 1 else ", ".join(same[:-1]) + " and " + same[-1]
        same_line = (f'<p class="text-slate-600 mt-4"><strong class="text-slate-800">What they share:</strong> '
                     f'{e(joined)}.</p>')

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
{GA}
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{e(title)}</title>
    <meta name="description" content="{e(desc)}">
    <link rel="canonical" href="{url}">
    <link rel="icon" href="/favicon.svg" type="image/svg+xml">

    <meta property="og:type" content="article">
    <meta property="og:url" content="{url}">
    <meta property="og:title" content="{e(heading)}: {e(title.split(chr(8212))[-1].split('|')[0].strip())}">
    <meta property="og:description" content="{e(desc)}">
    <meta property="og:site_name" content="PlantFinder">
    <meta property="og:image" content="{BASE}/images/plants/{e(a_id)}.webp">

    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{e(heading)}">
    <meta name="twitter:description" content="{e(desc)}">
    <meta name="twitter:image" content="{BASE}/images/plants/{e(a_id)}.webp">

    <link rel="stylesheet" href="/assets/tailwind.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        * {{ font-family: 'Plus Jakarta Sans', sans-serif; }}
        details > summary::-webkit-details-marker {{ display: none; }}
    </style>
    <meta name="theme-color" content="#059669">

    <script type="application/ld+json">
    {article}
    </script>
    <script type="application/ld+json">
    {breadcrumb}
    </script>
    <script type="application/ld+json">
    {faq_schema}
    </script>
    <script src="https://analytics.ahrefs.com/analytics.js" data-key="qlbhxGtUr2oyQ7ePI+y0Qg" async></script>
</head>
<body class="bg-slate-50 text-slate-800">
{NAV}
    <main class="max-w-5xl mx-auto px-4 py-8">
        <nav class="text-sm text-slate-500 mb-6">
            <a href="/" class="hover:text-emerald-600">Home</a>
            <span class="mx-2">/</span>
            <a href="/compare/" class="hover:text-emerald-600">Compare</a>
            <span class="mx-2">/</span>
            <span class="text-slate-700">{e(heading)}</span>
        </nav>

        <header class="mb-8">
            <h1 class="text-3xl md:text-4xl font-extrabold text-slate-900 mb-4">{e(heading)}</h1>
            <p class="text-lg text-slate-800 leading-relaxed font-medium">{e(lede_answer)}</p>
            <p class="text-slate-600 leading-relaxed mt-3">{e(lede_evidence)}</p>
            {same_line}
        </header>

        <!-- Verdict cards -->
        <section class="grid md:grid-cols-2 gap-4 mb-10" aria-label="Which to choose">
            <div class="bg-white rounded-2xl border-2 border-emerald-200 p-6">
                <p class="text-xs uppercase tracking-wide text-emerald-700 font-bold mb-2">Choose</p>
                <h2 class="text-xl font-bold text-slate-900 mb-4">{e(a['name'])} if&hellip;</h2>
                <ul class="space-y-2 text-slate-600">
{a_reasons}
                </ul>
            </div>
            <div class="bg-white rounded-2xl border-2 border-teal-200 p-6">
                <p class="text-xs uppercase tracking-wide text-teal-700 font-bold mb-2">Choose</p>
                <h2 class="text-xl font-bold text-slate-900 mb-4">{e(b['name'])} if&hellip;</h2>
                <ul class="space-y-2 text-slate-600">
{b_reasons}
                </ul>
            </div>
        </section>

        <!-- Comparison table -->
        <section class="mb-10">
            <h2 class="text-2xl font-bold text-slate-900 mb-4">{e(heading)}: side by side</h2>
            <div class="bg-white rounded-2xl border border-slate-200 overflow-hidden">
                <div class="overflow-x-auto">
                <table class="w-full min-w-[520px]">
                    <caption class="sr-only">Care requirements for {e(a['name'])} and {e(b['name'])}</caption>
                    <thead>
                        <tr class="border-b border-slate-200">
                            <th scope="col" class="p-4 text-left text-slate-600 font-medium w-1/4">Attribute</th>
                            <th scope="col" class="p-4 text-center">
                                <a href="/plants/{e(a_id)}/" class="group">
                                    <img src="/images/plants/{e(a_id)}.webp" alt="{e(a['name'])}" width="56" height="56" class="w-14 h-14 rounded-xl object-cover mx-auto mb-2 bg-emerald-50">
                                    <span class="font-bold text-slate-900 group-hover:text-emerald-700">{e(a['name'])}</span>
                                </a>
                            </th>
                            <th scope="col" class="p-4 text-center">
                                <a href="/plants/{e(b_id)}/" class="group">
                                    <img src="/images/plants/{e(b_id)}.webp" alt="{e(b['name'])}" width="56" height="56" class="w-14 h-14 rounded-xl object-cover mx-auto mb-2 bg-emerald-50">
                                    <span class="font-bold text-slate-900 group-hover:text-emerald-700">{e(b['name'])}</span>
                                </a>
                            </th>
                        </tr>
                    </thead>
                    <tbody>
{table_rows(a, b)}
                    </tbody>
                </table>
                </div>
            </div>
        </section>

        <!-- Key differences -->
        <section class="mb-10">
            <h2 class="text-2xl font-bold text-slate-900 mb-5">Key differences between {e(a['name'])} and {e(b['name'])}</h2>
            <div class="space-y-5">
{diff_html}
            </div>
        </section>

        <!-- Telling them apart -->
        <section class="bg-emerald-50 border border-emerald-100 rounded-2xl p-6 md:p-8 mb-10">
            <h2 class="text-2xl font-bold text-slate-900 mb-3">How to tell {e(a['name'])} and {e(b['name'])} apart</h2>
            <p class="text-slate-700 leading-relaxed">{e(note)}</p>
        </section>

        <!-- Care summaries -->
        <section class="mb-10">
            <h2 class="text-2xl font-bold text-slate-900 mb-5">Care at a glance</h2>
            <div class="grid md:grid-cols-2 gap-4">
{plant_card(a)}
{plant_card(b)}
            </div>
        </section>

        <!-- FAQ -->
        <section class="mb-10">
            <h2 class="text-2xl font-bold text-slate-900 mb-5">{e(heading)}: common questions</h2>
            <div class="space-y-3">
{faq_html}
            </div>
        </section>

        <!-- Tool CTA -->
        <section class="bg-gradient-to-br from-emerald-500 to-teal-600 text-white rounded-2xl p-6 md:p-8 mb-10">
            <h2 class="text-2xl font-bold mb-2">Comparing something else?</h2>
            <p class="text-emerald-50 mb-5 leading-relaxed">Put any two or three of our {len(PLANTS)} houseplants head to head on light, water, humidity, size and pet safety.</p>
            <a href="/compare/" class="inline-block bg-white text-emerald-700 px-6 py-3 rounded-xl font-bold hover:bg-emerald-50 transition">Build your own comparison &rarr;</a>
        </section>

        <!-- Related -->
        <section>
            <h2 class="text-2xl font-bold text-slate-900 mb-5">Related comparisons</h2>
            <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-3">
{rel_html}
            </div>
        </section>
    </main>
{FOOTER}
</body>
</html>
"""


# ------------------------------------------------------------------ main ----

def prune_stale(current):
    """Remove comparison directories from earlier runs whose slug has changed."""
    keep = set(current)
    for name in sorted(os.listdir(OUT_ROOT)):
        path = os.path.join(OUT_ROOT, name)
        if not os.path.isdir(path) or name in keep:
            continue
        if "-vs-" not in name:
            continue
        for f in os.listdir(path):
            os.remove(os.path.join(path, f))
        os.rmdir(path)
        print(f"Removed stale /{OUT_ROOT}/{name}/")


def build_pages():
    seen_desc, seen_title, seen_slug = {}, {}, {}
    written = []
    for idx, (a_id, b_id, note) in enumerate(PAIRS):
        slug = pair_slug(a_id, b_id)
        assert slug not in seen_slug, f"duplicate slug {slug}"
        seen_slug[slug] = True

        page = render(idx, a_id, b_id, note)
        a, b = PLANTS[a_id], PLANTS[b_id]
        diffs = differences(a, b)
        d = meta_description(a, b, diffs)
        t = title_of(a, b, diffs)
        assert d not in seen_desc, f"duplicate description: {slug} / {seen_desc.get(d)}"
        assert t not in seen_title, f"duplicate title: {slug} / {seen_title.get(t)}"
        seen_desc[d], seen_title[t] = slug, slug

        d_out = os.path.join(OUT_ROOT, slug)
        os.makedirs(d_out, exist_ok=True)
        with open(os.path.join(d_out, "index.html"), "w") as f:
            f.write(page)
        written.append(slug)
    prune_stale(written)
    return written





# ------------------------------------------------- compare/ hub index -------

GROUP_ORDER = [
    ("foliage", "Foliage &amp; statement plants"),
    ("trailing", "Trailing &amp; vining plants"),
    ("succulent", "Succulents"),
    ("cactus", "Cacti"),
    ("fern", "Ferns"),
    ("palm", "Palms"),
    ("flowering", "Flowering plants"),
]


def group_of(a, b):
    """Shared category if they have one, otherwise the first plant's."""
    if a["category"] == b["category"]:
        return a["category"]
    order = [k for k, _ in GROUP_ORDER]
    return min((a["category"], b["category"]), key=order.index)


def build_index_html():
    buckets = {k: [] for k, _ in GROUP_ORDER}
    for a_id, b_id, _note in PAIRS:
        a, b = PLANTS[a_id], PLANTS[b_id]
        buckets[group_of(a, b)].append((a, b))

    blocks = []
    for key, heading in GROUP_ORDER:
        items = sorted(buckets[key], key=lambda ab: (ab[0]["name"], ab[1]["name"]))
        if not items:
            continue
        cards = "\n".join(
            f"""                    <a href="/compare/{pair_slug(a['id'], b['id'])}/" class="bg-white p-4 rounded-xl shadow-sm hover:shadow-md hover:ring-1 hover:ring-emerald-200 transition block">
                        <span class="font-semibold text-slate-800">{e(a['name'])} vs {e(b['name'])}</span>
                        <p class="text-sm text-slate-600 mt-1">{e(index_hook(a, b))}</p>
                    </a>""" for a, b in items)
        blocks.append(f"""            <h3 class="text-lg font-bold text-slate-800 mt-8 mb-4">{heading}</h3>
                <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-4">
{cards}
                </div>""")

    item_list = json.dumps({
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": "Houseplant comparisons",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1,
             "name": f"{PLANTS[x]['name']} vs {PLANTS[y]['name']}",
             "url": f"{BASE}/compare/{pair_slug(x, y)}/"}
            for i, (x, y, _n) in enumerate(PAIRS)
        ],
    }, indent=4)

    return f"""        <!-- COMPARISON-INDEX:START (generated by generate_comparisons.py) -->
        <script type="application/ld+json">
{item_list}
        </script>
        <section class="mt-16">
            <h2 class="text-2xl font-bold mb-2">Ready-made comparisons</h2>
            <p class="text-slate-600 mb-2">{len(PAIRS)} head-to-head guides, each answering which plant is easier, which is pet-safe and which suits your light.</p>
{chr(10).join(blocks)}
        </section>
        <!-- COMPARISON-INDEX:END -->"""


def index_hook(a, b):
    """One line per card -- the reason to click, not a restatement of the title."""
    diffs = differences(a, b)
    axis = diffs[0][0] if diffs else "same"
    if axis == "pets":
        safe = a if a["pet_safe"] else b
        return f"{safe['name']} is the pet-safe one"
    if axis == "difficulty":
        easier = a if DIFF_RANK[norm_difficulty(a)] < DIFF_RANK[norm_difficulty(b)] else b
        return f"{easier['name']} is the easier plant"
    if axis == "light":
        lower = a if a["light"] < b["light"] else b
        return f"{lower['name']} takes the darker spot"
    if axis == "water":
        lower = a if a["water"] < b["water"] else b
        return f"{lower['name']} needs less water"
    if axis == "humidity":
        lower = a if a["humidity"] < b["humidity"] else b
        return f"{lower['name']} copes with drier air"
    if axis == "size":
        big = a if SIZE_RANK[a["size"]] > SIZE_RANK[b["size"]] else b
        return f"{big['name']} is the bigger plant"
    if axis == "growth":
        fast = a if GROWTH_RANK[a["growth_rate"]] > GROWTH_RANK[b["growth_rate"]] else b
        return f"{fast['name']} grows faster"
    return "Same care - told apart by looks"


def update_compare_index():
    path = os.path.join(OUT_ROOT, "index.html")
    with open(path) as f:
        s = f.read()
    start = s.index("        <!-- COMPARISON-INDEX:START")
    end = s.index("<!-- COMPARISON-INDEX:END -->") + len("<!-- COMPARISON-INDEX:END -->")
    s = s[:start] + build_index_html() + s[end:]
    with open(path, "w") as f:
        f.write(s)
    print(f"Updated /{OUT_ROOT}/index.html with {len(PAIRS)} links")


def update_sitemap(slugs):
    """Add/refresh the comparison URLs in sitemap.xml, leaving the rest alone.

    sitemap.xml carries hand-added entries that scripts/generate_sitemap.py does
    not know about, so this edits in place rather than regenerating.
    """
    path = "sitemap.xml"
    with open(path) as f:
        s = f.read()

    marker_start = "    <!-- COMPARISONS:START -->"
    marker_end = "    <!-- COMPARISONS:END -->"
    block = "\n".join(
        f"""    <url>
        <loc>{BASE}/compare/{slug}/</loc>
        <lastmod>{TODAY}</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.7</priority>
    </url>""" for slug in slugs)
    section = f"{marker_start}\n{block}\n{marker_end}"

    if marker_start in s:
        start = s.index(marker_start)
        end = s.index(marker_end) + len(marker_end)
        s = s[:start] + section + s[end:]
    else:
        s = s.replace("</urlset>", section + "\n</urlset>")

    with open(path, "w") as f:
        f.write(s)
    print(f"Updated sitemap.xml with {len(slugs)} comparison URLs")


# ---------------------------------------------- plant-page cross-links ------

PLANT_MARK_START = "    <!-- COMPARISONS:START (generated by generate_comparisons.py) -->"
PLANT_MARK_END = "    <!-- COMPARISONS:END -->"


def relative_hook(me, other):
    """Describe `other` relative to `me` -- so one plant page gets varied hooks
    rather than the same line repeated down the grid."""
    phrases = []
    if other["pet_safe"] != me["pet_safe"]:
        phrases.append("pet-safe" if other["pet_safe"] else "toxic to pets")
    dm, do = DIFF_RANK[norm_difficulty(me)], DIFF_RANK[norm_difficulty(other)]
    if do != dm:
        phrases.append("easier to grow" if do < dm else "fussier")
    if other["light"] != me["light"]:
        phrases.append("takes a darker spot" if other["light"] < me["light"]
                       else "needs more light")
    if other["water"] != me["water"]:
        phrases.append("needs less water" if other["water"] < me["water"]
                       else "drinks more")
    if other["humidity"] != me["humidity"]:
        phrases.append("copes with drier air" if other["humidity"] < me["humidity"]
                       else "wants damper air")
    if other["size"] != me["size"]:
        phrases.append("bigger" if SIZE_RANK[other["size"]] > SIZE_RANK[me["size"]]
                       else "more compact")
    if other.get("growth_rate") and me.get("growth_rate") and other["growth_rate"] != me["growth_rate"]:
        phrases.append("grows faster"
                       if GROWTH_RANK[other["growth_rate"]] > GROWTH_RANK[me["growth_rate"]]
                       else "grows slower")
    if not phrases:
        return "Same care, told apart by looks"
    hook = ", ".join(phrases[:2])
    return hook[0].upper() + hook[1:]


def update_plant_pages():
    """Link each plant page to the comparisons it appears in.

    Without this the comparison pages hang off /compare/ alone; the plant pages
    are where people (and crawlers) actually land.
    """
    by_plant = {}
    for a_id, b_id, _note in PAIRS:
        by_plant.setdefault(a_id, []).append((a_id, b_id))
        by_plant.setdefault(b_id, []).append((a_id, b_id))

    touched = 0
    for pid, pairs in by_plant.items():
        path = os.path.join("plants", pid, "index.html")
        if not os.path.exists(path):
            print(f"  skipped {pid}: no plant page")
            continue
        with open(path) as f:
            s = f.read()

        me = PLANTS[pid]
        cards = []
        for a_id, b_id in pairs[:6]:
            other = PLANTS[b_id if a_id == pid else a_id]
            cards.append(
                f"""            <a href="/compare/{pair_slug(a_id, b_id)}/" class="block bg-white rounded-lg border border-slate-200 p-4 hover:shadow-md transition">
                <h3 class="font-bold text-slate-900">vs {e(other['name'])}</h3>
                <p class="text-sm text-slate-500 mt-1">{e(relative_hook(me, other))}</p>
            </a>""")

        block = f"""{PLANT_MARK_START}
    <section class="mt-12 mb-8">
        <h2 class="text-xl font-bold text-slate-900 mb-6">{e(me['name'])} compared with&hellip;</h2>
        <div class="grid grid-cols-2 md:grid-cols-3 gap-4">
{chr(10).join(cards)}
        </div>
        <a href="/compare/" class="inline-block mt-4 text-emerald-700 font-semibold hover:underline">Compare {e(me['name'])} with any other plant &rarr;</a>
    </section>
{PLANT_MARK_END}
"""

        if PLANT_MARK_START in s:
            start = s.index(PLANT_MARK_START)
            end = s.index(PLANT_MARK_END) + len(PLANT_MARK_END) + 1
            s = s[:start] + block + s[end:]
        else:
            anchor = "    <!-- Related Plants Section -->"
            if anchor not in s:
                print(f"  skipped {pid}: no insertion point")
                continue
            s = s.replace(anchor, block + anchor, 1)

        with open(path, "w") as f:
            f.write(s)
        touched += 1
    print(f"Linked comparisons from {touched} plant pages")


if __name__ == "__main__":
    pages = build_pages()
    print(f"Wrote {len(pages)} comparison pages under /{OUT_ROOT}/")
    update_compare_index()
    update_sitemap(pages)
    update_plant_pages()
