#!/usr/bin/env python3
"""
Bulk improvements for plantfinder.org:
1. Add GDPR consent banner with conditional GA loading
2. Add hreflang tags to plant pages
3. Create 404 redirect stubs for broken URLs
4. Fix SearchAction schema
5. Copy data files to es/ and de/ if missing
"""

import os
import json
from pathlib import Path
from bs4 import BeautifulSoup
import re

BASE_DIR = Path("/tmp/houseplant-finder")
GA_ID = "G-J2JW25BZPF"

# Templates
CONSENT_BANNER = '''
<script id="consent-banner-script">
(function() {
  const consentKey = 'plantfinder-consent';
  const scripts = document.querySelectorAll('script[data-ga-pending]');

  function loadGA() {
    // Load GA scripts that were marked as pending
    scripts.forEach(script => {
      const newScript = document.createElement('script');
      newScript.async = true;
      newScript.src = 'https://www.googletagmanager.com/gtag/js?id=''' + GA_ID + '''';
      document.head.appendChild(newScript);

      const configScript = document.createElement('script');
      configScript.textContent = `window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag("js",new Date());gtag("config","''' + GA_ID + '''");`;
      document.head.appendChild(configScript);
    });
  }

  function showConsentBanner() {
    const banner = document.createElement('div');
    banner.id = 'consent-banner';
    banner.style.cssText = `
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      background: #fff;
      border-top: 1px solid #e5e7eb;
      padding: 16px 24px;
      z-index: 9999;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-family: system-ui, -apple-system, sans-serif;
      font-size: 14px;
    `;

    const text = document.createElement('p');
    text.style.cssText = 'margin: 0; flex: 1; margin-right: 16px;';
    text.textContent = 'We use analytics to understand how you use our site and improve it.';

    const acceptBtn = document.createElement('button');
    acceptBtn.textContent = 'Accept';
    acceptBtn.style.cssText = `
      background: #16a34a;
      color: white;
      border: none;
      padding: 8px 24px;
      border-radius: 4px;
      cursor: pointer;
      font-size: 14px;
      font-weight: 500;
      white-space: nowrap;
    `;
    acceptBtn.onclick = function() {
      localStorage.setItem(consentKey, 'accepted');
      banner.remove();
      loadGA();
    };

    const denyBtn = document.createElement('button');
    denyBtn.textContent = 'Decline';
    denyBtn.style.cssText = `
      background: transparent;
      color: #666;
      border: 1px solid #ddd;
      padding: 8px 24px;
      border-radius: 4px;
      cursor: pointer;
      font-size: 14px;
      margin-left: 8px;
      white-space: nowrap;
    `;
    denyBtn.onclick = function() {
      localStorage.setItem(consentKey, 'declined');
      banner.remove();
    };

    banner.appendChild(text);
    banner.appendChild(acceptBtn);
    banner.appendChild(denyBtn);
    document.body.appendChild(banner);
  }

  const consent = localStorage.getItem(consentKey);
  if (!consent) {
    showConsentBanner();
  } else if (consent === 'accepted') {
    loadGA();
  }
})();
</script>
'''

REDIRECT_TEMPLATE = '''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta http-equiv="refresh" content="0;url={target}">
<link rel="canonical" href="{target}">
</head>
<body></body>
</html>
'''

def remove_ga_scripts(html_content):
    """Remove existing GA scripts from HTML."""
    # Remove gtag script tags
    html_content = re.sub(
        r'<script\s+async\s+src="https://www\.googletagmanager\.com/gtag/js\?id=G-[^"]+"></script>',
        '',
        html_content
    )
    # Remove gtag config script
    html_content = re.sub(
        r'<script>\s*window\.dataLayer\s*=\s*window\.dataLayer\s*\|\|.*?gtag\([\'"]config[\'"],\s*[\'"]G-[^\'"]+["\']\);\s*</script>',
        '',
        html_content,
        flags=re.DOTALL
    )
    return html_content

def add_consent_to_html(html_content, filename):
    """Add consent banner before </body>."""
    # First remove existing GA scripts
    html_content = remove_ga_scripts(html_content)

    # Insert consent banner before </body>
    if '</body>' in html_content:
        html_content = html_content.replace('</body>', CONSENT_BANNER + '\n</body>')
    else:
        # Fallback if no </body> tag
        html_content += CONSENT_BANNER

    return html_content

