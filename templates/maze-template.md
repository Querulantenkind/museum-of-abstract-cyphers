# Maze Template

Design your own labyrinth by adding walls and paths.

```
┌─────────────────┐
│                 │
│                 │
│                 │
│                 │
│                 │
│                 │
│                 │
│                 │
└─────────────────┘
```

## Design Elements
- Walls: █ ▓ ▒ ░ ║ ═ │ ─
- Paths: · ∘ ○ ●
- Entrance/Exit: mark with ▶ or ★
- Center: place a goal marker ◎

## Maze Types
- **Unicursal**: One path, no choices
- **Classical**: Multiple paths, dead ends
- **Spiral**: Winds toward center
- **Branching**: Multiple solution paths

## Example Structure
```
┌─────────────────┐
│ █ █████ ███ █ █ │
│   █     █   █   │
│ █ █ ███ █ ███ █ │
│ █   █   █   █ █ │
│ ███████████ █ █ │
└─────────────────┘
```
