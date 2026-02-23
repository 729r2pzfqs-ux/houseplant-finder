#!/usr/bin/env python3
"""Generate complete Spanish translations for PlantFinder plant pages"""

import json
import os
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent
PLANTS_FILE = BASE_DIR / "data" / "plants.json"
PLANTS_ES_FILE = BASE_DIR / "data" / "plants_es.json"

# Load data
with open(PLANTS_FILE) as f:
    plants = json.load(f)
with open(PLANTS_ES_FILE) as f:
    plants_es = json.load(f)

def generate_plant_page(plant):
    """Generate a complete Spanish plant page"""
    plant_id = plant['id']
    es_data = plants_es.get(plant_id, {})
    
    # Get translated values or fall back to English
    name = es_data.get('name', plant['name'])
    description = es_data.get('description', plant['description'])
    care_tips = es_data.get('care_tips', plant['care_tips'])
    
    # Translate static values
    difficulty_map = {'easy': 'Fácil', 'moderate': 'Moderado', 'hard': 'Difícil'}
    size_map = {'small': 'Pequeño', 'medium': 'Mediano', 'large': 'Grande'}
    growth_map = {'slow': 'Lento', 'moderate': 'Moderado', 'fast': 'Rápido'}
    
    difficulty = difficulty_map.get(plant.get('difficulty', ''), plant.get('difficulty', ''))
    size = size_map.get(plant.get('size', ''), plant.get('size', ''))
    growth_rate = growth_map.get(plant.get('growth_rate', ''), plant.get('growth_rate', ''))
    
    # Light/water/humidity levels
    light_labels = {1: 'Muy Bajo', 2: 'Bajo', 3: 'Medio', 4: 'Alto', 5: 'Muy Alto'}
    water_labels = {1: 'Muy Bajo', 2: 'Bajo', 3: 'Medio', 4: 'Alto', 5: 'Muy Alto'}
    humidity_labels = {1: 'Muy Baja', 2: 'Baja', 3: 'Media', 4: 'Alta', 5: 'Muy Alta'}
    
    light = plant.get('light', 3)
    water = plant.get('water', 3)
    humidity = plant.get('humidity', 3)
    
    # Pet safety
    pet_safe = plant.get('pet_safe', False)
    pet_safe_text = 'Sí ✓' if pet_safe else 'No ✗'
    pet_safe_class = 'text-green-600' if pet_safe else 'text-red-600'
    
    toxic_to = plant.get('toxic_to', [])
    toxic_text = ', '.join(['Gatos' if t == 'cats' else 'Perros' if t == 'dogs' else t for t in toxic_to]) if toxic_to else 'No tóxica'
    
    # Air purifying
    air_purifying = plant.get('air_purifying', False)
    air_text = 'Sí ✓' if air_purifying else 'No'
    
    # Common names
    common_names = plant.get('common_names', [])
    common_names_text = ', '.join(common_names) if common_names else ''
    
    # Origin translation
    origin_map = {
        'West Africa': 'África Occidental',
        'East Africa': 'África Oriental',
        'South Africa': 'Sudáfrica',
        'Central Africa': 'África Central',
        'Central America': 'América Central',
        'South America': 'América del Sur',
        'North America': 'América del Norte',
        'Southeast Asia': 'Sudeste Asiático',
        'East Asia': 'Asia Oriental',
        'Asia': 'Asia',
        'China': 'China',
        'Japan': 'Japón',
        'India': 'India',
        'Madagascar': 'Madagascar',
        'Mexico': 'México',
        'Brazil': 'Brasil',
        'Caribbean': 'Caribe',
        'Australia': 'Australia',
        'Mediterranean': 'Mediterráneo',
        'Tropical regions': 'Regiones tropicales',
        'Tropical Africa': 'África Tropical',
        'Tropical Asia': 'Asia Tropical',
        'Hybrid': 'Híbrido',
        'Cultivar': 'Cultivar'
    }
    raw_origin = plant.get('origin', 'Desconocido')
    origin = origin_map.get(raw_origin, raw_origin)
    # Handle compound origins like "South America (cultivar)"
    for eng, esp in origin_map.items():
        origin = origin.replace(eng, esp)
    
    # Category
    category_map = {
        'foliage': 'Follaje',
        'succulent': 'Suculenta', 
        'flowering': 'Floración',
        'palm': 'Palmera',
        'fern': 'Helecho',
        'cactus': 'Cactus'
    }
    category = category_map.get(plant.get('category', ''), plant.get('category', ''))
    
    # Generate HTML
    html = f'''<!DOCTYPE html>
<html lang="es">
<head>
    <meta name="google-site-verification" content="_6B659H6pJiEc-n-JpbJOzbFOC9-IVr9OAmN5TTVh74">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} - Guía de Cuidado | PlantFinder</title>
    <meta name="description" content="{description[:155]}...">
    <link rel="canonical" href="https://plantfinder.org/es/plants/{plant_id}/">
    <link rel="alternate" hreflang="en" href="https://plantfinder.org/plants/{plant_id}/">
    <link rel="alternate" hreflang="es" href="https://plantfinder.org/es/plants/{plant_id}/">
    <link rel="alternate" hreflang="de" href="https://plantfinder.org/de/plants/{plant_id}/">
    <link rel="alternate" hreflang="x-default" href="https://plantfinder.org/plants/{plant_id}/">
    <link rel="icon" href="/favicon.svg" type="image/svg+xml">
    <script src="https://cdn.tailwindcss.com"></script>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-J2JW25BZPF"></script>
    <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag("js",new Date());gtag("config","G-J2JW25BZPF");</script>
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Article",
      "headline": "{name} - Guía de Cuidado",
      "description": "{description[:200]}",
      "image": "https://plantfinder.org/images/plants/{plant_id}.webp"
    }}
    </script>
</head>
<body class="bg-slate-50 text-slate-800">
    <!-- Header -->
    <header class="bg-white shadow-sm sticky top-0 z-40">
        <nav class="max-w-6xl mx-auto px-4 py-4 flex items-center justify-between">
            <a href="/es/" class="flex items-center gap-2 text-xl font-bold text-emerald-600">
                <svg class="w-8 h-8" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg>
                PlantFinder
            </a>
            <div class="flex items-center gap-4 md:gap-6">
                <a href="/es/search/" class="text-slate-600 hover:text-emerald-600">Buscar</a>
                <a href="/es/quiz/" class="text-slate-600 hover:text-emerald-600">Quiz</a>
                <a href="/es/compare/" class="text-slate-600 hover:text-emerald-600">Comparar</a>
                <!-- Language selector -->
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
        </nav>
    </header>

    <main class="max-w-4xl mx-auto px-4 py-8">
        <!-- Breadcrumb -->
        <nav class="text-sm mb-6">
            <a href="/es/" class="text-emerald-600 hover:underline">Inicio</a>
            <span class="mx-2 text-slate-400">/</span>
            <a href="/es/search/" class="text-emerald-600 hover:underline">Plantas</a>
            <span class="mx-2 text-slate-400">/</span>
            <span class="text-slate-600">{name}</span>
        </nav>

        <div class="bg-white rounded-2xl shadow-lg overflow-hidden">
            <!-- Hero Section -->
            <div class="md:flex">
                <div class="md:w-1/2 p-6">
                    <img src="/images/plants/{plant_id}.webp" 
                         alt="{name}" 
                         class="w-full h-80 object-cover rounded-xl"
                         onerror="this.src='data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 400 300%22><rect fill=%22%2310b981%22 width=%22400%22 height=%22300%22/><text x=%22200%22 y=%22150%22 text-anchor=%22middle%22 fill=%22white%22 font-size=%2248%22>🌿</text></svg>'">
                </div>
                <div class="md:w-1/2 p-6">
                    <div class="flex items-center gap-2 mb-2">
                        <span class="px-3 py-1 bg-emerald-100 text-emerald-700 text-sm rounded-full">{category}</span>
                        {f'<span class="px-3 py-1 bg-green-100 text-green-700 text-sm rounded-full">Segura para mascotas</span>' if pet_safe else ''}
                    </div>
                    <h1 class="text-3xl font-bold text-slate-800 mb-2">{name}</h1>
                    {f'<p class="text-slate-500 mb-4">También conocida como: {common_names_text}</p>' if common_names_text else ''}
                    <p class="text-slate-600 mb-6">{description}</p>
                    
                    <div class="grid grid-cols-2 gap-4">
                        <div class="bg-slate-50 rounded-lg p-3">
                            <div class="text-sm text-slate-500">Dificultad</div>
                            <div class="font-semibold text-slate-800">{difficulty}</div>
                        </div>
                        <div class="bg-slate-50 rounded-lg p-3">
                            <div class="text-sm text-slate-500">Tamaño</div>
                            <div class="font-semibold text-slate-800">{size}</div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Care Requirements -->
            <div class="border-t border-slate-100 p-6">
                <h2 class="text-xl font-bold text-slate-800 mb-4">Requisitos de Cuidado</h2>
                <div class="grid md:grid-cols-3 gap-6">
                    <!-- Light -->
                    <div class="bg-amber-50 rounded-xl p-4">
                        <div class="flex items-center gap-2 mb-3">
                            <span class="text-2xl">☀️</span>
                            <span class="font-semibold text-slate-800">Luz</span>
                        </div>
                        <div class="flex gap-1 mb-2">
                            {''.join([f'<div class="w-6 h-2 rounded-full {"bg-amber-400" if i < light else "bg-slate-200"}"></div>' for i in range(5)])}
                        </div>
                        <div class="text-sm text-slate-600">{light_labels.get(light, 'Medio')}</div>
                    </div>
                    
                    <!-- Water -->
                    <div class="bg-blue-50 rounded-xl p-4">
                        <div class="flex items-center gap-2 mb-3">
                            <span class="text-2xl">💧</span>
                            <span class="font-semibold text-slate-800">Agua</span>
                        </div>
                        <div class="flex gap-1 mb-2">
                            {''.join([f'<div class="w-6 h-2 rounded-full {"bg-blue-400" if i < water else "bg-slate-200"}"></div>' for i in range(5)])}
                        </div>
                        <div class="text-sm text-slate-600">{water_labels.get(water, 'Medio')}</div>
                    </div>
                    
                    <!-- Humidity -->
                    <div class="bg-teal-50 rounded-xl p-4">
                        <div class="flex items-center gap-2 mb-3">
                            <span class="text-2xl">💨</span>
                            <span class="font-semibold text-slate-800">Humedad</span>
                        </div>
                        <div class="flex gap-1 mb-2">
                            {''.join([f'<div class="w-6 h-2 rounded-full {"bg-teal-400" if i < humidity else "bg-slate-200"}"></div>' for i in range(5)])}
                        </div>
                        <div class="text-sm text-slate-600">{humidity_labels.get(humidity, 'Media')}</div>
                    </div>
                </div>
            </div>

            <!-- Care Tips -->
            <div class="border-t border-slate-100 p-6">
                <h2 class="text-xl font-bold text-slate-800 mb-4">Consejos de Cuidado</h2>
                <div class="bg-emerald-50 rounded-xl p-4">
                    <p class="text-slate-700">{care_tips}</p>
                </div>
            </div>

            <!-- Additional Info -->
            <div class="border-t border-slate-100 p-6">
                <h2 class="text-xl font-bold text-slate-800 mb-4">Información Adicional</h2>
                <div class="grid md:grid-cols-2 gap-4">
                    <div class="flex justify-between py-2 border-b border-slate-100">
                        <span class="text-slate-500">Segura para mascotas</span>
                        <span class="{pet_safe_class} font-medium">{pet_safe_text}</span>
                    </div>
                    <div class="flex justify-between py-2 border-b border-slate-100">
                        <span class="text-slate-500">Tóxica para</span>
                        <span class="text-slate-800">{toxic_text}</span>
                    </div>
                    <div class="flex justify-between py-2 border-b border-slate-100">
                        <span class="text-slate-500">Purificadora de aire</span>
                        <span class="text-slate-800">{air_text}</span>
                    </div>
                    <div class="flex justify-between py-2 border-b border-slate-100">
                        <span class="text-slate-500">Velocidad de crecimiento</span>
                        <span class="text-slate-800">{growth_rate}</span>
                    </div>
                    <div class="flex justify-between py-2 border-b border-slate-100">
                        <span class="text-slate-500">Origen</span>
                        <span class="text-slate-800">{origin}</span>
                    </div>
                </div>
            </div>
        </div>

        <!-- Back to Search -->
        <div class="mt-8 text-center">
            <a href="/es/search/" class="inline-flex items-center gap-2 text-emerald-600 hover:text-emerald-700 font-medium">
                ← Volver a la búsqueda
            </a>
        </div>
    </main>

    <!-- Footer -->
    <footer class="bg-slate-800 text-slate-300 py-8 mt-12">
        <div class="max-w-6xl mx-auto px-4 text-center">
            <p class="text-sm">© 2025 PlantFinder. Tu guía para encontrar y cuidar plantas de interior perfectas.</p>
        </div>
    </footer>
</body>
</html>'''
    
    return html

def main():
    print("Generating complete Spanish plant pages...\\n")
    
    # Create es/plants directory
    es_plants_dir = BASE_DIR / "es" / "plants"
    es_plants_dir.mkdir(parents=True, exist_ok=True)
    
    count = 0
    for plant in plants:
        plant_id = plant['id']
        plant_dir = es_plants_dir / plant_id
        plant_dir.mkdir(exist_ok=True)
        
        html = generate_plant_page(plant)
        
        with open(plant_dir / "index.html", "w") as f:
            f.write(html)
        
        count += 1
        if count % 20 == 0:
            print(f"  Generated {count} pages...")
    
    print(f"\\n✅ Generated {count} Spanish plant pages")

if __name__ == "__main__":
    main()