def add_hreflang_tags(html_content, slug):
    """Add hreflang tags to plant pages."""
    soup = BeautifulSoup(html_content, 'html.parser')
    head = soup.find('head')

    if not head:
        return html_content

    # Check if hreflang tags already exist
    if head.find('link', rel='alternate', attrs={'hreflang': True}):
        return html_content

    # Create hreflang links
    hreflang_links = [
        f'<link rel="alternate" hreflang="en" href="https://plantfinder.org/plants/{slug}/" />',
        f'<link rel="alternate" hreflang="es" href="https://plantfinder.org/es/plants/{slug}/" />',
        f'<link rel="alternate" hreflang="de" href="https://plantfinder.org/de/plants/{slug}/" />',
        f'<link rel="alternate" hreflang="x-default" href="https://plantfinder.org/plants/{slug}/" />'
    ]

    # Insert before closing </head>
    hreflang_html = '\n    '.join(hreflang_links)
    html_content = html_content.replace('</head>', f'    {hreflang_html}\n  </head>')

    return html_content

def add_hreflang_es(html_content, slug):
    """Add hreflang tags for Spanish plant pages."""
    soup = BeautifulSoup(html_content, 'html.parser')
    head = soup.find('head')

    if not head:
        return html_content

    # Check if hreflang tags already exist
    if head.find('link', rel='alternate', attrs={'hreflang': True}):
        return html_content

    hreflang_links = [
        f'<link rel="alternate" hreflang="en" href="https://plantfinder.org/plants/{slug}/" />',
        f'<link rel="alternate" hreflang="es" href="https://plantfinder.org/es/plants/{slug}/" />',
        f'<link rel="alternate" hreflang="de" href="https://plantfinder.org/de/plants/{slug}/" />',
        f'<link rel="alternate" hreflang="x-default" href="https://plantfinder.org/plants/{slug}/" />'
    ]

    hreflang_html = '\n    '.join(hreflang_links)
    html_content = html_content.replace('</head>', f'    {hreflang_html}\n  </head>')

    return html_content

def add_hreflang_de(html_content, slug):
    """Add hreflang tags for German plant pages."""
    soup = BeautifulSoup(html_content, 'html.parser')
    head = soup.find('head')

    if not head:
        return html_content

    # Check if hreflang tags already exist
    if head.find('link', rel='alternate', attrs={'hreflang': True}):
        return html_content

    hreflang_links = [
        f'<link rel="alternate" hreflang="en" href="https://plantfinder.org/plants/{slug}/" />',
        f'<link rel="alternate" hreflang="es" href="https://plantfinder.org/es/plants/{slug}/" />',
        f'<link rel="alternate" hreflang="de" href="https://plantfinder.org/de/plants/{slug}/" />',
        f'<link rel="alternate" hreflang="x-default" href="https://plantfinder.org/plants/{slug}/" />'
    ]

    hreflang_html = '\n    '.join(hreflang_links)
    html_content = html_content.replace('</head>', f'    {hreflang_html}\n  </head>')

    return html_content

def create_redirect(source_path, target):
    """Create a redirect page."""
    source_path.parent.mkdir(parents=True, exist_ok=True)
    redirect_content = REDIRECT_TEMPLATE.format(target=target)
    source_path.write_text(redirect_content)

def fix_search_action(html_content):
    """Fix SearchAction schema to use EntryPoint."""
    # Replace the target pattern
    pattern = r'"target"\s*:\s*"https://plantfinder\.org/search/\?q=\{search_term_string\}"'
    replacement = '"target": {\n  "@type": "EntryPoint",\n  "urlTemplate": "https://plantfinder.org/search/?q={search_term_string}"\n}'

    html_content = re.sub(pattern, replacement, html_content)
    return html_content

def copy_data_files():
    """Copy data files to es/ and de/ directories if they don't exist."""
    en_plants_file = BASE_DIR / 'data' / 'plants.json'

    if en_plants_file.exists():
        # Copy to es/data/
        es_data_dir = BASE_DIR / 'es' / 'data'
        es_data_dir.mkdir(parents=True, exist_ok=True)
        es_plants_file = es_data_dir / 'plants.json'
        if not es_plants_file.exists():
            es_plants_file.write_text(en_plants_file.read_text())
            print(f"Created: {es_plants_file}")

        # Copy to de/data/
        de_data_dir = BASE_DIR / 'de' / 'data'
        de_data_dir.mkdir(parents=True, exist_ok=True)
        de_plants_file = de_data_dir / 'plants.json'
        if not de_plants_file.exists():
            de_plants_file.write_text(en_plants_file.read_text())
            print(f"Created: {de_plants_file}")

def process_all_html_files():
    """Process all HTML files with GDPR consent."""
    modified_count = 0

    for html_file in BASE_DIR.rglob('index.html'):
        try:
            content = html_file.read_text(encoding='utf-8')
            original_content = content

            # Add GDPR consent (for all HTML files)
            content = add_consent_to_html(content, str(html_file))

            # Fix SearchAction in main index.html
            if html_file.name == 'index.html' and html_file.parent == BASE_DIR:
                content = fix_search_action(content)

            if content != original_content:
                html_file.write_text(content, encoding='utf-8')
                modified_count += 1
        except Exception as e:
            print(f"Error processing {html_file}: {e}")

    return modified_count

