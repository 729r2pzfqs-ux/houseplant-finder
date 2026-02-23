#!/usr/bin/env python3
"""Generate all Spanish plant pages for PlantFinder"""

import json
import os
from datetime import datetime

# Configuration
BASE_DIR = os.path.expanduser("~/clawd/houseplant-finder")
PLANTS_DIR = os.path.join(BASE_DIR, "es/plants")
DATA_FILE = os.path.join(BASE_DIR, "data/plants.json")
TRANSLATIONS_FILE = os.path.join(BASE_DIR, "data/plants_es.json")
BASE_URL = "https://plantfinder.org/es"
GA_ID = "G-J2JW25BZPF"

# Size to height mapping
size_heights = {
    "small": "15-30 cm",
    "medium": "30-90 cm", 
    "large": "90-180+ cm"
}

size_labels = {
    "small": "Pequeña",
    "medium": "Mediana",
    "large": "Grande"
}

growth_labels = {
    "slow": "Lento",
    "moderate": "Moderado",
    "fast": "Rápido"
}

def get_light_label(level):
    labels = {1: "Muy Bajo", 2: "Bajo", 3: "Medio", 4: "Brillante Indirecto", 5: "Sol Directo"}
    return labels.get(level, "Medio")

def get_water_label(level):
    labels = {1: "Muy Bajo", 2: "Bajo", 3: "Moderado", 4: "Frecuente", 5: "Constante"}
    return labels.get(level, "Moderado")

def get_humidity_label(level):
    labels = {1: "Muy Baja", 2: "Baja", 3: "Media", 4: "Alta", 5: "Muy Alta"}
    return labels.get(level, "Media")

def get_difficulty_badge(difficulty):
    colors = {
        "easy": ("emerald", "Fácil"),
        "medium": ("amber", "Moderado"),
        "hard": ("rose", "Experto")
    }
    color, text = colors.get(difficulty, ("slate", difficulty.title()))
    return f'<span class="bg-{color}-100 text-{color}-700 px-3 py-1 rounded-full text-sm font-medium">{text}</span>'

def get_growth_rate_value(rate):
    values = {"slow": 2, "moderate": 3, "fast": 5}
    return values.get(rate, 3)

