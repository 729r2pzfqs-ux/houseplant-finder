#!/usr/bin/env python3
"""Generate all plant pages for PlantFinder"""

import json

# Size to height mapping
size_heights = {
    "small": "15-30 cm (6-12 in)",
    "medium": "30-90 cm (1-3 ft)", 
    "large": "90-180+ cm (3-6+ ft)"
}

import os
from datetime import datetime

# Configuration
BASE_DIR = os.path.expanduser("~/clawd/houseplant-finder")
PLANTS_DIR = os.path.join(BASE_DIR, "plants")
DATA_FILE = os.path.join(BASE_DIR, "data/plants.json")
SITEMAP_FILE = os.path.join(BASE_DIR, "sitemap.xml")
BASE_URL = "https://plantfinder.org"
GA_ID = "G-J2JW25BZPF"
PAGE_META_FILE = os.path.join(BASE_DIR, "data/page_meta.json")
DATE_PUBLISHED = "2026-02-22"
DATE_MODIFIED = "2026-07-06"

# Per-plant meta description and publish date, authored separately from the page
# template. Both fall back to a derived value for any plant without an entry.
try:
    with open(PAGE_META_FILE, encoding="utf-8") as _f:
        PAGE_META = json.load(_f).get("en", {})
except FileNotFoundError:
    PAGE_META = {}

# FAQ phrasing, keyed off the plant's numeric care ratings.
faq_light_phrases = {
    1: "low light", 2: "low-medium light", 3: "medium light",
    4: "bright indirect", 5: "bright/direct",
}
faq_water_phrases = {
    1: "very low", 2: "low", 3: "moderate", 4: "regular", 5: "frequent",
}
faq_difficulty_phrases = {
    "easy": "easy", "medium": "medium", "moderate": "moderate", "hard": "hard",
}


def json_escape(text):
    """Escape a string for embedding in a JSON-LD literal."""
    return json.dumps(str(text))[1:-1]


def build_faq_schema(plant, name, page_url):
    """FAQPage schema: light, toxicity, difficulty and watering."""
    light = plant.get("light", 3)
    water = plant.get("water", 3)
    difficulty = plant.get("difficulty", "medium")
    growth_rate = plant.get("growth_rate", "moderate")
    pet_safe = plant.get("pet_safe", False)
    toxic_to = plant.get("toxic_to", [])
    care_tips = plant.get("care_tips", "")

    light_phrase = faq_light_phrases.get(light, "medium light")
    water_phrase = faq_water_phrases.get(water, "moderate")
    diff_phrase = faq_difficulty_phrases.get(difficulty, difficulty)

    if pet_safe:
        tox_q = f"Is {name} safe for pets?"
        tox_a = f"Yes, the {name} is non-toxic and safe for cats and dogs."
    else:
        pets = ", ".join(toxic_to) if toxic_to else "pets"
        tox_q = f"Is {name} toxic to pets?"
        tox_a = f"Yes, the {name} is toxic to {pets}. Keep it out of reach of pets."

    qa = [
        (f"How much light does a {name} need?",
         f"The {name} needs {light_phrase} conditions. {care_tips}".strip()),
        (tox_q, tox_a),
        (f"Is {name} easy to care for?",
         f"The {name} is considered {diff_phrase} to care for. "
         f"It has {water_phrase} watering needs and grows at a {growth_rate} rate."),
        (f"How often should I water my {name}?",
         f"The {name} has {water_phrase} watering needs. {care_tips}".strip()),
    ]
    entities = ",\n".join(
        '''        {
            "@type": "Question",
            "name": "%s",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "%s"
            }
        }''' % (json_escape(q), json_escape(a))
        for q, a in qa
    )
    return '''    <!-- FAQ Schema -->
    <script type="application/ld+json">
    {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
%s
    ]
}
    </script>''' % entities

def get_light_label(level):
    labels = {1: "Very Low", 2: "Low", 3: "Medium (Indirect)", 4: "Bright Indirect", 5: "Direct Sun"}
    return labels.get(level, "Medium")