def process_plant_pages():
    """Add hreflang tags to plant pages."""
    modified_count = 0

    # Process EN plants
    en_plants_dir = BASE_DIR / 'plants'
    for plant_dir in en_plants_dir.iterdir():
        if plant_dir.is_dir():
            index_file = plant_dir / 'index.html'
            if index_file.exists():
                slug = plant_dir.name
                try:
                    content = index_file.read_text(encoding='utf-8')
                    original_content = content
                    content = add_hreflang_tags(content, slug)

                    if content != original_content:
                        index_file.write_text(content, encoding='utf-8')
                        modified_count += 1
                except Exception as e:
                    print(f"Error processing {index_file}: {e}")

    # Process ES plants
    es_plants_dir = BASE_DIR / 'es' / 'plants'
    if es_plants_dir.exists():
        for plant_dir in es_plants_dir.iterdir():
            if plant_dir.is_dir():
                index_file = plant_dir / 'index.html'
                if index_file.exists():
                    slug = plant_dir.name
                    try:
                        content = index_file.read_text(encoding='utf-8')
                        original_content = content
                        content = add_hreflang_es(content, slug)

                        if content != original_content:
                            index_file.write_text(content, encoding='utf-8')
                            modified_count += 1
                    except Exception as e:
                        print(f"Error processing {index_file}: {e}")

    # Process DE plants
    de_plants_dir = BASE_DIR / 'de' / 'plants'
    if de_plants_dir.exists():
        for plant_dir in de_plants_dir.iterdir():
            if plant_dir.is_dir():
                index_file = plant_dir / 'index.html'
                if index_file.exists():
                    slug = plant_dir.name
                    try:
                        content = index_file.read_text(encoding='utf-8')
                        original_content = content
                        content = add_hreflang_de(content, slug)

                        if content != original_content:
                            index_file.write_text(content, encoding='utf-8')
                            modified_count += 1
                    except Exception as e:
                        print(f"Error processing {index_file}: {e}")

    return modified_count

def create_404_redirects():
    """Create redirect pages for common 404 URLs."""
    created_count = 0
    redirects = []

    # Template slug redirects
    redirects.append((BASE_DIR / 'plants' / '${p.slug}' / 'index.html', '/'))
    redirects.append((BASE_DIR / 'es' / 'plants' / '${p.slug}' / 'index.html', '/es/'))
    redirects.append((BASE_DIR / 'de' / 'plants' / '${plant.id}' / 'index.html', '/de/'))
    redirects.append((BASE_DIR / 'de' / 'plants' / '${p.slug}' / 'index.html', '/de/'))
    redirects.append((BASE_DIR / 'plants' / '${plant.id}' / 'index.html', '/'))

    # Generic dracaena redirects (find closest existing dracaena page)
    dracaena_target = '/plants/dracaena-marginata/'
    es_dracaena_target = '/es/plants/dracaena-marginata/'
    de_dracaena_target = '/de/plants/dracaena-marginata/'

    redirects.append((BASE_DIR / 'plants' / 'dracaena' / 'index.html', dracaena_target))
    redirects.append((BASE_DIR / 'es' / 'plants' / 'dracaena' / 'index.html', es_dracaena_target))
    redirects.append((BASE_DIR / 'de' / 'plants' / 'dracaena' / 'index.html', de_dracaena_target))

    # Missing plant directory indices
    redirects.append((BASE_DIR / 'plants' / 'index.html', '/'))
    redirects.append((BASE_DIR / 'es' / 'plants' / 'index.html', '/es/'))
    redirects.append((BASE_DIR / 'de' / 'plants' / 'index.html', '/de/'))

    for redirect_path, target in redirects:
        try:
            redirect_path.parent.mkdir(parents=True, exist_ok=True)
            create_redirect(redirect_path, target)
            created_count += 1
        except Exception as e:
            print(f"Error creating redirect {redirect_path}: {e}")

    return created_count

def main():
    print("Starting bulk improvements...")

    # Step 1: Process all HTML files (GDPR consent and SearchAction fix)
    print("\n1. Adding GDPR consent banners to all HTML files...")
    consent_count = process_all_html_files()
    print(f"   Modified {consent_count} HTML files with GDPR consent")

    # Step 2: Add hreflang tags to plant pages
    print("\n2. Adding hreflang tags to plant pages...")
    hreflang_count = process_plant_pages()
    print(f"   Added hreflang to {hreflang_count} plant pages")

    # Step 3: Create 404 redirect stubs
    print("\n3. Creating 404 redirect stubs...")
    redirect_count = create_404_redirects()
    print(f"   Created {redirect_count} redirect pages")

    # Step 4: Copy data files
    print("\n4. Copying data files to language directories...")
    copy_data_files()
    print("   Data files checked/copied")

    total_modified = consent_count + hreflang_count + redirect_count
    print(f"\n✓ Complete! Total files modified/created: {total_modified}")

if __name__ == '__main__':
    main()
