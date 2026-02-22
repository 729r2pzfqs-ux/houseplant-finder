#!/usr/bin/env python3
"""Update plant pages to use verified correct images only"""

import os
import re

BASE_DIR = os.path.expanduser("~/clawd/houseplant-finder")
PLANTS_DIR = os.path.join(BASE_DIR, "plants")
IMAGES_DIR = os.path.join(BASE_DIR, "images/plants")

# Verified correct images only
VERIFIED_IMAGES = {
    "monstera-deliciosa",
    "boston-fern",
    "pothos-golden",
    "aloe-vera",
    "jade-plant",
    "bunny-ears-cactus",
    "areca-palm",
    "haworthia-zebra",
    "peace-lily",
}

# Placeholder HTML (current)
PLACEHOLDER_PATTERN = re.compile(
    r'<div class="aspect-\[4/5\] bg-gradient-to-br from-emerald-100.*?</div>\s*</div>',
    re.DOTALL
)

def get_image_html(plant_id):
    """Generate image HTML - real image or placeholder"""
    if plant_id in VERIFIED_IMAGES:
        return f'''<div class="aspect-[4/5] bg-slate-100 relative overflow-hidden">
                        <img src="/images/plants/{plant_id}.png" 
                             alt="{plant_id.replace('-', ' ').title()}" 
                             class="w-full h-full object-cover"
                             loading="lazy">
                    </div>'''
    else:
        return '''<div class="aspect-[4/5] bg-gradient-to-br from-emerald-100 via-teal-100 to-lime-100 relative overflow-hidden flex items-center justify-center">
                        <span class="text-9xl">🪴</span>
                        <div class="absolute bottom-4 left-4 right-4 bg-white/90 backdrop-blur rounded-xl p-3 text-center text-sm text-slate-500">
                            <i data-lucide="image" class="w-4 h-4 inline mr-1"></i>
                            Image coming soon
                        </div>
                    </div>'''

def update_plant_page(plant_id):
    """Update a single plant page with correct image"""
    page_path = os.path.join(PLANTS_DIR, plant_id, "index.html")
    
    if not os.path.exists(page_path):
        return False, "not found"
    
    with open(page_path, 'r') as f:
        content = f.read()
    
    # Find and replace image section
    new_image_html = get_image_html(plant_id)
    
    # Pattern to match the image container div
    pattern = r'(<div class="md:w-2/5">\s*)<div class="aspect-\[4/5\][^>]*>.*?</div>\s*</div>(\s*</div>)'
    
    def replacer(match):
        return match.group(1) + new_image_html + match.group(2)
    
    new_content, count = re.subn(pattern, replacer, content, flags=re.DOTALL)
    
    if count > 0:
        with open(page_path, 'w') as f:
            f.write(new_content)
        return True, "updated"
    else:
        return False, "pattern not found"

def main():
    print("🌿 Updating plant pages with verified images...")
    print(f"📷 Verified images: {len(VERIFIED_IMAGES)}")
    print()
    
    updated = 0
    skipped = 0
    errors = []
    
    # Get all plant directories
    plant_dirs = sorted([d for d in os.listdir(PLANTS_DIR) 
                        if os.path.isdir(os.path.join(PLANTS_DIR, d))])
    
    for plant_id in plant_dirs:
        success, status = update_plant_page(plant_id)
        if success:
            has_image = "✅" if plant_id in VERIFIED_IMAGES else "⬜"
            print(f"{has_image} {plant_id}")
            updated += 1
        else:
            print(f"❌ {plant_id}: {status}")
            errors.append(plant_id)
    
    print()
    print(f"{'='*50}")
    print(f"✅ Updated: {updated}")
    print(f"📷 With real images: {len([p for p in plant_dirs if p in VERIFIED_IMAGES])}")
    print(f"⬜ With placeholders: {updated - len([p for p in plant_dirs if p in VERIFIED_IMAGES])}")
    if errors:
        print(f"❌ Errors: {len(errors)}")

if __name__ == "__main__":
    main()
