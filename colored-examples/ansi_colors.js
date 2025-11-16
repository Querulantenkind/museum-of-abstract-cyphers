#!/usr/bin/env node

/**
 * ANSI Color Examples for ASCII Art (Node.js)
 * Display ASCII art with terminal colors using ANSI escape codes.
 */

const Colors = {
  // Regular colors
  black: '\x1b[30m',
  red: '\x1b[31m',
  green: '\x1b[32m',
  yellow: '\x1b[33m',
  blue: '\x1b[34m',
  magenta: '\x1b[35m',
  cyan: '\x1b[36m',
  white: '\x1b[37m',
  
  // Bright colors
  brightBlack: '\x1b[90m',
  brightRed: '\x1b[91m',
  brightGreen: '\x1b[92m',
  brightYellow: '\x1b[93m',
  brightBlue: '\x1b[94m',
  brightMagenta: '\x1b[95m',
  brightCyan: '\x1b[96m',
  brightWhite: '\x1b[97m',
  
  // Styles
  bold: '\x1b[1m',
  dim: '\x1b[2m',
  italic: '\x1b[3m',
  underline: '\x1b[4m',
  
  // Reset
  reset: '\x1b[0m'
};

function coloredMandala() {
  console.log(`\n${Colors.bold}Colorful Mandala${Colors.reset}\n`);
  
  const mandala = `
      ${Colors.magenta}○   ○   ○${Colors.reset}
    ${Colors.blue}○${Colors.reset}   ${Colors.magenta}○   ○   ○${Colors.reset}   ${Colors.blue}○${Colors.reset}
  ${Colors.cyan}○${Colors.reset}   ${Colors.blue}○${Colors.reset}   ${Colors.magenta}○   ○   ○${Colors.reset}   ${Colors.blue}○${Colors.reset}   ${Colors.cyan}○${Colors.reset}
    ${Colors.blue}○${Colors.reset}   ${Colors.magenta}○   ○   ○${Colors.reset}   ${Colors.blue}○${Colors.reset}
${Colors.green}○${Colors.reset}   ${Colors.cyan}○${Colors.reset}   ${Colors.blue}○${Colors.reset}   ${Colors.red}●${Colors.reset}   ${Colors.blue}○${Colors.reset}   ${Colors.cyan}○${Colors.reset}   ${Colors.green}○${Colors.reset}
    ${Colors.blue}○${Colors.reset}   ${Colors.magenta}○   ○   ○${Colors.reset}   ${Colors.blue}○${Colors.reset}
  ${Colors.cyan}○${Colors.reset}   ${Colors.blue}○${Colors.reset}   ${Colors.magenta}○   ○   ○${Colors.reset}   ${Colors.blue}○${Colors.reset}   ${Colors.cyan}○${Colors.reset}
    ${Colors.blue}○${Colors.reset}   ${Colors.magenta}○   ○   ○${Colors.reset}   ${Colors.blue}○${Colors.reset}
      ${Colors.magenta}○   ○   ○${Colors.reset}
`;
  console.log(mandala);
}

function coloredTree() {
  console.log(`\n${Colors.bold}Colorful Tree${Colors.reset}\n`);
  
  const tree = `
          ${Colors.green}●${Colors.reset}
          ${Colors.green}│${Colors.reset}
      ${Colors.green}╱───┴───╲${Colors.reset}
     ${Colors.green}│         │${Colors.reset}
    ${Colors.green}╱╲       ╱╲${Colors.reset}
   ${Colors.green}│  │     │  │${Colors.reset}
  ${Colors.green}╱╲ ╱╲   ╱╲ ╱╲${Colors.reset}
 ${Colors.green}│  │  │ │  │  │${Colors.reset}
  ${Colors.yellow}▓▓${Colors.reset} ${Colors.yellow}▓▓${Colors.reset} ${Colors.yellow}▓▓${Colors.reset} ${Colors.yellow}▓▓${Colors.reset}
    ${Colors.red}█${Colors.brightRed}█${Colors.red}█${Colors.brightRed}█${Colors.red}█${Colors.reset}
`;
  console.log(tree);
}

