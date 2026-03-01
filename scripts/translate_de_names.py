#!/usr/bin/env python3
"""Translate plant names in German detail pages."""
import os
import re

PLANT_NAMES_DE = {
    "Monstera Deliciosa": "Fensterblatt",
    "Golden Pothos": "Goldene Efeutute",
    "Snake Plant": "Bogenhanf",
    "Peace Lily": "Einblatt",
    "Fiddle Leaf Fig": "Geigenfeige",
    "Rubber Plant": "Gummibaum",
    "ZZ Plant": "Zamioculcas",
    "Spider Plant": "Grünlilie",
    "Boston Fern": "Schwertfarn",
    "Aloe Vera": "Aloe Vera",
    "Heartleaf Philodendron": "Herzblatt-Philodendron",
    "Chinese Evergreen": "Kolbenfaden",
    "Jade Plant": "Geldbaum",
    "Bird of Paradise": "Strelitzie",
    "Parlor Palm": "Bergpalme",
    "Calathea Medallion": "Korbmarante",
    "String of Pearls": "Erbsenpflanze",
    "Pothos Marble Queen": "Efeutute Marble Queen",
    "Dracaena Marginata": "Drachenbaum",
    "Bamboo Palm": "Bambuspalme",
    "English Ivy": "Efeu",
    "Prayer Plant": "Pfeilwurz",
    "Croton": "Kroton",
    "Dieffenbachia": "Dieffenbachie",
    "Areca Palm": "Goldfruchtpalme",
    "Cast Iron Plant": "Schusterpalme",
    "Chinese Money Plant": "Ufopflanze",
    "Hoya Carnosa": "Wachsblume",
    "Calathea Orbifolia": "Calathea Orbifolia",
    "Birds Nest Fern": "Nestfarn",
    "African Violet": "Usambaraveilchen",
    "Peperomia": "Zwergpfeffer",
    "Anthurium": "Flamingoblume",
    "Schefflera": "Strahlenaralie",
    "Yucca": "Yucca-Palme",
    "Norfolk Island Pine": "Zimmertanne",
    "Weeping Fig": "Birkenfeige",
    "Monstera Adansonii": "Monstera Adansonii",
    "Philodendron Brasil": "Philodendron Brasil",
    "Pothos Neon": "Neon Efeutute",
    "String of Hearts": "Leuchterblume",
    "Swiss Cheese Plant": "Fensterblatt",
    "Mother-in-Law's Tongue": "Bogenhanf",
    "Devil's Ivy": "Efeutute",
    "Rubber Tree": "Gummibaum",
}

def translate_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    for en_name, de_name in PLANT_NAMES_DE.items():
        # Replace in title, h1, breadcrumb, etc. but preserve the original for "Also known as"
        content = re.sub(
            rf'<title>{re.escape(en_name)} -',
            f'<title>{de_name} -',
            content
        )
        content = re.sub(
            rf'<h1[^>]*>{re.escape(en_name)}</h1>',
            f'<h1 class="text-3xl md:text-4xl font-bold text-slate-900 mb-2">{de_name}</h1>',
            content
        )
        content = re.sub(
            rf'<span class="text-slate-700">{re.escape(en_name)}</span>',
            f'<span class="text-slate-700">{de_name}</span>',
            content
        )
        content = re.sub(
            rf'"headline": "{re.escape(en_name)}:',
            f'"headline": "{de_name}:',
            content
        )
        content = re.sub(
            rf'og:title" content="{re.escape(en_name)} -',
            f'og:title" content="{de_name} -',
            content
        )
        # Replace in meta description start
        content = re.sub(
            rf'Pflegeanleitung für {re.escape(en_name)}\.',
            f'Pflegeanleitung für {de_name}.',
            content
        )
        content = re.sub(
            rf'wie du deine {re.escape(en_name)} gesund',
            f'wie du deine {de_name} gesund',
            content
        )
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    de_plants_dir = 'de/plants'
    count = 0
    for plant_dir in os.listdir(de_plants_dir):
        filepath = os.path.join(de_plants_dir, plant_dir, 'index.html')
        if os.path.exists(filepath):
            if translate_file(filepath):
                count += 1
                print(f"✓ {plant_dir}")
    
    print(f"\nUpdated {count} German plant pages")

if __name__ == "__main__":
    main()
