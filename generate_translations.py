#!/usr/bin/env python3
"""Generate Spanish and German translations for PlantFinder"""

import json
import os
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent
PLANTS_FILE = BASE_DIR / "data" / "plants.json"
TRANS_FILE = BASE_DIR / "translations.json"

# Load data
with open(PLANTS_FILE) as f:
    plants = json.load(f)
with open(TRANS_FILE) as f:
    translations = json.load(f)

# Plant name translations (common plants)
PLANT_NAMES = {
    "es": {
        "Monstera Deliciosa": "Monstera Deliciosa",
        "Golden Pothos": "Pothos Dorado",
        "Snake Plant": "Lengua de Suegra",
        "Peace Lily": "Lirio de la Paz",
        "Fiddle Leaf Fig": "Ficus Lira",
        "Rubber Plant": "Árbol del Caucho",
        "ZZ Plant": "Planta ZZ",
        "Spider Plant": "Planta Araña",
        "Boston Fern": "Helecho de Boston",
        "Aloe Vera": "Aloe Vera",
        "Jade Plant": "Planta de Jade",
        "Bird of Paradise": "Ave del Paraíso",
        "Chinese Evergreen": "Aglaonema",
        "Prayer Plant": "Planta de la Oración",
        "English Ivy": "Hiedra Inglesa",
        "Dragon Tree": "Drácena Marginata",
        "Ponytail Palm": "Pata de Elefante",
        "Money Tree": "Árbol del Dinero",
        "Lucky Bamboo": "Bambú de la Suerte",
        "Christmas Cactus": "Cactus de Navidad",
        "String of Pearls": "Collar de Perlas",
        "String of Hearts": "Collar de Corazones",
        "String of Bananas": "Collar de Bananas",
        "String of Dolphins": "Collar de Delfines",
        "String of Turtles": "Collar de Tortugas",
        "Cast Iron Plant": "Aspidistra",
        "Nerve Plant": "Fitonia",
        "Polka Dot Plant": "Planta Lunares",
        "African Violet": "Violeta Africana",
        "Moth Orchid": "Orquídea Mariposa",
        "Sweetheart Plant": "Planta Corazón",
        "Never Never Plant": "Ctenanthe",
        "Arrowhead Plant": "Singonio",
        "Mini Monstera": "Mini Monstera",
    },
    "de": {
        "Monstera Deliciosa": "Monstera Deliciosa",
        "Golden Pothos": "Goldene Efeutute",
        "Snake Plant": "Bogenhanf",
        "Peace Lily": "Einblatt",
        "Fiddle Leaf Fig": "Geigenfeige",
        "Rubber Plant": "Gummibaum",
        "ZZ Plant": "Zamioculcas",
        "Spider Plant": "Grünlilie",
        "Boston Fern": "Schwertfarn",
        "Aloe Vera": "Aloe Vera",
        "Jade Plant": "Geldbaum",
        "Bird of Paradise": "Strelitzie",
        "Chinese Evergreen": "Kolbenfaden",
        "Prayer Plant": "Pfeilwurz",
        "English Ivy": "Efeu",
        "Dragon Tree": "Drachenbaum",
        "Ponytail Palm": "Elefantenfuß",
        "Money Tree": "Geldbaum",
        "Lucky Bamboo": "Glücksbambus",
        "Christmas Cactus": "Weihnachtskaktus",
        "String of Pearls": "Erbsenpflanze",
        "String of Hearts": "Leuchterblume",
        "String of Bananas": "Bananenschnur",
        "String of Dolphins": "Delfinpflanze",
        "String of Turtles": "Schildkrötenpflanze",
        "Cast Iron Plant": "Schusterpalme",
        "Nerve Plant": "Fittonie",
        "Polka Dot Plant": "Punktblume",
        "African Violet": "Usambaraveilchen",
        "Moth Orchid": "Schmetterlingsorchidee",
        "Sweetheart Plant": "Herzpflanze",
        "Never Never Plant": "Korbmarante",
        "Arrowhead Plant": "Purpurtute",
        "Mini Monstera": "Mini Monstera",
    }
}

