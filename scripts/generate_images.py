#!/usr/bin/env python3
"""
Batch generate houseplant images using Replicate API (Flux 1.1 Pro - highest quality)
Uses direct HTTP API calls for Python 3.14 compatibility.
"""

import os
import json
import requests
import time
import sys

API_URL = "https://api.replicate.com/v1/models/black-forest-labs/flux-1.1-pro/predictions"

def load_plants():
    """Load plants from JSON data"""
    script_dir = os.path.dirname(__file__)
    data_path = os.path.join(script_dir, "..", "data", "plants.json")
    with open(data_path, 'r') as f:
        return json.load(f)

def generate_prompt(plant):
    """Generate the image prompt for a plant"""
    name = plant['name']
    category = plant.get('category', 'foliage')
    size = plant.get('size', 'medium')
    
    # Customize prompt based on plant type
    if category == 'succulent':
        container = "a modern minimalist ceramic pot"
        style = "showing the succulent rosette or compact form"
    elif category == 'cactus':
        container = "a terracotta pot"
        style = "showing the distinctive cactus form and spines"
    elif category == 'trailing':
        container = "a white ceramic hanging planter"
        style = "with beautiful trailing vines cascading down"
    elif category == 'fern':
        container = "an elegant ceramic pot"
        style = "with lush feathery fronds"
    elif category == 'palm':
        container = "a woven basket planter"
        style = "with graceful arching fronds"
    elif category == 'flowering':
        container = "a decorative ceramic pot"
        style = "showcasing blooms or elegant flowers"
    else:  # foliage
        container = "a minimalist white ceramic pot"
        style = "showcasing the beautiful foliage"
    
    if size == 'large':
        size_desc = "a full-sized mature"
    elif size == 'small':
        size_desc = "a compact"
    else:
        size_desc = "a healthy"
    
    return f"""Ultra realistic studio photograph of {size_desc} {name} houseplant in {container}, {style}. 
The plant is framed in a vertical 4:5 portrait composition, centered, with the pot at the bottom third.
Soft diffused studio lighting, shallow depth of field creating a professional look.
Seamless light grey studio background with subtle natural shadow under the pot.
Professional botanical photography style, crisp focus on the plant, no props, no text, no watermarks.
The plant should look healthy, vibrant, and true to species characteristics."""

def wait_for_prediction(prediction_url, headers, max_wait=60):
    """Poll until prediction is complete"""
    start = time.time()
    while time.time() - start < max_wait:
        try:
            response = requests.get(prediction_url, headers=headers, timeout=30)
            data = response.json()
            status = data.get('status')
            
            if status == 'succeeded':
                return data.get('output')
            elif status == 'failed':
                error_msg = data.get('error') or 'unknown error'
                print(f" (failed: {error_msg})", end="")
                return None
            elif status == 'canceled':
                print(f" (canceled)", end="")
                return None
            
            # Still processing (starting/processing), wait and retry
            time.sleep(2)
        except Exception as e:
            print(f" (poll error: {e})", end="")
            time.sleep(2)
    
    print(f" (timeout)", end="")
    return None

def generate_image(plant, output_dir, api_token):
    """Generate a single plant image"""
    slug = plant['id']
    output_path = os.path.join(output_dir, f"{slug}.png")
    
    # Skip if already exists
    if os.path.exists(output_path):
        print(f"⏭️  Skipping {plant['name']} (already exists)")
        return True, "skipped"
    
    prompt = generate_prompt(plant)
    print(f"🌱 Generating {plant['name']}...", end="", flush=True)
    
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "input": {
            "prompt": prompt,
            "aspect_ratio": "4:5",
            "output_format": "png",
            "output_quality": 100,
            "safety_tolerance": 2,
            "prompt_upsampling": True
        }
    }
    
    try:
        # Create prediction
        response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
        data = response.json()
        
        # Check for actual error (not null)
        if data.get('error'):
            print(f"\n❌ API error: {data['error']}")
            return False, data['error']
        
        # Get the prediction URL for polling
        prediction_id = data.get('id')
        if not prediction_id:
            print(f"\n❌ No prediction ID returned")
            return False, "no_id"
        
        prediction_url = f"https://api.replicate.com/v1/predictions/{prediction_id}"
        
        # Poll for completion
        output = wait_for_prediction(prediction_url, headers)
        
        if output:
            img_url = str(output)
            img_response = requests.get(img_url, timeout=60)
            
            os.makedirs(output_dir, exist_ok=True)
            with open(output_path, 'wb') as f:
                f.write(img_response.content)
            
            print(f"\n✅ Saved {slug}.png ({len(img_response.content) // 1024}KB)")
            return True, "generated"
        else:
            print(f"\n❌ No output for {plant['name']}")
            return False, "no_output"
            
    except Exception as e:
        print(f"\n❌ Error generating {plant['name']}: {e}")
        return False, str(e)

def main():
    print("🌿 HousePlantFinder Image Generator (Flux 1.1 Pro - Highest Quality)")
    print("="*60)
    
    # Check API key
    api_token = os.environ.get("REPLICATE_API_TOKEN")
    if not api_token:
        print("❌ Error: REPLICATE_API_TOKEN not set")
        print("   Run: export REPLICATE_API_TOKEN=your_token_here")
        return 1
    
    # Load plants
    plants = load_plants()
    print(f"📦 {len(plants)} plants to generate\n")
    
    script_dir = os.path.dirname(__file__)
    output_dir = os.path.join(script_dir, "..", "images", "plants")
    
    success = 0
    skipped = 0
    failed = []
    
    for i, plant in enumerate(plants, 1):
        print(f"[{i}/{len(plants)}] ", end="")
        result, status = generate_image(plant, output_dir, api_token)
        
        if result:
            if status == "skipped":
                skipped += 1
            else:
                success += 1
        else:
            failed.append(plant['name'])
        
        # Small delay between requests to avoid rate limits
        time.sleep(0.5)
    
    print(f"\n{'='*60}")
    print(f"✅ Generated: {success}")
    print(f"⏭️  Skipped: {skipped}")
    if failed:
        print(f"❌ Failed ({len(failed)}): {', '.join(failed[:10])}")
        if len(failed) > 10:
            print(f"   ... and {len(failed) - 10} more")
    print(f"📁 Output: {output_dir}")
    
    # Calculate cost estimate
    cost = success * 0.04
    print(f"💰 Estimated cost: ${cost:.2f}")
    
    return 0 if not failed else 1

if __name__ == "__main__":
    sys.exit(main())