def get_water_label(level):
    labels = {1: "Very Low", 2: "Low", 3: "Moderate", 4: "Frequent", 5: "Constant"}
    return labels.get(level, "Moderate")

def get_humidity_label(level):
    labels = {1: "Very Low", 2: "Low", 3: "Average", 4: "High", 5: "Very High"}
    return labels.get(level, "Average")

def get_difficulty_badge(difficulty):
    colors = {
        "easy": ("emerald", "Easy Care"),
        "medium": ("amber", "Moderate Care"),
        "hard": ("rose", "Expert Care")
    }
    color, text = colors.get(difficulty, ("slate", difficulty.title()))
    return f'<span class="bg-{color}-100 text-{color}-700 px-3 py-1 rounded-full text-sm font-medium">{text}</span>'

def get_growth_rate_value(rate):
    values = {"slow": 2, "moderate": 3, "fast": 5}
    return values.get(rate, 3)

def generate_plant_html(plant):
    plant_id = plant["id"]
    name = plant["name"]
    common_names = plant.get("common_names", [])
    common_names_str = ", ".join(common_names) if common_names else ""
    
    light = plant.get("light", 3)
    water = plant.get("water", 3)
    humidity = plant.get("humidity", 3)
    difficulty = plant.get("difficulty", "medium")
    pet_safe = plant.get("pet_safe", False)
    toxic_to = plant.get("toxic_to", [])
    size = plant.get("size", "medium").title()
    size_height = size_heights.get(plant.get("size", "medium"), "30-90 cm")
    growth_rate = plant.get("growth_rate", "moderate")
    air_purifying = plant.get("air_purifying", False)
    description = plant.get("description", "")
    care_tips = plant.get("care_tips", "")
    origin = plant.get("origin", "")
    category = plant.get("category", "foliage")
    
    # Calculate maintenance (inverse of difficulty)
    maintenance_map = {"easy": 2, "medium": 3, "hard": 4}
    maintenance = maintenance_map.get(difficulty, 3)
    
    # Build badges
    badges = [get_difficulty_badge(difficulty)]
    badges.append(f'<span class="bg-teal-100 text-teal-700 px-3 py-1 rounded-full text-sm font-medium">{category.title()}</span>')
    if not pet_safe:
        badges.append('<span class="bg-rose-100 text-rose-700 px-3 py-1 rounded-full text-sm font-medium">⚠️ Toxic to Pets</span>')
    else:
        badges.append('<span class="bg-green-100 text-green-700 px-3 py-1 rounded-full text-sm font-medium">✓ Pet Safe</span>')
    
    badges_html = "\n                        ".join(badges)
    
    # Pet warning section
    pet_warning_html = ""
    if not pet_safe and toxic_to:
        pets_str = " and ".join(toxic_to)
        pet_warning_html = f'''
        <!-- Pet Safety Warning -->
        <div class="bg-rose-50 border border-rose-200 rounded-2xl p-6 mb-8">
            <div class="flex items-start gap-4">
                <div class="w-12 h-12 bg-rose-100 rounded-xl flex items-center justify-center flex-shrink-0">
                    <i data-lucide="alert-triangle" class="w-6 h-6 text-rose-600"></i>
                </div>
                <div>
                    <h3 class="font-bold text-rose-800 mb-1">⚠️ Toxic to Pets</h3>
                    <p class="text-rose-700">{name} contains compounds that are toxic to {pets_str} if ingested. Keep this plant out of reach of pets, or consider a <a href="/search/?pet_safe=true" class="underline hover:no-underline">pet-safe alternative</a>.</p>
                </div>
            </div>
        </div>
'''
    elif pet_safe:
        pet_warning_html = f'''
        <!-- Pet Safety Notice -->
        <div class="bg-green-50 border border-green-200 rounded-2xl p-6 mb-8">
            <div class="flex items-start gap-4">
                <div class="w-12 h-12 bg-green-100 rounded-xl flex items-center justify-center flex-shrink-0">
                    <i data-lucide="heart" class="w-6 h-6 text-green-600"></i>
                </div>
                <div>
                    <h3 class="font-bold text-green-800 mb-1">✓ Pet Safe</h3>
                    <p class="text-green-700">{name} is non-toxic and safe for homes with cats and dogs.</p>
                </div>
            </div>
        </div>
'''
    
    # Additional badges for size, growth rate, air purifying
    info_badges = []
    info_badges.append(f'''<div class="flex items-center gap-2 px-4 py-2 bg-slate-100 rounded-xl">
                            <i data-lucide="ruler" class="w-4 h-4 text-slate-600"></i>
                            <span class="text-sm font-medium text-slate-700">{size}</span>
                        </div>''')
    info_badges.append(f'''<div class="flex items-center gap-2 px-4 py-2 bg-slate-100 rounded-xl">
                            <i data-lucide="trending-up" class="w-4 h-4 text-slate-600"></i>
                            <span class="text-sm font-medium text-slate-700">{growth_rate.title()} Growth</span>
                        </div>''')
    if air_purifying:
        info_badges.append('''<div class="flex items-center gap-2 px-4 py-2 bg-emerald-100 rounded-xl">
                            <i data-lucide="wind" class="w-4 h-4 text-emerald-600"></i>
                            <span class="text-sm font-medium text-emerald-700">Air Purifying</span>
                        </div>''')
    
    info_badges_html = "\n                        ".join(info_badges)
    
    # Best for / Not ideal for based on plant characteristics
    best_for = []
    not_ideal = []
    
    if light <= 2:
        best_for.append("Low light rooms and offices")
    elif light >= 4:
        best_for.append("Bright rooms with good natural light")
    else:
        best_for.append("Living rooms with indirect light")
    
    if difficulty == "easy":
        best_for.append("Beginners and busy plant parents")
    elif difficulty == "hard":
        not_ideal.append("Beginners or those with limited time")
    
    if pet_safe:
        best_for.append("Homes with cats and dogs")
    else:
        not_ideal.append("Homes with curious pets")
    
    if water <= 2:
        best_for.append("Forgetful waterers")
    elif water >= 4:
        not_ideal.append("Frequent travelers")
    
    if size == "Large":
        best_for.append("Making a statement in spacious rooms")
        not_ideal.append("Small apartments or tight spaces")
    elif size == "Small":
        best_for.append("Desks, shelves, and small spaces")
    
    if humidity >= 4:
        best_for.append("Bathrooms or rooms with humidifiers")
        not_ideal.append("Very dry climates without humidity control")
    
    if air_purifying:
        best_for.append("Improving indoor air quality")
    
    if category == "trailing":
        best_for.append("Hanging baskets and high shelves")
    elif category == "succulent" or category == "cactus":
        best_for.append("Sunny windowsills")
    
    best_for_html = "\n                        ".join([f'<li class="flex items-start gap-2"><i data-lucide="check" class="w-5 h-5 text-green-500 flex-shrink-0 mt-0.5"></i><span>{item}</span></li>' for item in best_for[:4]])
    not_ideal_html = "\n                        ".join([f'<li class="flex items-start gap-2"><i data-lucide="x" class="w-5 h-5 text-red-500 flex-shrink-0 mt-0.5"></i><span>{item}</span></li>' for item in not_ideal[:3]])
    
    growth_rate_val = get_growth_rate_value(growth_rate)
    air_purifying_val = 4 if air_purifying else 1

    page_meta = PAGE_META.get(plant_id, {})
    date_published = page_meta.get("date_published", DATE_PUBLISHED)
    meta_description = page_meta.get(
        "description",
        f"Complete care guide for {name}{' (' + common_names[0] + ')' if common_names else ''}. "
        f"Learn about light, water, humidity needs, and how to keep your {name} thriving."
    )
    image_url = f"{BASE_URL}/images/plants/{plant_id}.webp"
    page_url = f"{BASE_URL}/plants/{plant_id}/"
    faq_schema = build_faq_schema(plant, name, page_url)

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script><script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag("js",new Date());gtag("config","{GA_ID}");</script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} Care Guide | PlantFinder</title>
    <meta name="description" content="{meta_description}">
    <link rel="canonical" href="{page_url}">
    <meta property="og:title" content="{name} Care Guide | PlantFinder">
    <meta property="og:description" content="{description}">
    <meta property="og:url" content="{page_url}">
    <meta property="og:type" content="article">
    <meta property="og:site_name" content="PlantFinder">
    <meta property="og:image" content="{image_url}">
    <meta property="og:image:width" content="1024">
    <meta property="og:image:height" content="1536">
    <link rel="icon" href="/favicon.svg" type="image/svg+xml">
    <link rel="stylesheet" href="/assets/tailwind.css">
    <script defer src="https://unpkg.com/lucide@1.47.0/dist/umd/lucide.min.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        .rating-bar {{ height: 8px; background: #e2e8f0; border-radius: 4px; overflow: hidden; }}
        .rating-bar::after {{ content: ''; display: block; height: 100%; border-radius: 4px; background: linear-gradient(90deg, #10b981, #14b8a6); }}
        .rating-1::after {{ width: 20%; }}
        .rating-2::after {{ width: 40%; }}
        .rating-3::after {{ width: 60%; }}
        .rating-4::after {{ width: 80%; }}
        .rating-5::after {{ width: 100%; }}
    </style>

    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{name} Care Guide">
    <meta name="twitter:description" content="{description}">
    <meta name="twitter:image" content="{image_url}">

    <!-- Schema.org Markup -->
    <script type="application/ld+json">
    {{
    "@context": "https://schema.org",
    "@type": "Article",
    "mainEntityOfPage": {{
        "@type": "WebPage",
        "@id": "{page_url}"
    }},
    "headline": "{name}: Complete Care Guide, Light & Water Needs",
    "description": "{description}",
    "author": {{
        "@type": "Organization",
        "name": "PlantFinder",
        "url": "{BASE_URL}/"
    }},
    "publisher": {{
        "@type": "Organization",
        "name": "PlantFinder",
        "logo": {{
            "@type": "ImageObject",
            "url": "{BASE_URL}/logos/logo-icon-512x512.png"
        }}
    }},
    "image": [
        "{image_url}"
    ],
    "inLanguage": "en",
    "datePublished": "{date_published}",
    "dateModified": "{DATE_MODIFIED}",
    "about": {{
        "@type": "Thing",
        "name": "{name}"
    }}
}}
    </script>

    <!-- Breadcrumb Schema -->
    <script type="application/ld+json">
    {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
        {{
            "@type": "ListItem",
            "position": 1,
            "name": "Home",
            "item": "{BASE_URL}/"
        }},
        {{
            "@type": "ListItem",
            "position": 2,
            "name": "Plants",
            "item": "{BASE_URL}/search/"
        }},
        {{
            "@type": "ListItem",
            "position": 3,
            "name": "{name}"
        }}
    ]
}}
    </script>
    <link rel="alternate" hreflang="en" href="{BASE_URL}/plants/{plant_id}/" />
    <link rel="alternate" hreflang="es" href="{BASE_URL}/es/plants/{plant_id}/" />
    <link rel="alternate" hreflang="de" href="{BASE_URL}/de/plants/{plant_id}/" />
    <link rel="alternate" hreflang="x-default" href="{BASE_URL}/plants/{plant_id}/" />

{faq_schema}
<script src="https://analytics.ahrefs.com/analytics.js" data-key="qlbhxGtUr2oyQ7ePI+y0Qg" async></script>
</head>
<body class="bg-slate-50 text-slate-800">
    <nav class="bg-white/80 backdrop-blur-md border-b border-slate-200 sticky top-0 z-50">
        <div class="max-w-6xl mx-auto px-4 py-4">
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
                <div class="flex items-center gap-4 md:gap-6">
                    <a href="/search/" class="text-slate-600 hover:text-slate-900 font-medium hidden sm:block">Browse</a>
                    <a href="/quiz/" class="text-slate-600 hover:text-slate-900 font-medium hidden sm:block">Quiz</a>
                    <a href="/compare/" class="text-slate-600 hover:text-slate-900 font-medium hidden sm:block">Compare</a>
                    <!-- Language selector -->
                    <div class="relative group">
                        <button class="flex items-center gap-1 text-slate-600 hover:text-emerald-700 py-2">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
                            <span>EN</span>
                        </button>
                        <div class="absolute right-0 top-full bg-white border border-slate-200 rounded-xl shadow-xl hidden group-hover:block min-w-[140px] py-2 z-50">
                            <a href="/plants/{plant_id}/" class="block px-4 py-2 hover:bg-slate-100 font-semibold text-emerald-700">English</a>
                            <a href="/es/plants/{plant_id}/" class="block px-4 py-2 hover:bg-slate-100 text-slate-600">Español</a>
                            <a href="/de/plants/{plant_id}/" class="block px-4 py-2 hover:bg-slate-100 text-slate-600">Deutsch</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </nav>

    <main class="max-w-6xl mx-auto px-4 py-8">
        <nav class="text-sm text-slate-500 mb-6">
            <a href="/" class="hover:text-emerald-600">Home</a>
            <span class="mx-2">/</span>
            <a href="/search/" class="hover:text-emerald-600">Plants</a>
            <span class="mx-2">/</span>
            <span class="text-slate-700">{name}</span>
        </nav>

        <div class="bg-white rounded-2xl shadow-sm border border-slate-200 overflow-hidden mb-8">
            <div class="md:flex">
                <div class="md:w-2/5">
                    <div class="aspect-[4/5] bg-gradient-to-br from-emerald-100 via-teal-100 to-lime-100 relative overflow-hidden flex items-center justify-center p-8">
                        <img src="/images/plants/{plant_id}.webp" alt="{name}" class="w-full h-full object-contain" onerror="this.onerror=null; this.src=''; this.parentElement.innerHTML='<span class=\'text-9xl\'>🪴</span>'">
                    </div>
                </div>
                <div class="md:w-3/5 p-6 md:p-8">
                    <div class="flex flex-wrap gap-2 mb-4">
                        {badges_html}
                    </div>
                    <h1 class="text-3xl md:text-4xl font-bold text-slate-900 mb-2">{name}</h1>
                    {f'<p class="text-slate-500 mb-4">Also known as: {common_names_str}</p>' if common_names_str else '<div class="mb-4"></div>'}
                    
                    <div class="flex flex-wrap gap-2 mb-6">
                        {info_badges_html}
                    </div>
                    
                    <div class="grid grid-cols-2 gap-4">
                        <div class="flex items-center gap-3 p-3 bg-slate-50 rounded-xl">
                            <i data-lucide="sun" class="w-6 h-6 text-amber-500"></i>
                            <div>
                                <p class="text-xs text-slate-500">Light</p>
                                <p class="font-semibold text-slate-700">{get_light_label(light)}</p>
                            </div>
                        </div>
                        <div class="flex items-center gap-3 p-3 bg-slate-50 rounded-xl">
                            <i data-lucide="droplets" class="w-6 h-6 text-blue-500"></i>
                            <div>
                                <p class="text-xs text-slate-500">Water</p>
                                <p class="font-semibold text-slate-700">{get_water_label(water)}</p>
                            </div>
                        </div>
                        <div class="flex items-center gap-3 p-3 bg-slate-50 rounded-xl">
                            <i data-lucide="cloud" class="w-6 h-6 text-cyan-500"></i>
                            <div>
                                <p class="text-xs text-slate-500">Humidity</p>
                                <p class="font-semibold text-slate-700">{get_humidity_label(humidity)}</p>
                            </div>
                        </div>
                        <div class="flex items-center gap-3 p-3 bg-slate-50 rounded-xl">
                            <i data-lucide="ruler" class="w-6 h-6 text-emerald-500"></i>
                            <div>
                                <p class="text-xs text-slate-500">Size</p>
                                <p class="font-semibold text-slate-700">{size}</p>
                                <p class="text-xs text-slate-500 mt-1">{size_height}</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

{pet_warning_html}
        <!-- Care Ratings -->
        <section class="bg-white rounded-2xl shadow-sm border border-slate-200 p-6 md:p-8 mb-8">
            <h2 class="text-xl font-bold text-slate-900 mb-6">Care Requirements</h2>
            <div class="grid md:grid-cols-2 gap-x-12 gap-y-4">
                <div>
                    <div class="flex justify-between mb-2"><span class="text-slate-600">Light Needs</span><span class="font-medium">{light}/5</span></div>
                    <div class="rating-bar rating-{light}"></div>
                </div>
                <div>
                    <div class="flex justify-between mb-2"><span class="text-slate-600">Water Needs</span><span class="font-medium">{water}/5</span></div>
                    <div class="rating-bar rating-{water}"></div>
                </div>
                <div>
                    <div class="flex justify-between mb-2"><span class="text-slate-600">Humidity Needs</span><span class="font-medium">{humidity}/5</span></div>
                    <div class="rating-bar rating-{humidity}"></div>
                </div>
                <div>
                    <div class="flex justify-between mb-2"><span class="text-slate-600">Maintenance</span><span class="font-medium">{maintenance}/5</span></div>
                    <div class="rating-bar rating-{maintenance}"></div>
                </div>
                <div>
                    <div class="flex justify-between mb-2"><span class="text-slate-600">Growth Speed</span><span class="font-medium">{growth_rate_val}/5</span></div>
                    <div class="rating-bar rating-{growth_rate_val}"></div>
                </div>
                <div>
                    <div class="flex justify-between mb-2"><span class="text-slate-600">Air Purifying</span><span class="font-medium">{air_purifying_val}/5</span></div>
                    <div class="rating-bar rating-{air_purifying_val}"></div>
                </div>
            </div>
        </section>

        <!-- About -->
        <section class="bg-white rounded-2xl shadow-sm border border-slate-200 p-6 md:p-8 mb-8">
            <h2 class="text-xl font-bold text-slate-900 mb-4">About the {name}</h2>
            <p class="text-slate-600 leading-relaxed mb-4">{description}</p>
            {f'<p class="text-slate-600 leading-relaxed"><strong>Origin:</strong> {origin}</p>' if origin else ''}
        </section>

        <!-- Care Tips -->
        <section class="bg-white rounded-2xl shadow-sm border border-slate-200 p-6 md:p-8 mb-8">
            <h2 class="text-xl font-bold text-slate-900 mb-4">Care Tips</h2>
            <div class="bg-emerald-50 rounded-xl p-5">
                <div class="flex items-start gap-3">
                    <i data-lucide="lightbulb" class="w-6 h-6 text-emerald-600 mt-0.5"></i>
                    <p class="text-slate-700">{care_tips}</p>
                </div>
            </div>
        </section>

        <!-- Is This Plant Right for You? -->
        <section class="bg-gradient-to-br from-emerald-50 via-teal-50 to-lime-50 rounded-2xl p-6 md:p-8 mb-8">
            <h2 class="text-xl font-bold text-slate-900 mb-6">Is This Plant Right for You?</h2>
            <div class="grid md:grid-cols-2 gap-6 mb-6">
                <div class="bg-white rounded-xl p-5 shadow-sm">
                    <h3 class="font-semibold text-green-700 mb-3 flex items-center gap-2">
                        <i data-lucide="check-circle" class="w-5 h-5"></i>
                        Best For
                    </h3>
                    <ul class="space-y-2 text-slate-600">
                        {best_for_html}
                    </ul>
                </div>
                <div class="bg-white rounded-xl p-5 shadow-sm">
                    <h3 class="font-semibold text-red-700 mb-3 flex items-center gap-2">
                        <i data-lucide="x-circle" class="w-5 h-5"></i>
                        Not Ideal For
                    </h3>
                    <ul class="space-y-2 text-slate-600">
                        {not_ideal_html if not_ideal_html else '<li class="text-slate-400">No major concerns!</li>'}
                    </ul>
                </div>
            </div>
            
            <div class="flex flex-wrap gap-3">
                <a href="/compare/" class="inline-flex items-center gap-2 bg-white text-slate-700 border border-slate-200 px-5 py-2.5 rounded-xl font-semibold hover:border-slate-300 hover:shadow-md transition">
                    <i data-lucide="scale" class="w-4 h-4"></i>
                    Compare with other plants
                </a>
                {f'<a href="/search/?pet_safe=true" class="inline-flex items-center gap-2 bg-emerald-600 text-white px-5 py-2.5 rounded-xl font-semibold hover:bg-emerald-700 transition"><i data-lucide="paw-print" class="w-4 h-4"></i>Find pet-safe alternatives</a>' if not pet_safe else ''}
            </div>
        </section>
    </main>

    <footer class="bg-slate-900 text-slate-400 py-12">
        <div class="max-w-6xl mx-auto px-4">
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
    
    <script>
        document.addEventListener('DOMContentLoaded', () => lucide.createIcons());
    </script>
</body>
</html>'''
    
    return html


def generate_sitemap(plants):
    """Generate sitemap.xml with all plant URLs"""
    today = datetime.now().strftime("%Y-%m-%d")
    
    sitemap = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>{BASE_URL}/</loc>
        <lastmod>{today}</lastmod>
        <changefreq>weekly</changefreq>
        <priority>1.0</priority>
    </url>
    <url>
        <loc>{BASE_URL}/search/</loc>
        <lastmod>{today}</lastmod>
        <changefreq>weekly</changefreq>
        <priority>0.9</priority>
    </url>
    <url>
        <loc>{BASE_URL}/quiz/</loc>
        <lastmod>{today}</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.8</priority>
    </url>
    <url>
        <loc>{BASE_URL}/compare/</loc>
        <lastmod>{today}</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.8</priority>
    </url>
    <url>
        <loc>{BASE_URL}/faq/</loc>
        <lastmod>{today}</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.7</priority>
    </url>
'''
    
    for plant in plants:
        sitemap += f'''    <url>
        <loc>{BASE_URL}/plants/{plant["id"]}/</loc>
        <lastmod>{today}</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.8</priority>
    </url>
'''
    
    sitemap += '</urlset>'
    return sitemap


# Blocks appended to plant pages by later passes (generate_comparisons.py, and the
# "Related Plants" cards). They live between the template's last section and
# </main>. Regenerating must not drop them, so they are carried across.
INJECTED_ANCHORS = (
    "    <!-- COMPARISONS:START",
    "    <!-- Related Plants Section -->",
)


def extract_injected_blocks(path):
    """Return the post-generation blocks in an existing page, or ''."""
    try:
        with open(path, encoding="utf-8") as f:
            existing = f.read()
    except FileNotFoundError:
        return ""
    starts = [existing.index(a) for a in INJECTED_ANCHORS if a in existing]
    if not starts:
        return ""
    end = existing.rfind("</main>")
    if end == -1 or end <= min(starts):
        return ""
    return existing[min(starts):end]


def main():
    # Load plant data
    print(f"Loading plant data from {DATA_FILE}...")
    with open(DATA_FILE, 'r') as f:
        plants = json.load(f)
    
    print(f"Found {len(plants)} plants")
    
    # Generate pages for each plant
    created = 0
    skipped = 0
    
    for plant in plants:
        plant_id = plant["id"]
        plant_dir = os.path.join(PLANTS_DIR, plant_id)
        plant_file = os.path.join(plant_dir, "index.html")
        
        # Create directory if needed
        os.makedirs(plant_dir, exist_ok=True)
        
        # Generate HTML, carrying over any blocks added by later passes
        preserved = extract_injected_blocks(plant_file)
        html = generate_plant_html(plant)
        if preserved:
            html = html.replace("</main>", preserved + "</main>", 1)
        
        # Write file
        with open(plant_file, 'w') as f:
            f.write(html)
        
        created += 1
        print(f"  ✓ {plant['name']} ({plant_id})")
    
    print(f"\n✅ Created {created} plant pages")
    
    # Generate sitemap
    print(f"\nGenerating sitemap...")
    sitemap = generate_sitemap(plants)
    with open(SITEMAP_FILE, 'w') as f:
        f.write(sitemap)
    print(f"✅ Sitemap updated with {len(plants)} plant URLs")
    
    print(f"\n🎉 Done! All plant pages generated at {PLANTS_DIR}/")


if __name__ == "__main__":
    main()