# Description translations
PLANT_DESCRIPTIONS = {
    "es": {
        "easy": "fácil",
        "moderate": "moderado", 
        "hard": "difícil",
        "small": "pequeña",
        "medium": "mediana",
        "large": "grande",
        "slow": "lento",
        "fast": "rápido",
        "foliage": "follaje",
        "succulent": "suculenta",
        "flowering": "floración",
        "palm": "palmera",
        "fern": "helecho",
        "cactus": "cactus",
    },
    "de": {
        "easy": "einfach",
        "moderate": "mittel",
        "hard": "schwer", 
        "small": "klein",
        "medium": "mittel",
        "large": "groß",
        "slow": "langsam",
        "fast": "schnell",
        "foliage": "Blattpflanze",
        "succulent": "Sukkulente",
        "flowering": "Blühpflanze",
        "palm": "Palme",
        "fern": "Farn",
        "cactus": "Kaktus",
    }
}

def get_plant_name(plant, lang):
    """Get translated plant name or return original"""
    return PLANT_NAMES.get(lang, {}).get(plant["name"], plant["name"])

def translate_difficulty(diff, lang):
    return PLANT_DESCRIPTIONS.get(lang, {}).get(diff, diff)

def translate_size(size, lang):
    return PLANT_DESCRIPTIONS.get(lang, {}).get(size, size)

def generate_homepage(lang):
    """Generate translated homepage"""
    t = translations[lang]
    
    # Read English homepage as template
    with open(BASE_DIR / "index.html") as f:
        html = f.read()
    
    # Create language directory
    lang_dir = BASE_DIR / lang
    lang_dir.mkdir(exist_ok=True)
    
    # Simple replacements for key elements
    replacements = {
        '<html lang="en">': f'<html lang="{lang}">',
        'PlantFinder | Quiz, Compare & Find Your Perfect Houseplant': t['site_title'],
        'Find your perfect houseplant with our quiz, compare tool & care guides. 100+ plants rated for light needs, pet safety, difficulty & more.': t['meta_description'],
        'Find Your Perfect Houseplant': t['hero_title'],
        'Discover the ideal plant for your space and lifestyle': t['hero_subtitle'],
        'Take the Quiz': t['hero_cta'],
        'Browse Plants': t['browse_plants'],
        'Search plants...': t['search_placeholder'],
        'Popular Plants': t['popular_plants'],
        'View All': t['view_all'],
        'Pet Safe Plants': t['pet_safe'],
        'Non-toxic plants for your home': t['pet_safe_subtitle'],
        'Easy Care': t['easy_care'],
        'Low Light': t['low_light'],
        'Air Purifying': t['air_purifying'],
        'Tools to Find Your Plant': t['tools_title'],
        'Plant Quiz': t['quiz_title'],
        'Answer a few questions and we\'ll recommend perfect plants for you': t['quiz_desc'],
        'Compare Plants': t['compare_title'],
        'Compare two plants side-by-side to see which suits your needs better': t['compare_desc'],
        'Search Plants': t['search_title'],
        'Filter by light, water, size, pet safety and more': t['search_desc'],
        'Frequently Asked Questions': t['faq_title'],
        'Your guide to finding and caring for the perfect houseplants.': t['footer_desc'],
        'About': t['about'],
        'Contact': t['contact'],
        'Privacy': t['privacy'],
    }
    
    for old, new in replacements.items():
        html = html.replace(old, new)
    
    # Fix URLs for language subdirectory
    html = html.replace('href="/quiz/"', f'href="/{lang}/quiz/"')
    html = html.replace('href="/compare/"', f'href="/{lang}/compare/"')
    html = html.replace('href="/search/"', f'href="/{lang}/search/"')
    html = html.replace('href="/faq/"', f'href="/{lang}/faq/"')
    html = html.replace('href="/about/"', f'href="/{lang}/about/"')
    html = html.replace('href="/plants/', f'href="/{lang}/plants/')
    
    # Update canonical
    html = html.replace('https://houseplantfinder.app/">', f'https://plantfinder.org/{lang}/">')
    html = re.sub(r'<link rel="canonical" href="[^"]+">',
                  f'<link rel="canonical" href="https://plantfinder.org/{lang}/">', html)
    
    # Add hreflang tags
    hreflang = '''
    <link rel="alternate" hreflang="en" href="https://plantfinder.org/">
    <link rel="alternate" hreflang="es" href="https://plantfinder.org/es/">
    <link rel="alternate" hreflang="de" href="https://plantfinder.org/de/">
    <link rel="alternate" hreflang="x-default" href="https://plantfinder.org/">'''
    
    html = html.replace('</head>', f'{hreflang}\n</head>')
    
    # Add language selector before </body>
    lang_selector = f'''
    <div style="position:fixed;bottom:20px;right:20px;z-index:50;">
        <select onchange="window.location.href=this.value" 
                class="bg-white dark:bg-slate-800 border border-slate-300 dark:border-slate-600 rounded-lg px-3 py-2 text-sm shadow-lg"
                aria-label="Select language">
            <option value="/" {"" if lang == "en" else ""}>🇬🇧 English</option>
            <option value="/es/" {"selected" if lang == "es" else ""}>🇪🇸 Español</option>
            <option value="/de/" {"selected" if lang == "de" else ""}>🇩🇪 Deutsch</option>
        </select>
    </div>'''
    
    html = html.replace('</body>', f'{lang_selector}\n</body>')
    
    # Write translated homepage
    with open(lang_dir / "index.html", "w") as f:
        f.write(html)
    
    print(f"  ✓ {lang}/index.html")

