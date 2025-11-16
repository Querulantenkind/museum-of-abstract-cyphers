#!/usr/bin/env python3
"""
ANSI Color Examples for ASCII Art
Display ASCII art with terminal colors using ANSI escape codes.
"""

class Colors:
    """ANSI color codes."""
    # Regular colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    # Bright colors
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'
    
    # Background colors
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'
    
    # Styles
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    
    # Reset
    RESET = '\033[0m'


def colored_mandala():
    """Display a colorful mandala."""
    print(f"\n{Colors.BOLD}Colorful Mandala{Colors.RESET}\n")
    
    mandala = f"""
      {Colors.MAGENTA}○   ○   ○{Colors.RESET}
    {Colors.BLUE}○{Colors.RESET}   {Colors.MAGENTA}○   ○   ○{Colors.RESET}   {Colors.BLUE}○{Colors.RESET}
  {Colors.CYAN}○{Colors.RESET}   {Colors.BLUE}○{Colors.RESET}   {Colors.MAGENTA}○   ○   ○{Colors.RESET}   {Colors.BLUE}○{Colors.RESET}   {Colors.CYAN}○{Colors.RESET}
    {Colors.BLUE}○{Colors.RESET}   {Colors.MAGENTA}○   ○   ○{Colors.RESET}   {Colors.BLUE}○{Colors.RESET}
{Colors.GREEN}○{Colors.RESET}   {Colors.CYAN}○{Colors.RESET}   {Colors.BLUE}○{Colors.RESET}   {Colors.RED}●{Colors.RESET}   {Colors.BLUE}○{Colors.RESET}   {Colors.CYAN}○{Colors.RESET}   {Colors.GREEN}○{Colors.RESET}
    {Colors.BLUE}○{Colors.RESET}   {Colors.MAGENTA}○   ○   ○{Colors.RESET}   {Colors.BLUE}○{Colors.RESET}
  {Colors.CYAN}○{Colors.RESET}   {Colors.BLUE}○{Colors.RESET}   {Colors.MAGENTA}○   ○   ○{Colors.RESET}   {Colors.BLUE}○{Colors.RESET}   {Colors.CYAN}○{Colors.RESET}
    {Colors.BLUE}○{Colors.RESET}   {Colors.MAGENTA}○   ○   ○{Colors.RESET}   {Colors.BLUE}○{Colors.RESET}
      {Colors.MAGENTA}○   ○   ○{Colors.RESET}
"""
    print(mandala)


def colored_tree():
    """Display a colorful tree."""
    print(f"\n{Colors.BOLD}Colorful Tree{Colors.RESET}\n")
    
    tree = f"""
          {Colors.GREEN}●{Colors.RESET}
          {Colors.GREEN}│{Colors.RESET}
      {Colors.GREEN}╱───┴───╲{Colors.RESET}
     {Colors.GREEN}│         │{Colors.RESET}
    {Colors.GREEN}╱╲       ╱╲{Colors.RESET}
   {Colors.GREEN}│  │     │  │{Colors.RESET}
  {Colors.GREEN}╱╲ ╱╲   ╱╲ ╱╲{Colors.RESET}
 {Colors.GREEN}│  │  │ │  │  │{Colors.RESET}
  {Colors.YELLOW}▓▓{Colors.RESET} {Colors.YELLOW}▓▓{Colors.RESET} {Colors.YELLOW}▓▓{Colors.RESET} {Colors.YELLOW}▓▓{Colors.RESET}
    {Colors.RED}█{Colors.BRIGHT_RED}█{Colors.RED}█{Colors.BRIGHT_RED}█{Colors.RED}█{Colors.RESET}
"""
    print(tree)


def colored_spiral():
    """Display a colorful spiral."""
    print(f"\n{Colors.BOLD}Rainbow Spiral{Colors.RESET}\n")
    
    spiral = f"""
        {Colors.MAGENTA}●{Colors.RESET}
      {Colors.MAGENTA}●{Colors.RESET}   {Colors.BLUE}●{Colors.RESET}
    {Colors.MAGENTA}●{Colors.RESET}       {Colors.BLUE}●{Colors.RESET}
  {Colors.RED}●{Colors.RESET}           {Colors.CYAN}●{Colors.RESET}
    {Colors.RED}●{Colors.RESET}       {Colors.CYAN}●{Colors.RESET}
      {Colors.YELLOW}●{Colors.RESET}   {Colors.GREEN}●{Colors.RESET}
        {Colors.YELLOW}●{Colors.RESET}
"""
    print(spiral)


def colored_fractal():
    """Display a colorful fractal."""
    print(f"\n{Colors.BOLD}Sierpinski Triangle (Colored){Colors.RESET}\n")
    
    fractal = f"""
        {Colors.CYAN}▲{Colors.RESET}
       {Colors.CYAN}▲{Colors.RESET} {Colors.CYAN}▲{Colors.RESET}
      {Colors.BLUE}▲{Colors.RESET}   {Colors.BLUE}▲{Colors.RESET}
     {Colors.BLUE}▲{Colors.RESET} {Colors.BLUE}▲{Colors.RESET} {Colors.BLUE}▲{Colors.RESET} {Colors.BLUE}▲{Colors.RESET}
    {Colors.MAGENTA}▲{Colors.RESET}       {Colors.MAGENTA}▲{Colors.RESET}
   {Colors.MAGENTA}▲{Colors.RESET} {Colors.MAGENTA}▲{Colors.RESET}     {Colors.MAGENTA}▲{Colors.RESET} {Colors.MAGENTA}▲{Colors.RESET}
  {Colors.MAGENTA}▲{Colors.RESET}   {Colors.MAGENTA}▲{Colors.RESET}   {Colors.MAGENTA}▲{Colors.RESET}   {Colors.MAGENTA}▲{Colors.RESET}
 {Colors.RED}▲{Colors.RESET} {Colors.RED}▲{Colors.RESET} {Colors.RED}▲{Colors.RESET} {Colors.RED}▲{Colors.RESET} {Colors.RED}▲{Colors.RESET} {Colors.RED}▲{Colors.RESET} {Colors.RED}▲{Colors.RESET} {Colors.RED}▲{Colors.RESET}
"""
    print(fractal)