def generate_plant_html(plant):
    plant_id = plant["id"]
    name = plant.get("name_es", plant["name"])
    common_names = plant.get("common_names", [])
    common_names_str = ", ".join(common_names) if common_names else ""
    
    light = plant.get("light", 3)
    water = plant.get("water", 3)
    humidity = plant.get("humidity", 3)
    difficulty = plant.get("difficulty", "medium")
    pet_safe = plant.get("pet_safe", False)
    toxic_to = plant.get("toxic_to", [])
    size = plant.get("size", "medium")
    size_label = size_labels.get(size, "Mediana")
    size_height = size_heights.get(size, "30-90 cm")
    growth_rate = plant.get("growth_rate", "moderate")
    growth_label = growth_labels.get(growth_rate, "Moderado")
    air_purifying = plant.get("air_purifying", False)
    description = plant.get("description", "")
    care_tips = plant.get("care_tips", "")
    origin = plant.get("origin", "")
    category = plant.get("category", "foliage")
    
    # Category translations
    category_labels = {
        "foliage": "Follaje",
        "trailing": "Colgante",
        "succulent": "Suculenta",
        "cactus": "Cactus",
        "palm": "Palma",
        "fern": "Helecho",
        "flowering": "Floración"
    }
    category_label = category_labels.get(category, category.title())
    
    maintenance_map = {"easy": 2, "medium": 3, "hard": 4}
    maintenance = maintenance_map.get(difficulty, 3)
    
    # Build badges
    badges = [get_difficulty_badge(difficulty)]
    badges.append(f'<span class="bg-teal-100 text-teal-700 px-3 py-1 rounded-full text-sm font-medium">{category_label}</span>')
    if not pet_safe:
        badges.append('<span class="bg-rose-100 text-rose-700 px-3 py-1 rounded-full text-sm font-medium">⚠️ Tóxica para Mascotas</span>')
    else:
        badges.append('<span class="bg-green-100 text-green-700 px-3 py-1 rounded-full text-sm font-medium">✓ Segura para Mascotas</span>')
    
    badges_html = "\n                        ".join(badges)
    
    # Pet warning section
    pet_warning_html = ""
    if not pet_safe and toxic_to:
        toxic_pets = {"cats": "gatos", "dogs": "perros"}
        pets_es = [toxic_pets.get(p, p) for p in toxic_to]
        pets_str = " y ".join(pets_es)
        pet_warning_html = f'''
        <div class="bg-rose-50 border border-rose-200 rounded-2xl p-6 mb-8">
            <div class="flex items-start gap-4">
                <div class="w-12 h-12 bg-rose-100 rounded-xl flex items-center justify-center flex-shrink-0">
                    <i data-lucide="alert-triangle" class="w-6 h-6 text-rose-600"></i>
                </div>
                <div>
                    <h3 class="font-bold text-rose-800 mb-1">⚠️ Tóxica para Mascotas</h3>
                    <p class="text-rose-700">{name} contiene compuestos tóxicos para {pets_str} si se ingiere. Mantén esta planta fuera del alcance de las mascotas, o considera una <a href="/es/search/?pet_safe=true" class="underline hover:no-underline">alternativa segura para mascotas</a>.</p>
                </div>
            </div>
        </div>
'''
    elif pet_safe:
        pet_warning_html = f'''
        <div class="bg-green-50 border border-green-200 rounded-2xl p-6 mb-8">
            <div class="flex items-start gap-4">
                <div class="w-12 h-12 bg-green-100 rounded-xl flex items-center justify-center flex-shrink-0">
                    <i data-lucide="heart" class="w-6 h-6 text-green-600"></i>
                </div>
                <div>
                    <h3 class="font-bold text-green-800 mb-1">✓ Segura para Mascotas</h3>
                    <p class="text-green-700">{name} no es tóxica y es segura para hogares con gatos y perros.</p>
                </div>
            </div>
        </div>
'''
    
    # Info badges
    info_badges = []
    info_badges.append(f'''<div class="flex items-center gap-2 px-4 py-2 bg-slate-100 rounded-xl">
                            <i data-lucide="ruler" class="w-4 h-4 text-slate-600"></i>
                            <span class="text-sm font-medium text-slate-700">{size_label}</span>
                        </div>''')
    info_badges.append(f'''<div class="flex items-center gap-2 px-4 py-2 bg-slate-100 rounded-xl">
                            <i data-lucide="trending-up" class="w-4 h-4 text-slate-600"></i>
                            <span class="text-sm font-medium text-slate-700">Crecimiento {growth_label}</span>
                        </div>''')
    if air_purifying:
        info_badges.append('''<div class="flex items-center gap-2 px-4 py-2 bg-emerald-100 rounded-xl">
                            <i data-lucide="wind" class="w-4 h-4 text-emerald-600"></i>
                            <span class="text-sm font-medium text-emerald-700">Purifica el Aire</span>
                        </div>''')
    
    info_badges_html = "\n                        ".join(info_badges)
    
    # Best for / Not ideal for
    best_for = []
    not_ideal = []
    
    if light <= 2:
        best_for.append("Habitaciones con poca luz y oficinas")
    elif light >= 4:
        best_for.append("Habitaciones luminosas con buena luz natural")
    else:
        best_for.append("Salas de estar con luz indirecta")
    
    if difficulty == "easy":
        best_for.append("Principiantes y personas ocupadas")
    elif difficulty == "hard":
        not_ideal.append("Principiantes o quienes tienen poco tiempo")
    
    if pet_safe:
        best_for.append("Hogares con gatos y perros")
    else:
        not_ideal.append("Hogares con mascotas curiosas")
    
    if water <= 2:
        best_for.append("Quienes olvidan regar")
    elif water >= 4:
        not_ideal.append("Viajeros frecuentes")
    
    if size == "large":
        best_for.append("Espacios amplios como declaración")
        not_ideal.append("Apartamentos pequeños")
    elif size == "small":
        best_for.append("Escritorios y estantes")
    
    if humidity >= 4:
        best_for.append("Baños o habitaciones con humidificadores")
        not_ideal.append("Climas muy secos")
    
    if air_purifying:
        best_for.append("Mejorar la calidad del aire interior")
    
    best_for_html = "\n                        ".join([f'<li class="flex items-start gap-2"><i data-lucide="check" class="w-5 h-5 text-green-500 flex-shrink-0 mt-0.5"></i><span>{item}</span></li>' for item in best_for[:4]])
    not_ideal_html = "\n                        ".join([f'<li class="flex items-start gap-2"><i data-lucide="x" class="w-5 h-5 text-red-500 flex-shrink-0 mt-0.5"></i><span>{item}</span></li>' for item in not_ideal[:3]])
    
    growth_rate_val = get_growth_rate_value(growth_rate)
    air_purifying_val = 4 if air_purifying else 1

    html = f'''<!DOCTYPE html>
<html lang="es">
<head>
    <script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>
    <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag("js",new Date());gtag("config","{GA_ID}");</script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} - Guía de Cuidado | PlantFinder</title>
    <meta name="description" content="Guía completa de cuidado para {name}. Aprende sobre luz, agua, humedad, y cómo mantener tu {name} saludable.">
    <link rel="canonical" href="{BASE_URL}/plants/{plant_id}/">
    <link rel="alternate" hreflang="en" href="https://plantfinder.org/plants/{plant_id}/">
    <link rel="alternate" hreflang="es" href="https://plantfinder.org/es/plants/{plant_id}/">
    <link rel="alternate" hreflang="de" href="https://plantfinder.org/de/plants/{plant_id}/">
    <meta property="og:title" content="{name} - Guía de Cuidado | PlantFinder">
    <meta property="og:description" content="{description}">
    <meta property="og:url" content="{BASE_URL}/plants/{plant_id}/">
    <meta property="og:type" content="article">
    <link rel="icon" href="/favicon.svg" type="image/svg+xml">
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <script>tailwind.config={{theme:{{extend:{{fontFamily:{{sans:['Plus Jakarta Sans','sans-serif']}}}}}}}}</script>
    <style>
        .rating-bar {{ height: 8px; background: #e2e8f0; border-radius: 4px; overflow: hidden; }}
        .rating-bar::after {{ content: ''; display: block; height: 100%; border-radius: 4px; background: linear-gradient(90deg, #10b981, #14b8a6); }}
        .rating-1::after {{ width: 20%; }} .rating-2::after {{ width: 40%; }} .rating-3::after {{ width: 60%; }} .rating-4::after {{ width: 80%; }} .rating-5::after {{ width: 100%; }}
    </style>
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": "{name}: Guía Completa de Cuidado",
        "description": "{description}",
        "author": {{"@type": "Organization", "name": "PlantFinder"}},
        "publisher": {{"@type": "Organization", "name": "PlantFinder"}}
    }}
    </script>
</head>
<body class="bg-slate-50 text-slate-800">
    <nav class="bg-white/80 backdrop-blur-md border-b border-slate-200 sticky top-0 z-50">
        <div class="max-w-6xl mx-auto px-4 py-4">
            <div class="flex items-center justify-between">
                <a href="/es/" class="flex items-center gap-2">
                    <svg class="w-7 h-7 text-emerald-600" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M7 20h10"/><path d="M10 20c5.5-2.5.8-6.4 3-10"/>
                        <path d="M9.5 9.4c1.1.8 1.8 2.2 2.3 3.7-2 .4-3.5.4-4.8-.3-1.2-.6-2.3-1.9-3-4.2 2.8-.5 4.4 0 5.5.8z"/>
                        <path d="M14.1 6a7 7 0 0 0-1.1 4c1.9-.1 3.3-.6 4.3-1.4 1-1 1.6-2.3 1.7-4.6-2.7.1-4 1-4.9 2z"/>
                    </svg>
                    <span class="font-bold text-xl bg-gradient-to-r from-emerald-600 to-teal-600 bg-clip-text text-transparent">PlantFinder</span>
                </a>
                <div class="flex items-center gap-4 md:gap-6">
                    <a href="/es/search/" class="text-slate-600 hover:text-emerald-700 font-medium hidden sm:block">Buscar</a>
                    <a href="/es/quiz/" class="text-slate-600 hover:text-emerald-700 font-medium hidden sm:block">Quiz</a>
                    <a href="/es/compare/" class="text-slate-600 hover:text-emerald-700 font-medium hidden sm:block">Comparar</a>
                    <div class="relative group">
                        <button class="flex items-center gap-1 text-slate-600 hover:text-emerald-700 py-2">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
                            <span>ES</span>
                        </button>
                        <div class="absolute right-0 top-full bg-white border border-slate-200 rounded-xl shadow-xl hidden group-hover:block min-w-[140px] py-2 z-50">
                            <a href="/plants/{plant_id}/" class="block px-4 py-2 hover:bg-slate-100 text-slate-600">English</a>
                            <a href="/es/plants/{plant_id}/" class="block px-4 py-2 hover:bg-slate-100 font-semibold text-emerald-700">Español</a>
                            <a href="/de/plants/{plant_id}/" class="block px-4 py-2 hover:bg-slate-100 text-slate-600">Deutsch</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </nav>

    <main class="max-w-6xl mx-auto px-4 py-8">
        <nav class="text-sm text-slate-500 mb-6">
            <a href="/es/" class="hover:text-emerald-600">Inicio</a>
            <span class="mx-2">/</span>
            <a href="/es/search/" class="hover:text-emerald-600">Plantas</a>
            <span class="mx-2">/</span>
            <span class="text-slate-700">{name}</span>
        </nav>

        <div class="bg-white rounded-2xl shadow-sm border border-slate-200 overflow-hidden mb-8">
            <div class="md:flex">
                <div class="md:w-2/5">
                    <div class="aspect-[4/5] bg-gradient-to-br from-emerald-100 via-teal-100 to-lime-100 relative overflow-hidden flex items-center justify-center p-8">
                        <img src="/images/plants/{plant_id}.webp" alt="{name}" class="w-full h-full object-contain" onerror="this.onerror=null; this.src=''; this.parentElement.innerHTML='<span class=\\'text-9xl\\'>🪴</span>'">
                    </div>
                </div>
                <div class="md:w-3/5 p-6 md:p-8">
                    <div class="flex flex-wrap gap-2 mb-4">
                        {badges_html}
                    </div>
                    <h1 class="text-3xl md:text-4xl font-bold text-slate-900 mb-2">{name}</h1>
                    {f'<p class="text-slate-500 mb-4">También conocida como: {common_names_str}</p>' if common_names_str else '<div class="mb-4"></div>'}
                    
                    <div class="flex flex-wrap gap-2 mb-6">
                        {info_badges_html}
                    </div>
                    
                    <div class="grid grid-cols-2 gap-4">
                        <div class="flex items-center gap-3 p-3 bg-slate-50 rounded-xl">
                            <i data-lucide="sun" class="w-6 h-6 text-amber-500"></i>
                            <div>
                                <p class="text-xs text-slate-500">Luz</p>
                                <p class="font-semibold text-slate-700">{get_light_label(light)}</p>
                            </div>
                        </div>
                        <div class="flex items-center gap-3 p-3 bg-slate-50 rounded-xl">
                            <i data-lucide="droplets" class="w-6 h-6 text-blue-500"></i>
                            <div>
                                <p class="text-xs text-slate-500">Agua</p>
                                <p class="font-semibold text-slate-700">{get_water_label(water)}</p>
                            </div>
                        </div>
                        <div class="flex items-center gap-3 p-3 bg-slate-50 rounded-xl">
                            <i data-lucide="cloud" class="w-6 h-6 text-cyan-500"></i>
                            <div>
                                <p class="text-xs text-slate-500">Humedad</p>
                                <p class="font-semibold text-slate-700">{get_humidity_label(humidity)}</p>
                            </div>
                        </div>
                        <div class="flex items-center gap-3 p-3 bg-slate-50 rounded-xl">
                            <i data-lucide="ruler" class="w-6 h-6 text-emerald-500"></i>
                            <div>
                                <p class="text-xs text-slate-500">Tamaño</p>
                                <p class="font-semibold text-slate-700">{size_label}</p>
                                <p class="text-xs text-slate-500 mt-1">{size_height}</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

{pet_warning_html}
        <section class="bg-white rounded-2xl shadow-sm border border-slate-200 p-6 md:p-8 mb-8">
            <h2 class="text-xl font-bold text-slate-900 mb-6">Requisitos de Cuidado</h2>
            <div class="grid md:grid-cols-2 gap-x-12 gap-y-4">
                <div>
                    <div class="flex justify-between mb-2"><span class="text-slate-600">Necesidades de Luz</span><span class="font-medium">{light}/5</span></div>
                    <div class="rating-bar rating-{light}"></div>
                </div>
                <div>
                    <div class="flex justify-between mb-2"><span class="text-slate-600">Necesidades de Agua</span><span class="font-medium">{water}/5</span></div>
                    <div class="rating-bar rating-{water}"></div>
                </div>
                <div>
                    <div class="flex justify-between mb-2"><span class="text-slate-600">Necesidades de Humedad</span><span class="font-medium">{humidity}/5</span></div>
                    <div class="rating-bar rating-{humidity}"></div>
                </div>
                <div>
                    <div class="flex justify-between mb-2"><span class="text-slate-600">Mantenimiento</span><span class="font-medium">{maintenance}/5</span></div>
                    <div class="rating-bar rating-{maintenance}"></div>
                </div>
                <div>
                    <div class="flex justify-between mb-2"><span class="text-slate-600">Velocidad de Crecimiento</span><span class="font-medium">{growth_rate_val}/5</span></div>
                    <div class="rating-bar rating-{growth_rate_val}"></div>
                </div>
                <div>
                    <div class="flex justify-between mb-2"><span class="text-slate-600">Purificación de Aire</span><span class="font-medium">{air_purifying_val}/5</span></div>
                    <div class="rating-bar rating-{air_purifying_val}"></div>
                </div>
            </div>
        </section>

        <section class="bg-white rounded-2xl shadow-sm border border-slate-200 p-6 md:p-8 mb-8">
            <h2 class="text-xl font-bold text-slate-900 mb-4">Acerca de {name}</h2>
            <p class="text-slate-600 leading-relaxed mb-4">{description}</p>
            {f'<p class="text-slate-600 leading-relaxed"><strong>Origen:</strong> {origin}</p>' if origin else ''}
        </section>

        <section class="bg-white rounded-2xl shadow-sm border border-slate-200 p-6 md:p-8 mb-8">
            <h2 class="text-xl font-bold text-slate-900 mb-4">Consejos de Cuidado</h2>
            <div class="bg-emerald-50 rounded-xl p-5">
                <div class="flex items-start gap-3">
                    <i data-lucide="lightbulb" class="w-6 h-6 text-emerald-600 mt-0.5"></i>
                    <p class="text-slate-700">{care_tips}</p>
                </div>
            </div>
        </section>

        <section class="bg-gradient-to-br from-emerald-50 via-teal-50 to-lime-50 rounded-2xl p-6 md:p-8 mb-8">
            <h2 class="text-xl font-bold text-slate-900 mb-6">¿Es Esta Planta Para Ti?</h2>
            <div class="grid md:grid-cols-2 gap-6 mb-6">
                <div class="bg-white rounded-xl p-5 shadow-sm">
                    <h3 class="font-semibold text-green-700 mb-3 flex items-center gap-2">
                        <i data-lucide="check-circle" class="w-5 h-5"></i>
                        Ideal Para
                    </h3>
                    <ul class="space-y-2 text-slate-600">
                        {best_for_html}
                    </ul>
                </div>
                <div class="bg-white rounded-xl p-5 shadow-sm">
                    <h3 class="font-semibold text-red-700 mb-3 flex items-center gap-2">
                        <i data-lucide="x-circle" class="w-5 h-5"></i>
                        No Ideal Para
                    </h3>
                    <ul class="space-y-2 text-slate-600">
                        {not_ideal_html if not_ideal_html else '<li class="text-slate-400">¡Sin preocupaciones importantes!</li>'}
                    </ul>
                </div>
            </div>
            
            <div class="flex flex-wrap gap-3">
                <a href="/es/compare/" class="inline-flex items-center gap-2 bg-white text-slate-700 border border-slate-200 px-5 py-2.5 rounded-xl font-semibold hover:border-slate-300 hover:shadow-md transition">
                    <i data-lucide="scale" class="w-4 h-4"></i>
                    Comparar con otras plantas
                </a>
                {f'<a href="/es/search/?pet_safe=true" class="inline-flex items-center gap-2 bg-emerald-600 text-white px-5 py-2.5 rounded-xl font-semibold hover:bg-emerald-700 transition"><i data-lucide="paw-print" class="w-4 h-4"></i>Buscar alternativas seguras</a>' if not pet_safe else ''}
            </div>
        </section>
    </main>

    <footer class="bg-slate-900 text-slate-400 py-12">
        <div class="max-w-6xl mx-auto px-4">
            <div class="flex flex-col md:flex-row justify-between items-center gap-4">
                <div class="flex items-center gap-2">
                    <svg class="w-6 h-6 text-emerald-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M7 20h10"/><path d="M10 20c5.5-2.5.8-6.4 3-10"/><path d="M9.5 9.4c1.1.8 1.8 2.2 2.3 3.7-2 .4-3.5.4-4.8-.3-1.2-.6-2.3-1.9-3-4.2 2.8-.5 4.4 0 5.5.8z"/><path d="M14.1 6a7 7 0 0 0-1.1 4c1.9-.1 3.3-.6 4.3-1.4 1-1 1.6-2.3 1.7-4.6-2.7.1-4 1-4.9 2z"/></svg>
                    <span class="font-bold text-white">PlantFinder</span>
                </div>
                <div class="flex gap-6 text-sm">
                    <a href="/es/search/" class="hover:text-white">Buscar</a>
                    <a href="/es/quiz/" class="hover:text-white">Quiz</a>
                    <a href="/es/compare/" class="hover:text-white">Comparar</a>
                    <a href="/es/articles/" class="hover:text-white">Guías</a>
                    <a href="/es/about/" class="hover:text-white">Acerca de</a>
                </div>
                <p class="text-sm">&copy; 2026 PlantFinder</p>
            </div>
        </div>
    </footer>
    
    <script>lucide.createIcons();</script>
</body>
</html>'''
    
    return html


def main():
    print(f"Loading plant data from {DATA_FILE}...")
    with open(DATA_FILE, 'r') as f:
        plants = json.load(f)
    
    with open(TRANSLATIONS_FILE, 'r') as f:
        translations = json.load(f)
    
    for plant in plants:
        plant_id = plant["id"]
        if plant_id in translations:
            trans = translations[plant_id]
            if "name" in trans:
                plant["name_es"] = trans["name"]
            if "description" in trans:
                plant["description"] = trans["description"]
            if "care_tips" in trans:
                plant["care_tips"] = trans["care_tips"]
    
    print(f"Found {len(plants)} plants with Spanish translations")
    
    created = 0
    for plant in plants:
        plant_id = plant["id"]
        plant_dir = os.path.join(PLANTS_DIR, plant_id)
        plant_file = os.path.join(plant_dir, "index.html")
        
        os.makedirs(plant_dir, exist_ok=True)
        html = generate_plant_html(plant)
        
        with open(plant_file, 'w') as f:
            f.write(html)
        
        created += 1
    
    print(f"\n✅ Created {created} Spanish plant pages")


if __name__ == "__main__":
    main()