def generate_search_page(lang):
    """Generate translated search page"""
    t = translations[lang]
    lang_dir = BASE_DIR / lang / "search"
    lang_dir.mkdir(parents=True, exist_ok=True)
    
    with open(BASE_DIR / "search" / "index.html") as f:
        html = f.read()
    
    # Key translations
    replacements = {
        '<html lang="en">': f'<html lang="{lang}">',
        'Browse Houseplants': 'Explorar Plantas' if lang == 'es' else 'Pflanzen durchsuchen',
        'Search plants...': t['search_placeholder'],
        'Light Level': 'Nivel de Luz' if lang == 'es' else 'Lichtbedarf',
        'Water Needs': 'Necesidad de Agua' if lang == 'es' else 'Wasserbedarf',
        'Difficulty': t['difficulty'],
        'Size': t['size'],
        'Pet Safe': t['pet_safe'],
        'Air Purifying': t['air_purifying'],
        'All': 'Todos' if lang == 'es' else 'Alle',
        'Low': t['low'],
        'Medium': t['medium'] if 'medium' in t else 'Medio' if lang == 'es' else 'Mittel',
        'Bright': t['bright'],
        'Direct Sun': 'Sol Directo' if lang == 'es' else 'Direkte Sonne',
        'Easy': t['easy'],
        'Moderate': t['moderate'],
        'Hard': t['hard'],
        'Small': t['small'],
        'Large': t['large'],
        'Yes': t['yes'],
        'No': t['no'],
        'plants found': 'plantas encontradas' if lang == 'es' else 'Pflanzen gefunden',
        'PlantFinder': 'PlantFinder',
    }
    
    for old, new in replacements.items():
        html = html.replace(old, new)
    
    # Fix URLs
    html = html.replace('href="/"', f'href="/{lang}/"')
    html = html.replace('href="/quiz/"', f'href="/{lang}/quiz/"')
    html = html.replace('href="/compare/"', f'href="/{lang}/compare/"')
    html = html.replace('href="/plants/', f'href="/{lang}/plants/')
    
    # Update canonical
    html = re.sub(r'<link rel="canonical" href="[^"]+">',
                  f'<link rel="canonical" href="https://plantfinder.org/{lang}/search/">', html)
    
    with open(lang_dir / "index.html", "w") as f:
        f.write(html)
    
    print(f"  ✓ {lang}/search/index.html")

