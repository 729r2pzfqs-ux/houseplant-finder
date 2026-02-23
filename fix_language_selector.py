#!/usr/bin/env python3
"""Fix language selector to match BreedFinder style - in header nav, hover dropdown"""

import os
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent

# Language selector HTML for each language
LANG_SELECTOR = {
    "en": '''<!-- Language selector -->
                <div class="relative group">
                    <button class="flex items-center gap-1 text-slate-600 hover:text-emerald-700 py-2">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
                        <span>EN</span>
                    </button>
                    <div class="absolute right-0 top-full bg-white border border-slate-200 rounded-xl shadow-xl hidden group-hover:block min-w-[140px] py-2 z-50 before:absolute before:h-2 before:-top-2 before:left-0 before:right-0 before:bg-transparent">
                        <a href="/" class="block px-4 py-2 hover:bg-slate-100 font-semibold text-emerald-700">English</a>
                        <a href="/es/" class="block px-4 py-2 hover:bg-slate-100 text-slate-600">Español</a>
                        <a href="/de/" class="block px-4 py-2 hover:bg-slate-100 text-slate-600">Deutsch</a>
                    </div>
                </div>''',
    "es": '''<!-- Language selector -->
                <div class="relative group">
                    <button class="flex items-center gap-1 text-slate-600 hover:text-emerald-700 py-2">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
                        <span>ES</span>
                    </button>
                    <div class="absolute right-0 top-full bg-white border border-slate-200 rounded-xl shadow-xl hidden group-hover:block min-w-[140px] py-2 z-50 before:absolute before:h-2 before:-top-2 before:left-0 before:right-0 before:bg-transparent">
                        <a href="/" class="block px-4 py-2 hover:bg-slate-100 text-slate-600">English</a>
                        <a href="/es/" class="block px-4 py-2 hover:bg-slate-100 font-semibold text-emerald-700">Español</a>
                        <a href="/de/" class="block px-4 py-2 hover:bg-slate-100 text-slate-600">Deutsch</a>
                    </div>
                </div>''',
    "de": '''<!-- Language selector -->
                <div class="relative group">
                    <button class="flex items-center gap-1 text-slate-600 hover:text-emerald-700 py-2">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
                        <span>DE</span>
                    </button>
                    <div class="absolute right-0 top-full bg-white border border-slate-200 rounded-xl shadow-xl hidden group-hover:block min-w-[140px] py-2 z-50 before:absolute before:h-2 before:-top-2 before:left-0 before:right-0 before:bg-transparent">
                        <a href="/" class="block px-4 py-2 hover:bg-slate-100 text-slate-600">English</a>
                        <a href="/es/" class="block px-4 py-2 hover:bg-slate-100 text-slate-600">Español</a>
                        <a href="/de/" class="block px-4 py-2 hover:bg-slate-100 font-semibold text-emerald-700">Deutsch</a>
                    </div>
                </div>'''
}

def get_lang_from_path(filepath):
    """Determine language from file path"""
    path_str = str(filepath)
    if "/es/" in path_str:
        return "es"
    elif "/de/" in path_str:
        return "de"
    return "en"

def fix_file(filepath):
    """Fix language selector in a single file"""
    with open(filepath, 'r') as f:
        content = f.read()
    
    lang = get_lang_from_path(filepath)
    
    # Remove old fixed position language selector
    content = re.sub(
        r'<div style="position:fixed;top:80px;right:20px;z-index:50;">.*?</select>\s*</div>',
        '',
        content,
        flags=re.DOTALL
    )
    
    # Also remove any other fixed language selectors
    content = re.sub(
        r'<div style="position:fixed;bottom:20px;right:20px;z-index:50;">.*?</select>\s*</div>',
        '',
        content,
        flags=re.DOTALL
    )
    
    # Check if language selector already in nav
    if '<!-- Language selector -->' in content:
        with open(filepath, 'w') as f:
            f.write(content)
        return "cleaned"
    
    # Add language selector to nav (before closing </nav>)
    selector = LANG_SELECTOR[lang]
    
    # Find the nav and add selector before </nav>
    if '</nav>' in content:
        content = content.replace('</nav>', f'{selector}\n            </nav>', 1)
    
    with open(filepath, 'w') as f:
        f.write(content)
    
    return "updated"

def main():
    print("Fixing language selectors...\\n")
    
    count = 0
    for html_file in BASE_DIR.rglob("*.html"):
        # Skip non-page files
        if "node_modules" in str(html_file):
            continue
        
        result = fix_file(html_file)
        count += 1
        if count % 50 == 0:
            print(f"  Processed {count} files...")
    
    print(f"\\n✅ Fixed {count} files")

if __name__ == "__main__":
    main()
