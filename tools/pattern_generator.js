#!/usr/bin/env node

/**
 * ASCII Art Pattern Generator (Node.js)
 * Generate various ASCII art patterns with customizable parameters.
 */

class PatternGenerator {
  /**
   * Generate a spiral pattern
   */
  static spiral(size = 10, char = '●') {
    const gridSize = size * 2 + 1;
    const grid = Array(gridSize).fill().map(() => Array(gridSize).fill(' '));
    const centerX = size, centerY = size;
    
    let angle = 0;
    let radius = 0;
    const maxRadius = size;
    
    while (radius < maxRadius) {
      const x = Math.floor(centerX + radius * Math.cos(angle));
      const y = Math.floor(centerY + radius * Math.sin(angle));
      if (x >= 0 && x < gridSize && y >= 0 && y < gridSize) {
        grid[y][x] = char;
      }
      angle += 0.3;
      radius += 0.1;
    }
    
    return grid.map(row => row.join('')).join('\n');
  }

  /**
   * Generate a mandala pattern
   */
  static mandala(rings = 5, points = 8) {
    const size = rings * 4 + 1;
    const grid = Array(size).fill().map(() => Array(size).fill(' '));
    const center = Math.floor(size / 2);
    
    for (let ring = 1; ring <= rings; ring++) {
      const radius = ring * 2;
      for (let i = 0; i < points * ring; i++) {
        const angle = 2 * Math.PI * i / (points * ring);
        const x = Math.floor(center + radius * Math.cos(angle));
        const y = Math.floor(center + radius * Math.sin(angle));
        if (x >= 0 && x < size && y >= 0 && y < size) {
          grid[y][x] = ring % 2 === 0 ? '●' : '○';
        }
      }
    }
    
    grid[center][center] = '◉';
    return grid.map(row => row.join('')).join('\n');
  }

  /**
   * Generate a wave pattern
   */
  static wave(amplitude = 5, frequency = 0.5, width = 60) {
    const height = amplitude * 2 + 1;
    const lines = [];
    
    for (let y = 0; y < height; y++) {
      let line = '';
      for (let x = 0; x < width; x++) {
        const waveY = amplitude + amplitude * Math.sin(frequency * x);
        if (Math.abs(y - waveY) < 0.5) {
          line += '~';
        } else {
          line += ' ';
        }
      }
      lines.push(line);
    }
    
    return lines.join('\n');
  }

  /**
   * Generate a grid pattern
   */
  static grid(rows = 10, cols = 10, style = 'box') {
    const chars = style === 'box' ? {
      h: '─', v: '│', cross: '┼',
      tl: '┌', tr: '┐', bl: '└', br: '┘',
      tDown: '┬', tUp: '┴', tRight: '├', tLeft: '┤'
    } : {
      h: '·', v: '·', cross: '·',
      tl: '·', tr: '·', bl: '·', br: '·',
      tDown: '·', tUp: '·', tRight: '·', tLeft: '·'
    };
    
    const lines = [];
    const cellWidth = 3;
    
    // Top border
    let line = chars.tl;
    for (let col = 0; col < cols; col++) {
      line += chars.h.repeat(cellWidth);
      line += col < cols - 1 ? chars.tDown : chars.tr;
    }
    lines.push(line);
    
    // Rows
    for (let row = 0; row < rows; row++) {
      // Cell row
      line = chars.v;
      for (let col = 0; col < cols; col++) {
        line += ' '.repeat(cellWidth) + chars.v;
      }
      lines.push(line);
      
      // Separator
      if (row < rows - 1) {
        line = chars.tRight;
        for (let col = 0; col < cols; col++) {
          line += chars.h.repeat(cellWidth);
          line += col < cols - 1 ? chars.cross : chars.tLeft;
        }
        lines.push(line);
      }
    }
    
    // Bottom border
    line = chars.bl;
    for (let col = 0; col < cols; col++) {
      line += chars.h.repeat(cellWidth);
      line += col < cols - 1 ? chars.tUp : chars.br;
    }
    lines.push(line);
    
    return lines.join('\n');
  }

  /**
   * Generate a diamond pattern
   */
  static diamond(size = 7) {
    const lines = [];
    
    // Top half
    for (let i = 0; i < size; i++) {
      const spaces = ' '.repeat(size - i - 1);
      const stars = '◆'.repeat(2 * i + 1);
      lines.push(spaces + stars);
    }
    
    // Bottom half
    for (let i = size - 2; i >= 0; i--) {
      const spaces = ' '.repeat(size - i - 1);
      const stars = '◆'.repeat(2 * i + 1);
      lines.push(spaces + stars);
    }
    
    return lines.join('\n');
  }

