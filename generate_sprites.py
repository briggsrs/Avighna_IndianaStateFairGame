#!/usr/bin/env python3
"""
PixelLab Sprite Generator for Indiana Treasure Quest
Run: python3 generate_sprites.py
"""

import requests
import os
import time
import base64

API_KEY = "5f0d7a87-086d-4e2b-8510-40b21472b393"
API_URL = "https://api.pixellab.ai/v2/text-to-pixel"
OUTPUT_DIR = "./sprites"

# Famous Hoosiers to generate sprites for
CHARACTERS = [
    ("mj", "pixel art portrait of Michael Jackson, king of pop, iconic singer, sparkly glove, 80s style"),
    ("larry", "pixel art portrait of Larry Bird, basketball player, green and white jersey number 33"),
    ("james", "pixel art portrait of James Dean, 1950s movie star, leather jacket, cool hair"),
    ("abe", "pixel art portrait of Abraham Lincoln, tall black top hat, beard, bow tie"),
    ("axl", "pixel art portrait of Axl Rose, rock singer, red bandana, long red hair"),
    ("david", "pixel art portrait of David Letterman, TV host, glasses, gray hair, suit"),
    ("john", "pixel art portrait of John Mellencamp, rock musician, jeans, guitar"),
    ("orville", "pixel art portrait of Orville Redenbacher, elderly man, bow tie, glasses, white hair"),
]

def generate_sprite(char_id, prompt):
    """Generate a pixel art sprite using PixelLab API"""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "description": f"{prompt}, cute game character sprite, simple style, solid background",
        "pixel_size": 8,
        "image_size": {"width": 64, "height": 64}
    }

    try:
        print(f"Generating {char_id}...")
        response = requests.post(API_URL, json=payload, headers=headers, timeout=60)

        if response.status_code == 200:
            data = response.json()
            # Handle base64 image response
            if "image" in data:
                image_data = base64.b64decode(data["image"])
                filepath = os.path.join(OUTPUT_DIR, f"{char_id}.png")
                with open(filepath, "wb") as f:
                    f.write(image_data)
                print(f"  ✓ Saved to {filepath}")
                return True
            # Handle direct binary response
            elif response.headers.get("content-type", "").startswith("image"):
                filepath = os.path.join(OUTPUT_DIR, f"{char_id}.png")
                with open(filepath, "wb") as f:
                    f.write(response.content)
                print(f"  ✓ Saved to {filepath}")
                return True
            else:
                print(f"  Response: {data}")
        else:
            print(f"  ✗ Error {response.status_code}: {response.text[:200]}")

    except Exception as e:
        print(f"  ✗ Error: {e}")

    return False

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("=" * 50)
    print("Indiana Treasure Quest - Sprite Generator")
    print("=" * 50)
    print()

    success_count = 0
    for char_id, prompt in CHARACTERS:
        if generate_sprite(char_id, prompt):
            success_count += 1
        time.sleep(2)  # Rate limiting

    print()
    print(f"Generated {success_count}/{len(CHARACTERS)} sprites")
    print(f"Sprites saved to: {OUTPUT_DIR}/")

if __name__ == "__main__":
    main()