def generate_quiz_page(lang):
    """Generate translated quiz page"""
    t = translations[lang]
    lang_dir = BASE_DIR / lang / "quiz"
    lang_dir.mkdir(parents=True, exist_ok=True)
    
    with open(BASE_DIR / "quiz" / "index.html") as f:
        html = f.read()
    
    # Quiz-specific translations
    quiz_trans = {
        'es': {
            'Plant Quiz': 'Quiz de Plantas',
            'Find Your Perfect Plant': 'Encuentra tu Planta Perfecta',
            'Answer a few questions': 'Responde algunas preguntas',
            'How much light does your space get?': '¿Cuánta luz recibe tu espacio?',
            'Low light': 'Poca luz',
            'Medium light': 'Luz media',
            'Bright indirect': 'Luz brillante indirecta',
            'Direct sunlight': 'Luz solar directa',
            'How often do you want to water?': '¿Con qué frecuencia quieres regar?',
            'Rarely': 'Raramente',
            'Weekly': 'Semanalmente',
            'Often': 'Frecuentemente',
            'Do you have pets?': '¿Tienes mascotas?',
            'Yes, need pet-safe': 'Sí, necesito plantas seguras',
            'No pets': 'Sin mascotas',
            'What size plant do you want?': '¿Qué tamaño de planta quieres?',
            'Small': 'Pequeña',
            'Medium': 'Mediana',
            'Large': 'Grande',
            'Any size': 'Cualquier tamaño',
            'Your experience level?': '¿Tu nivel de experiencia?',
            'Beginner': 'Principiante',
            'Intermediate': 'Intermedio',
            'Expert': 'Experto',
            'Next': 'Siguiente',
            'Previous': 'Anterior',
            'See Results': 'Ver Resultados',
            'Your Perfect Plants': 'Tus Plantas Perfectas',
            'Start Over': 'Empezar de Nuevo',
        },
        'de': {
            'Plant Quiz': 'Pflanzen-Quiz',
            'Find Your Perfect Plant': 'Finde deine perfekte Pflanze',
            'Answer a few questions': 'Beantworte ein paar Fragen',
            'How much light does your space get?': 'Wie viel Licht bekommt dein Raum?',
            'Low light': 'Wenig Licht',
            'Medium light': 'Mittleres Licht',
            'Bright indirect': 'Hell indirekt',
            'Direct sunlight': 'Direktes Sonnenlicht',
            'How often do you want to water?': 'Wie oft möchtest du gießen?',
            'Rarely': 'Selten',
            'Weekly': 'Wöchentlich',
            'Often': 'Oft',
            'Do you have pets?': 'Hast du Haustiere?',
            'Yes, need pet-safe': 'Ja, brauche haustiersichere',
            'No pets': 'Keine Haustiere',
            'What size plant do you want?': 'Welche Größe soll die Pflanze haben?',
            'Small': 'Klein',
            'Medium': 'Mittel',
            'Large': 'Groß',
            'Any size': 'Jede Größe',
            'Your experience level?': 'Dein Erfahrungslevel?',
            'Beginner': 'Anfänger',
            'Intermediate': 'Fortgeschritten',
            'Expert': 'Experte',
            'Next': 'Weiter',
            'Previous': 'Zurück',
            'See Results': 'Ergebnisse anzeigen',
            'Your Perfect Plants': 'Deine perfekten Pflanzen',
            'Start Over': 'Neu starten',
        }
    }
    
    replacements = {
        '<html lang="en">': f'<html lang="{lang}">',
    }
    replacements.update(quiz_trans.get(lang, {}))
    
    for old, new in replacements.items():
        html = html.replace(old, new)
    
    # Fix URLs
    html = html.replace('href="/"', f'href="/{lang}/"')
    html = html.replace('href="/plants/', f'href="/{lang}/plants/')
    
    with open(lang_dir / "index.html", "w") as f:
        f.write(html)
    
    print(f"  ✓ {lang}/quiz/index.html")