  /**
   * Generate a circular pattern
   */
  static circle(radius = 10, char = '○') {
    const size = radius * 2 + 1;
    const grid = Array(size).fill().map(() => Array(size).fill(' '));
    const center = radius;
    
    for (let y = 0; y < size; y++) {
      for (let x = 0; x < size; x++) {
        const distance = Math.sqrt((x - center) ** 2 + (y - center) ** 2);
        if (Math.abs(distance - radius) < 0.7) {
          grid[y][x] = char;
        }
      }
    }
    
    return grid.map(row => row.join('')).join('\n');
  }

  /**
   * Generate a labyrinth pattern
   */
  static labyrinth(size = 9) {
    const grid = Array(size).fill().map(() => Array(size).fill('█'));
    
    // Simple maze generation
    function carve(x, y) {
      grid[y][x] = ' ';
      const dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]];
      
      // Shuffle directions
      for (let i = dirs.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [dirs[i], dirs[j]] = [dirs[j], dirs[i]];
      }
      
      for (const [dx, dy] of dirs) {
        const nx = x + dx * 2;
        const ny = y + dy * 2;
        if (nx > 0 && nx < size - 1 && ny > 0 && ny < size - 1 && grid[ny][nx] === '█') {
          grid[y + dy][x + dx] = ' ';
          carve(nx, ny);
        }
      }
    }
    
    carve(1, 1);
    return grid.map(row => row.join('')).join('\n');
  }

  /**
   * Generate a zigzag pattern
   */
  static zigzag(width = 40, height = 10) {
    const lines = [];
    for (let y = 0; y < height; y++) {
      let line = '';
      for (let x = 0; x < width; x++) {
        const pattern = Math.floor(x / 3) % 2;
        if ((y % 4 === 0 && pattern === 0) || (y % 4 === 2 && pattern === 1)) {
          line += '╱';
        } else if ((y % 4 === 0 && pattern === 1) || (y % 4 === 2 && pattern === 0)) {
          line += '╲';
        } else {
          line += ' ';
        }
      }
      lines.push(line);
    }
    return lines.join('\n');
  }
}

// CLI Interface
function main() {
  const args = process.argv.slice(2);
  
  if (args.length === 0) {
    console.log('ASCII Art Pattern Generator');
    console.log('\nUsage: node pattern_generator.js <pattern> [options]');
    console.log('\nPatterns:');
    console.log('  spiral [size] [char]        - Generate spiral (default: 10, ●)');
    console.log('  mandala [rings] [points]    - Generate mandala (default: 5, 8)');
    console.log('  wave [amp] [freq] [width]   - Generate wave (default: 5, 0.5, 60)');
    console.log('  grid [rows] [cols] [style]  - Generate grid (default: 10, 10, box)');
    console.log('  diamond [size]              - Generate diamond (default: 7)');
    console.log('  circle [radius] [char]      - Generate circle (default: 10, ○)');
    console.log('  labyrinth [size]            - Generate labyrinth (default: 9)');
    console.log('  zigzag [width] [height]     - Generate zigzag (default: 40, 10)');
    console.log('\nExamples:');
    console.log('  node pattern_generator.js spiral 15 ★');
    console.log('  node pattern_generator.js mandala 7 12');
    console.log('  node pattern_generator.js grid 5 5 dots');
    return;
  }

  const pattern = args[0];

  try {
    switch (pattern) {
      case 'spiral':
        console.log(PatternGenerator.spiral(
          parseInt(args[1]) || 10,
          args[2] || '●'
        ));
        break;
      case 'mandala':
        console.log(PatternGenerator.mandala(
          parseInt(args[1]) || 5,
          parseInt(args[2]) || 8
        ));
        break;
      case 'wave':
        console.log(PatternGenerator.wave(
          parseInt(args[1]) || 5,
          parseFloat(args[2]) || 0.5,
          parseInt(args[3]) || 60
        ));
        break;
      case 'grid':
        console.log(PatternGenerator.grid(
          parseInt(args[1]) || 10,
          parseInt(args[2]) || 10,
          args[3] || 'box'
        ));
        break;
      case 'diamond':
        console.log(PatternGenerator.diamond(parseInt(args[1]) || 7));
        break;
      case 'circle':
        console.log(PatternGenerator.circle(
          parseInt(args[1]) || 10,
          args[2] || '○'
        ));
        break;
      case 'labyrinth':
        console.log(PatternGenerator.labyrinth(parseInt(args[1]) || 9));
        break;
      case 'zigzag':
        console.log(PatternGenerator.zigzag(
          parseInt(args[1]) || 40,
          parseInt(args[2]) || 10
        ));
        break;
      default:
        console.error(`Unknown pattern: ${pattern}`);
        process.exit(1);
    }
  } catch (error) {
    console.error('Error generating pattern:', error.message);
    process.exit(1);
  }
}

if (require.main === module) {
  main();
}

module.exports = PatternGenerator;
