# Indiana Treasure Quest

## Project Overview
An educational Indiana-themed treasure hunting game built as a single HTML file. Players choose a famous Hoosier avatar and travel through Indiana towns via underground sewers, answering trivia questions about Indiana history and culture.

## Tech Stack
- Single HTML file with embedded CSS and JavaScript
- Leaflet.js + OpenStreetMap for interactive map
- No build process required - just open in browser
- LocalStorage for game state persistence

## Game Flow
1. **Avatar Selection** - Choose from 8 famous Hoosiers (Michael Jackson, Larry Bird, etc.)
2. **Backstory** - Mission briefing from the Mayor of Indianapolis
3. **Travel Loop**:
   - Tunnel mini-game (collect coins while avoiding obstacles)
   - Map view with animated avatar movement
   - Question (19 total) or Fact (7 total, auto-advance after 4s)
   - Skip option available on questions (costs coins from that city's tunnel)
4. **Artifact Discovery** - Found at Angola (stop #16)
5. **End Game** - Return to Indianapolis, present artifact to Mayor, submit score to leaderboard, write review

## Route (28 stops)
Indianapolis → Bloomington → Vincennes → Washington → Evansville → New Albany → Bedford → Seymour → Columbus → Shelbyville → Richmond → New Castle → Muncie → Marion → Huntington → Fort Wayne → **Angola (artifact)** → Elkhart → South Bend → La Porte → Michigan City → Gary → Hammond → Logansport → Lafayette → Kokomo → Terre Haute → Indianapolis

## Key Files
- `AviGame.html` - The complete game (single file)
- `CLAUDE.md` - This file
- `sprites/` - Pixel art character sprites generated via PixelLab MCP
  - Each character has a subdirectory with `metadata.json`, rotations, and animations

## Famous Hoosier Avatars
| Character | Title | Hometown |
|-----------|-------|----------|
| Michael Jackson | King of Pop | Gary |
| Larry Bird | NBA Legend | French Lick |
| James Dean | Hollywood Icon | Marion |
| Abraham Lincoln | 16th President | Spencer County |
| Axl Rose | Rock Legend | Lafayette |
| David Letterman | TV Host | Indianapolis |
| John Mellencamp | Rock Singer | Seymour |
| Orville Redenbacher | Popcorn King | Brazil |

## Scoring System
- **Questions**: Correct answers earn points toward total score
- **Coins**: Collected in tunnel mini-game between cities
- **Total Points**: Score + Coins combined for leaderboard ranking
- **Skip Penalty**: Skipping a question costs the coins collected in that city's tunnel

## Leaderboard
- **Individual**: Top players by total points
- **Class**: Aggregated scores by teacher
- **School**: Aggregated scores by school
- Teachers/Schools can be selected from dropdown or entered manually via "Other" option
- Stored in localStorage

## Responsive Design
- Fully responsive layout using CSS clamp(), vh/vw units, and flexbox
- Tunnel mini-game uses percentage-based positioning for all elements
- Media queries for small screens (max-width: 480px), short screens (max-height: 500px), and landscape orientation

## Development Notes
- Questions and facts are randomly distributed each playthrough
- Game state saves to localStorage automatically
- Map shows traveled route (green) vs upcoming route (dashed gray)
- Avatar animates smoothly between towns on the map
- Tunnel game tracks `lastTunnelCoins` for skip functionality

## MCP Servers
- **PixelLab** - For generating pixel art sprites: `claude mcp add pixellab https://api.pixellab.ai/mcp -t http -H "Authorization: Bearer <key>"`