def generate_compare_page(lang):
    """Generate translated compare page"""
    t = translations[lang]
    lang_dir = BASE_DIR / lang / "compare"
    lang_dir.mkdir(parents=True, exist_ok=True)
    
    with open(BASE_DIR / "compare" / "index.html") as f:
        html = f.read()
    
    compare_trans = {
        'es': {
            'Compare Plants': 'Comparar Plantas',
            'Select two plants to compare': 'Selecciona dos plantas para comparar',
            'Choose a plant': 'Elige una planta',
            'Light': 'Luz',
            'Water': 'Agua',
            'Humidity': 'Humedad',
            'Difficulty': 'Dificultad',
            'Size': 'Tamaño',
            'Pet Safe': 'Segura para Mascotas',
            'Air Purifying': 'Purificadora de Aire',
            'Growth Rate': 'Velocidad de Crecimiento',
            'Popular Comparisons': 'Comparaciones Populares',
        },
        'de': {
            'Compare Plants': 'Pflanzen vergleichen',
            'Select two plants to compare': 'Wähle zwei Pflanzen zum Vergleichen',
            'Choose a plant': 'Pflanze wählen',
            'Light': 'Licht',
            'Water': 'Wasser',
            'Humidity': 'Luftfeuchtigkeit',
            'Difficulty': 'Schwierigkeit',
            'Size': 'Größe',
            'Pet Safe': 'Haustierfreundlich',
            'Air Purifying': 'Luftreinigend',
            'Growth Rate': 'Wachstumsrate',
            'Popular Comparisons': 'Beliebte Vergleiche',
        }
    }
    
    replacements = {
        '<html lang="en">': f'<html lang="{lang}">',
    }
    replacements.update(compare_trans.get(lang, {}))
    
    for old, new in replacements.items():
        html = html.replace(old, new)
    
    # Fix URLs
    html = html.replace('href="/"', f'href="/{lang}/"')
    html = html.replace('href="/plants/', f'href="/{lang}/plants/')
    
    with open(lang_dir / "index.html", "w") as f:
        f.write(html)
    
    print(f"  ✓ {lang}/compare/index.html")