def colored_flower():
    """Display a colorful flower."""
    print(f"\n{Colors.BOLD}Colorful Flower{Colors.RESET}\n")
    
    flower = f"""
      {Colors.YELLOW}✿{Colors.RESET}
    {Colors.MAGENTA}◉{Colors.RESET} {Colors.YELLOW}●{Colors.RESET} {Colors.MAGENTA}◉{Colors.RESET}
  {Colors.MAGENTA}◉{Colors.RESET}   {Colors.YELLOW}●{Colors.RESET}   {Colors.MAGENTA}◉{Colors.RESET}
    {Colors.MAGENTA}◉{Colors.RESET} {Colors.YELLOW}●{Colors.RESET} {Colors.MAGENTA}◉{Colors.RESET}
      {Colors.GREEN}│{Colors.RESET}
      {Colors.GREEN}│{Colors.RESET}
     {Colors.GREEN}╱{Colors.RESET} {Colors.GREEN}╲{Colors.RESET}
"""
    print(flower)


def colored_labyrinth():
    """Display a colorful labyrinth."""
    print(f"\n{Colors.BOLD}Colorful Labyrinth{Colors.RESET}\n")
    
    labyrinth = f"""
  {Colors.BRIGHT_BLACK}┌─────────────┐{Colors.RESET}
  {Colors.BRIGHT_BLACK}│{Colors.RESET} {Colors.GREEN}▶{Colors.RESET} {Colors.BRIGHT_BLACK}█ █ █ █ █{Colors.RESET} {Colors.BRIGHT_BLACK}│{Colors.RESET}
  {Colors.BRIGHT_BLACK}│{Colors.RESET}   {Colors.BRIGHT_BLACK}█{Colors.RESET}   {Colors.BRIGHT_BLACK}█{Colors.RESET}   {Colors.BRIGHT_BLACK}█{Colors.RESET} {Colors.BRIGHT_BLACK}│{Colors.RESET}
  {Colors.BRIGHT_BLACK}│{Colors.RESET} {Colors.BRIGHT_BLACK}█ █ █{Colors.RESET}   {Colors.BRIGHT_BLACK}█{Colors.RESET} {Colors.BRIGHT_BLACK}█{Colors.RESET} {Colors.BRIGHT_BLACK}│{Colors.RESET}
  {Colors.BRIGHT_BLACK}│{Colors.RESET} {Colors.BRIGHT_BLACK}█{Colors.RESET}     {Colors.BRIGHT_BLACK}█ █{Colors.RESET}   {Colors.BRIGHT_BLACK}│{Colors.RESET}
  {Colors.BRIGHT_BLACK}│{Colors.RESET} {Colors.BRIGHT_BLACK}█ █ █ █{Colors.RESET} {Colors.RED}◎{Colors.RESET} {Colors.BRIGHT_BLACK}█{Colors.RESET} {Colors.BRIGHT_BLACK}│{Colors.RESET}
  {Colors.BRIGHT_BLACK}└─────────────┘{Colors.RESET}
"""
    print(labyrinth)


def gradient_wave():
    """Display a gradient wave."""
    print(f"\n{Colors.BOLD}Gradient Wave{Colors.RESET}\n")
    
    colors = [Colors.RED, Colors.YELLOW, Colors.GREEN, Colors.CYAN, Colors.BLUE, Colors.MAGENTA]
    wave = """
    ╱╲      ╱╲
   ╱  ╲    ╱  ╲
  ╱    ╲  ╱    ╲
 ╱      ╲╱      ╲
"""
    for i, line in enumerate(wave.split('\n')):
        if line:
            color = colors[i % len(colors)]
            print(f"{color}{line}{Colors.RESET}")


def colored_chakras():
    """Display colorful chakras."""
    print(f"\n{Colors.BOLD}Chakra Symbols{Colors.RESET}\n")
    
    chakras = f"""
  {Colors.MAGENTA}◯{Colors.RESET}  Crown
  {Colors.BLUE}◉{Colors.RESET}  Third Eye
  {Colors.CYAN}◎{Colors.RESET}  Throat
  {Colors.GREEN}◈{Colors.RESET}  Heart
  {Colors.YELLOW}◇{Colors.RESET}  Solar Plexus
  {Colors.BRIGHT_YELLOW}◆{Colors.RESET}  Sacral
  {Colors.RED}●{Colors.RESET}  Root
"""
    print(chakras)


def main():
    """Display all colored examples."""
    print(f"\n{Colors.BOLD}{Colors.BRIGHT_CYAN}╔════════════════════════════════════╗{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BRIGHT_CYAN}║  ASCII Art with ANSI Colors Demo  ║{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BRIGHT_CYAN}╚════════════════════════════════════╝{Colors.RESET}")
    
    colored_mandala()
    colored_tree()
    colored_spiral()
    colored_fractal()
    colored_flower()
    colored_labyrinth()
    gradient_wave()
    colored_chakras()
    
    print(f"\n{Colors.DIM}Note: Colors require ANSI-compatible terminal{Colors.RESET}\n")


if __name__ == '__main__':
    main()