function coloredSpiral() {
  console.log(`\n${Colors.bold}Rainbow Spiral${Colors.reset}\n`);
  
  const spiral = `
        ${Colors.magenta}●${Colors.reset}
      ${Colors.magenta}●${Colors.reset}   ${Colors.blue}●${Colors.reset}
    ${Colors.magenta}●${Colors.reset}       ${Colors.blue}●${Colors.reset}
  ${Colors.red}●${Colors.reset}           ${Colors.cyan}●${Colors.reset}
    ${Colors.red}●${Colors.reset}       ${Colors.cyan}●${Colors.reset}
      ${Colors.yellow}●${Colors.reset}   ${Colors.green}●${Colors.reset}
        ${Colors.yellow}●${Colors.reset}
`;
  console.log(spiral);
}

function coloredFractal() {
  console.log(`\n${Colors.bold}Sierpinski Triangle (Colored)${Colors.reset}\n`);
  
  const fractal = `
        ${Colors.cyan}▲${Colors.reset}
       ${Colors.cyan}▲${Colors.reset} ${Colors.cyan}▲${Colors.reset}
      ${Colors.blue}▲${Colors.reset}   ${Colors.blue}▲${Colors.reset}
     ${Colors.blue}▲${Colors.reset} ${Colors.blue}▲${Colors.reset} ${Colors.blue}▲${Colors.reset} ${Colors.blue}▲${Colors.reset}
    ${Colors.magenta}▲${Colors.reset}       ${Colors.magenta}▲${Colors.reset}
   ${Colors.magenta}▲${Colors.reset} ${Colors.magenta}▲${Colors.reset}     ${Colors.magenta}▲${Colors.reset} ${Colors.magenta}▲${Colors.reset}
  ${Colors.magenta}▲${Colors.reset}   ${Colors.magenta}▲${Colors.reset}   ${Colors.magenta}▲${Colors.reset}   ${Colors.magenta}▲${Colors.reset}
 ${Colors.red}▲${Colors.reset} ${Colors.red}▲${Colors.reset} ${Colors.red}▲${Colors.reset} ${Colors.red}▲${Colors.reset} ${Colors.red}▲${Colors.reset} ${Colors.red}▲${Colors.reset} ${Colors.red}▲${Colors.reset} ${Colors.red}▲${Colors.reset}
`;
  console.log(fractal);
}

function gradientWave() {
  console.log(`\n${Colors.bold}Gradient Wave${Colors.reset}\n`);
  
  const colors = [Colors.red, Colors.yellow, Colors.green, Colors.cyan, Colors.blue, Colors.magenta];
  const wave = [
    '    ╱╲      ╱╲',
    '   ╱  ╲    ╱  ╲',
    '  ╱    ╲  ╱    ╲',
    ' ╱      ╲╱      ╲'
  ];
  
  wave.forEach((line, i) => {
    const color = colors[i % colors.length];
    console.log(`${color}${line}${Colors.reset}`);
  });
  console.log();
}

function coloredChakras() {
  console.log(`\n${Colors.bold}Chakra Symbols${Colors.reset}\n`);
  
  const chakras = `
  ${Colors.magenta}◯${Colors.reset}  Crown
  ${Colors.blue}◉${Colors.reset}  Third Eye
  ${Colors.cyan}◎${Colors.reset}  Throat
  ${Colors.green}◈${Colors.reset}  Heart
  ${Colors.yellow}◇${Colors.reset}  Solar Plexus
  ${Colors.brightYellow}◆${Colors.reset}  Sacral
  ${Colors.red}●${Colors.reset}  Root
`;
  console.log(chakras);
}

function main() {
  console.log(`\n${Colors.bold}${Colors.brightCyan}╔════════════════════════════════════╗${Colors.reset}`);
  console.log(`${Colors.bold}${Colors.brightCyan}║  ASCII Art with ANSI Colors Demo  ║${Colors.reset}`);
  console.log(`${Colors.bold}${Colors.brightCyan}╚════════════════════════════════════╝${Colors.reset}`);
  
  coloredMandala();
  coloredTree();
  coloredSpiral();
  coloredFractal();
  gradientWave();
  coloredChakras();
  
  console.log(`${Colors.dim}Note: Colors require ANSI-compatible terminal${Colors.reset}\n`);
}

if (require.main === module) {
  main();
}

module.exports = { Colors };