def generate_faq_page(lang):
    """Generate translated FAQ page"""
    lang_dir = BASE_DIR / lang / "faq"
    lang_dir.mkdir(parents=True, exist_ok=True)
    
    with open(BASE_DIR / "faq" / "index.html") as f:
        html = f.read()
    
    faq_trans = {
        'es': {
            'Frequently Asked Questions': 'Preguntas Frecuentes',
            'What are the best houseplants for beginners?': '¿Cuáles son las mejores plantas de interior para principiantes?',
            'Pothos, Snake Plant, ZZ Plant, and Spider Plant are excellent for beginners.': 'Pothos, Lengua de Suegra, Planta ZZ y Planta Araña son excelentes para principiantes.',
            'What houseplants are safe for cats and dogs?': '¿Qué plantas de interior son seguras para gatos y perros?',
            'Spider Plant, Boston Fern, Calathea, Parlor Palm, and Peperomia are all pet-safe.': 'Planta Araña, Helecho de Boston, Calathea, Palmera de Salón y Peperomia son seguras para mascotas.',
            'What are the best low light houseplants?': '¿Cuáles son las mejores plantas de interior para poca luz?',
            'Snake Plant, ZZ Plant, Pothos, Peace Lily, and Chinese Evergreen thrive in low light.': 'Lengua de Suegra, Planta ZZ, Pothos, Lirio de la Paz y Aglaonema prosperan con poca luz.',
            'How often should I water my houseplants?': '¿Con qué frecuencia debo regar mis plantas de interior?',
            'It varies by plant. Most prefer to dry out slightly between waterings.': 'Varía según la planta. La mayoría prefiere secarse ligeramente entre riegos.',
            'What houseplants purify air the best?': '¿Qué plantas de interior purifican mejor el aire?',
            'Snake Plant, Pothos, Peace Lily, Spider Plant, and Chinese Evergreen are excellent air purifiers.': 'Lengua de Suegra, Pothos, Lirio de la Paz, Planta Araña y Aglaonema son excelentes purificadoras de aire.',
        },
        'de': {
            'Frequently Asked Questions': 'Häufig gestellte Fragen',
            'What are the best houseplants for beginners?': 'Was sind die besten Zimmerpflanzen für Anfänger?',
            'Pothos, Snake Plant, ZZ Plant, and Spider Plant are excellent for beginners.': 'Efeutute, Bogenhanf, Zamioculcas und Grünlilie sind hervorragend für Anfänger.',
            'What houseplants are safe for cats and dogs?': 'Welche Zimmerpflanzen sind sicher für Katzen und Hunde?',
            'Spider Plant, Boston Fern, Calathea, Parlor Palm, and Peperomia are all pet-safe.': 'Grünlilie, Schwertfarn, Calathea, Bergpalme und Peperomia sind alle haustiersicher.',
            'What are the best low light houseplants?': 'Was sind die besten Zimmerpflanzen für wenig Licht?',
            'Snake Plant, ZZ Plant, Pothos, Peace Lily, and Chinese Evergreen thrive in low light.': 'Bogenhanf, Zamioculcas, Efeutute, Einblatt und Kolbenfaden gedeihen bei wenig Licht.',
            'How often should I water my houseplants?': 'Wie oft sollte ich meine Zimmerpflanzen gießen?',
            'It varies by plant. Most prefer to dry out slightly between waterings.': 'Es variiert je nach Pflanze. Die meisten trocknen gerne leicht zwischen dem Gießen.',
            'What houseplants purify air the best?': 'Welche Zimmerpflanzen reinigen die Luft am besten?',
            'Snake Plant, Pothos, Peace Lily, Spider Plant, and Chinese Evergreen are excellent air purifiers.': 'Bogenhanf, Efeutute, Einblatt, Grünlilie und Kolbenfaden sind hervorragende Luftreiniger.',
        }
    }
    
    replacements = {
        '<html lang="en">': f'<html lang="{lang}">',
    }
    replacements.update(faq_trans.get(lang, {}))
    
    for old, new in replacements.items():
        html = html.replace(old, new)
    
    # Fix URLs
    html = html.replace('href="/"', f'href="/{lang}/"')
    
    with open(lang_dir / "index.html", "w") as f:
        f.write(html)
    
    print(f"  ✓ {lang}/faq/index.html")

def generate_about_page(lang):
    """Generate translated about page"""
    lang_dir = BASE_DIR / lang / "about"
    lang_dir.mkdir(parents=True, exist_ok=True)
    
    with open(BASE_DIR / "about" / "index.html") as f:
        html = f.read()
    
    about_trans = {
        'es': {
            'About PlantFinder': 'Acerca de PlantFinder',
            'About': 'Acerca de',
            'Our Mission': 'Nuestra Misión',
            'Contact': 'Contacto',
        },
        'de': {
            'About PlantFinder': 'Über PlantFinder',
            'About': 'Über uns',
            'Our Mission': 'Unsere Mission',
            'Contact': 'Kontakt',
        }
    }
    
    replacements = {
        '<html lang="en">': f'<html lang="{lang}">',
    }
    replacements.update(about_trans.get(lang, {}))
    
    for old, new in replacements.items():
        html = html.replace(old, new)
    
    # Fix URLs
    html = html.replace('href="/"', f'href="/{lang}/"')
    
    with open(lang_dir / "index.html", "w") as f:
        f.write(html)
    
    print(f"  ✓ {lang}/about/index.html")

