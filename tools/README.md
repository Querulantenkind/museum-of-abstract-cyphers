# Tools & Resources

This directory contains tools and resources to help you create and experiment with ASCII art.

## Pattern Generators

### Python Generator (`pattern_generator.py`)

Generate ASCII art patterns using Python with customizable parameters.

**Usage:**
```bash
python3 tools/pattern_generator.py <pattern> [options]
```

**Available Patterns:**

- **spiral** - Generate spiral patterns
  ```bash
  python3 tools/pattern_generator.py spiral --size 15 --char ★
  ```

- **tree** - Generate fractal trees
  ```bash
  python3 tools/pattern_generator.py tree --depth 5
  ```

- **mandala** - Generate mandala patterns
  ```bash
  python3 tools/pattern_generator.py mandala --rings 7 --points 12
  ```

- **wave** - Generate wave patterns
  ```bash
  python3 tools/pattern_generator.py wave --amplitude 5 --frequency 0.5 --width 60
  ```

- **grid** - Generate grid/tessellation patterns
  ```bash
  python3 tools/pattern_generator.py grid --rows 10 --cols 10 --style box
  ```

- **sierpinski** - Generate Sierpinski triangles
  ```bash
  python3 tools/pattern_generator.py sierpinski --depth 4
  ```

- **diamond** - Generate diamond patterns
  ```bash
  python3 tools/pattern_generator.py diamond --size 9
  ```

**Options:**
- `--size` - Pattern size (default: 10)
- `--depth` - Recursion depth for fractals (default: 5)
- `--rings` - Number of rings for mandala (default: 5)
- `--points` - Points per ring for mandala (default: 8)
- `--amplitude` - Wave amplitude (default: 5)
- `--frequency` - Wave frequency (default: 0.5)
- `--width` - Pattern width (default: 60)
- `--rows` - Grid rows (default: 10)
- `--cols` - Grid columns (default: 10)
- `--style` - Grid style: box or dots (default: box)
- `--char` - Character to use (default: ●)

---

### Node.js Generator (`pattern_generator.js`)

Generate ASCII art patterns using Node.js.

**Usage:**
```bash
node tools/pattern_generator.js <pattern> [options]
```

**Available Patterns:**

- **spiral** - `node tools/pattern_generator.js spiral 15 ★`
- **mandala** - `node tools/pattern_generator.js mandala 7 12`
- **wave** - `node tools/pattern_generator.js wave 5 0.5 60`
- **grid** - `node tools/pattern_generator.js grid 5 5 dots`
- **diamond** - `node tools/pattern_generator.js diamond 9`
- **circle** - `node tools/pattern_generator.js circle 12 ○`
- **labyrinth** - `node tools/pattern_generator.js labyrinth 11`
- **zigzag** - `node tools/pattern_generator.js zigzag 40 10`

**Examples:**
```bash
# Generate a large spiral with stars
node tools/pattern_generator.js spiral 20 ★

# Create a complex mandala
node tools/pattern_generator.js mandala 10 16

# Generate a random labyrinth
node tools/pattern_generator.js labyrinth 15
```

---

## Templates

The `templates/` directory contains blank templates you can fill in to create your own ASCII art:

### Available Templates:

1. **mandala-template.md** - Circular mandala patterns
   - Tips for symmetry and sacred geometry
   - Character suggestions: ●, ○, ◉, ◎, ⊙, ☉

2. **fractal-tree-template.md** - Branching tree structures
   - Instructions for symmetric/asymmetric designs
   - Box-drawing characters: │ ─ ┌ ┐ └ ┘ ├ ┤ ┬ ┴ ┼

3. **maze-template.md** - Labyrinth designs
   - Unicursal, classical, and branching maze types
   - Wall characters: █ ▓ ▒ ░ ║ ═ │ ─

4. **spiral-template.md** - Spiral patterns
   - Archimedean (equal spacing) vs logarithmic (expanding)
   - Direction variations: clockwise, counter-clockwise, double

5. **grid-tessellation-template.md** - Grid and repeating patterns
   - Checkerboard, symbol grids, hexagonal grids
   - Various fill patterns and styles

6. **sacred-geometry-template.md** - Sacred geometric patterns
   - Flower of Life, Vesica Piscis, Merkaba
   - Platonic solids and Metatron's Cube

**How to Use Templates:**
1. Copy a template to your working directory
2. Open in a text editor with monospace font
3. Fill in the pattern following the guidelines
4. Test appearance in terminal or code block

---

## Colored Examples

The `colored-examples/` directory contains scripts that display ASCII art with ANSI terminal colors.

### Python Colors (`ansi_colors.py`)

Display colorful ASCII art examples:

```bash
python3 colored-examples/ansi_colors.py
```

**Features:**
- Colorful mandalas, trees, spirals, and fractals
- Gradient effects
- Chakra symbols with traditional colors
- Full ANSI color palette support

### Node.js Colors (`ansi_colors.js`)

Same functionality in JavaScript:

```bash
node colored-examples/ansi_colors.js
```

**Note:** Colors require an ANSI-compatible terminal (most modern terminals support this).

---

## Tips for Creating ASCII Art

### Character Selection

**Light to Dark:**
```
░ ▒ ▓ █
```

**Circles:**
```
○ ◌ ◯ ⊙ ◉ ● ⊚ ◎
```

**Lines:**
```
│ ║ ─ ═ ╱ ╲ ╳
```

**Box Drawing:**
```
┌ ┐ └ ┘ ├ ┤ ┬ ┴ ┼
╔ ╗ ╚ ╝ ╠ ╣ ╦ ╩ ╬
```

**Geometric:**
```
◆ ◇ ▲ △ ▼ ▽ ◀ ▶ ■ □
```

### Best Practices

1. **Use Monospace Font** - Ensures proper alignment
2. **Test in Terminal** - Preview how it looks in actual use
3. **Consider Width** - Keep lines under 80 characters when possible
4. **Maintain Symmetry** - Use rulers/guides for balanced designs
5. **Save Frequently** - ASCII art can be fragile, save versions
6. **Layer Complexity** - Start simple, add detail gradually

### Resources

- [Unicode Box Drawing Characters](https://en.wikipedia.org/wiki/Box-drawing_character)
- [Unicode Geometric Shapes](https://en.wikipedia.org/wiki/Geometric_Shapes)
- [ANSI Escape Codes](https://en.wikipedia.org/wiki/ANSI_escape_code)

---

## Contributing

Created an interesting pattern? Consider:
1. Adding it to the appropriate hall in the museum
2. Creating a new template for others to use
3. Submitting generator improvements via pull request

See `CONTRIBUTING.md` in the root directory for guidelines.
