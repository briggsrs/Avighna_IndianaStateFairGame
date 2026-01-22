#!/bin/bash
# PixelLab Sprite Generator for Indiana Treasure Quest
# Run this script to generate pixel art sprites for the famous Hoosiers

API_KEY="5f0d7a87-086d-4e2b-8510-40b21472b393"
API_URL="https://api.pixellab.ai/v1/generate-image"
OUTPUT_DIR="./sprites"

mkdir -p "$OUTPUT_DIR"

# Characters to generate
declare -a CHARACTERS=(
  "mj:pixel art portrait of Michael Jackson, king of pop singer, iconic 80s style, 64x64 game sprite, simple cute style"
  "larry:pixel art portrait of Larry Bird, basketball player, Boston Celtics jersey, 64x64 game sprite, simple cute style"
  "james:pixel art portrait of James Dean, 1950s movie star, leather jacket, 64x64 game sprite, simple cute style"
  "abe:pixel art portrait of Abraham Lincoln, tall hat, beard, president, 64x64 game sprite, simple cute style"
  "axl:pixel art portrait of Axl Rose, rock singer, bandana, long hair, 64x64 game sprite, simple cute style"
  "david:pixel art portrait of David Letterman, TV host, glasses, suit, 64x64 game sprite, simple cute style"
  "john:pixel art portrait of John Mellencamp, rock musician, guitar, 64x64 game sprite, simple cute style"
  "orville:pixel art portrait of Orville Redenbacher, elderly man, bow tie, glasses, popcorn, 64x64 game sprite, simple cute style"
)

echo "Generating sprites for Indiana Treasure Quest..."

for char in "${CHARACTERS[@]}"; do
  IFS=':' read -r id prompt <<< "$char"
  echo "Generating $id..."

  curl -s -X POST "$API_URL" \
    -H "Authorization: Bearer $API_KEY" \
    -H "Content-Type: application/json" \
    -d "{\"prompt\": \"$prompt\", \"width\": 64, \"height\": 64}" \
    -o "$OUTPUT_DIR/${id}.png"

  echo "  Saved to $OUTPUT_DIR/${id}.png"
  sleep 1  # Rate limiting
done

echo "Done! Sprites saved to $OUTPUT_DIR/"