def generate_plant_pages(lang):
    """Generate translated plant detail pages"""
    t = translations[lang]
    
    for plant in plants:
        plant_id = plant['id']
        plant_dir = BASE_DIR / lang / "plants" / plant_id
        plant_dir.mkdir(parents=True, exist_ok=True)
        
        # Read English plant page
        en_page = BASE_DIR / "plants" / plant_id / "index.html"
        if not en_page.exists():
            continue
        
        with open(en_page) as f:
            html = f.read()
        
        # Basic translations
        replacements = {
            '<html lang="en">': f'<html lang="{lang}">',
            'Care Guide': t['care_guide'],
            'Light': t['light'],
            'Water': t['water'],
            'Humidity': t['humidity'],
            'Difficulty': t['difficulty'],
            'Size': t['size'],
            'Toxic to': t['toxic_to'],
            'Origin': t['origin'],
            'Care Tips': t['care_tips'],
            'Common Names': t['common_names'],
            '>Easy<': f'>{t["easy"]}<',
            '>Moderate<': f'>{t["moderate"]}<',
            '>Hard<': f'>{t["hard"]}<',
            '>Small<': f'>{t["small"]}<',
            '>Medium<': f'>{t["medium"]}<',
            '>Large<': f'>{t["large"]}<',
            '>Low<': f'>{t["low"]}<',
            '>High<': f'>{t["high"]}<',
            'cats': t['cats'],
            'dogs': t['dogs'],
        }
        
        for old, new in replacements.items():
            html = html.replace(old, new)
        
        # Fix URLs
        html = html.replace('href="/"', f'href="/{lang}/"')
        html = html.replace('href="/search/"', f'href="/{lang}/search/"')
        html = html.replace('href="/quiz/"', f'href="/{lang}/quiz/"')
        html = html.replace('href="/compare/"', f'href="/{lang}/compare/"')
        html = html.replace('href="/plants/', f'href="/{lang}/plants/')
        
        # Update canonical
        html = re.sub(r'<link rel="canonical" href="[^"]+">',
                      f'<link rel="canonical" href="https://plantfinder.org/{lang}/plants/{plant_id}/">', html)
        
        with open(plant_dir / "index.html", "w") as f:
            f.write(html)
    
    print(f"  ✓ {lang}/plants/ ({len(plants)} plants)")

def update_sitemap():
    """Update sitemap with translated pages"""
    urls = []
    
    # English pages
    urls.append(('https://plantfinder.org/', '1.0'))
    urls.append(('https://plantfinder.org/search/', '0.9'))
    urls.append(('https://plantfinder.org/quiz/', '0.9'))
    urls.append(('https://plantfinder.org/compare/', '0.9'))
    urls.append(('https://plantfinder.org/faq/', '0.8'))
    urls.append(('https://plantfinder.org/about/', '0.7'))
    
    for plant in plants:
        urls.append((f'https://plantfinder.org/plants/{plant["id"]}/', '0.8'))
    
    # Spanish and German
    for lang in ['es', 'de']:
        urls.append((f'https://plantfinder.org/{lang}/', '1.0'))
        urls.append((f'https://plantfinder.org/{lang}/search/', '0.9'))
        urls.append((f'https://plantfinder.org/{lang}/quiz/', '0.9'))
        urls.append((f'https://plantfinder.org/{lang}/compare/', '0.9'))
        urls.append((f'https://plantfinder.org/{lang}/faq/', '0.8'))
        urls.append((f'https://plantfinder.org/{lang}/about/', '0.7'))
        
        for plant in plants:
            urls.append((f'https://plantfinder.org/{lang}/plants/{plant["id"]}/', '0.8'))
    
    sitemap = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
'''
    for url, priority in urls:
        sitemap += f'''  <url>
    <loc>{url}</loc>
    <priority>{priority}</priority>
  </url>
'''
    sitemap += '</urlset>'
    
    with open(BASE_DIR / "sitemap.xml", "w") as f:
        f.write(sitemap)
    
    print(f"✅ Sitemap updated with {len(urls)} URLs")

def main():
    print("Generating translations for PlantFinder...\n")
    
    for lang in ['es', 'de']:
        print(f"\n🌐 {translations[lang]['lang_name']} ({lang}):")
        generate_homepage(lang)
        generate_search_page(lang)
        generate_quiz_page(lang)
        generate_compare_page(lang)
        generate_faq_page(lang)
        generate_about_page(lang)
        generate_plant_pages(lang)
    
    print("\n")
    update_sitemap()
    print("\n🎉 Done!")

if __name__ == "__main__":
    main()
