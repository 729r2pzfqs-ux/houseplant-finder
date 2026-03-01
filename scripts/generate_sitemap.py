#!/usr/bin/env python3
"""Generate sitemap.xml with all pages and hreflang."""
import os
from datetime import date

BASE_URL = "https://plantfinder.org"
TODAY = date.today().isoformat()

# Static pages
STATIC_PAGES = [
    ("", 1.0, "weekly"),
    ("search/", 0.9, "weekly"),
    ("quiz/", 0.8, "monthly"),
    ("compare/", 0.8, "monthly"),
    ("about/", 0.5, "monthly"),
    ("faq/", 0.6, "monthly"),
]

LANGUAGES = ["en", "es", "de"]
LANG_PREFIXES = {"en": "", "es": "es/", "de": "de/"}

def generate_sitemap():
    urls = []
    
    # Static pages with hreflang
    for page, priority, freq in STATIC_PAGES:
        for lang in LANGUAGES:
            prefix = LANG_PREFIXES[lang]
            url = f"{BASE_URL}/{prefix}{page}"
            
            hreflangs = []
            for hl in LANGUAGES:
                hl_prefix = LANG_PREFIXES[hl]
                hreflangs.append(f'        <xhtml:link rel="alternate" hreflang="{hl}" href="{BASE_URL}/{hl_prefix}{page}"/>')
            hreflangs.append(f'        <xhtml:link rel="alternate" hreflang="x-default" href="{BASE_URL}/{page}"/>')
            
            urls.append(f"""    <url>
        <loc>{url}</loc>
        <lastmod>{TODAY}</lastmod>
        <changefreq>{freq}</changefreq>
        <priority>{priority}</priority>
{chr(10).join(hreflangs)}
    </url>""")
    
    # Plant pages
    plants_dir = "plants"
    if os.path.exists(plants_dir):
        for plant_slug in sorted(os.listdir(plants_dir)):
            if os.path.isdir(os.path.join(plants_dir, plant_slug)):
                for lang in LANGUAGES:
                    prefix = LANG_PREFIXES[lang]
                    url = f"{BASE_URL}/{prefix}plants/{plant_slug}/"
                    
                    hreflangs = []
                    for hl in LANGUAGES:
                        hl_prefix = LANG_PREFIXES[hl]
                        hreflangs.append(f'        <xhtml:link rel="alternate" hreflang="{hl}" href="{BASE_URL}/{hl_prefix}plants/{plant_slug}/"/>')
                    hreflangs.append(f'        <xhtml:link rel="alternate" hreflang="x-default" href="{BASE_URL}/plants/{plant_slug}/"/>')
                    
                    urls.append(f"""    <url>
        <loc>{url}</loc>
        <lastmod>{TODAY}</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.7</priority>
{chr(10).join(hreflangs)}
    </url>""")
    
    sitemap = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
{chr(10).join(urls)}
</urlset>'''
    
    with open("sitemap.xml", "w") as f:
        f.write(sitemap)
    
    print(f"Generated sitemap.xml with {len(urls)} URLs")

if __name__ == "__main__":
    generate_sitemap()
