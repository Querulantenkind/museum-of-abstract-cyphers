#!/usr/bin/env python3
"""
ASCII Art Pattern Generator
Generate various ASCII art patterns with customizable parameters.
"""

import math
import argparse
from typing import List, Tuple


class PatternGenerator:
    """Generate various ASCII art patterns."""
    
    @staticmethod
    def spiral(size: int = 10, char: str = "●") -> str:
        """Generate a spiral pattern."""
        grid = [[' ' for _ in range(size * 2 + 1)] for _ in range(size * 2 + 1)]
        center_x, center_y = size, size
        
        angle = 0
        radius = 0
        max_radius = size
        
        while radius < max_radius:
            x = int(center_x + radius * math.cos(angle))
            y = int(center_y + radius * math.sin(angle))
            if 0 <= x < len(grid[0]) and 0 <= y < len(grid):
                grid[y][x] = char
            angle += 0.3
            radius += 0.1
        
        return '\n'.join([''.join(row) for row in grid])
    
    @staticmethod
    def fractal_tree(depth: int = 5, branch_angle: float = 30) -> str:
        """Generate a fractal tree pattern."""
        lines = []
        
        def draw_branch(x: float, y: float, angle: float, length: float, level: int):
            if level == 0 or length < 1:
                return
            
            # Calculate end point
            end_x = x + length * math.cos(math.radians(angle))
            end_y = y - length * math.sin(math.radians(angle))
            
            # Store line segment
            lines.append((int(x), int(y), int(end_x), int(end_y)))
            
            # Recursive branches
            new_length = length * 0.7
            draw_branch(end_x, end_y, angle + branch_angle, new_length, level - 1)
            draw_branch(end_x, end_y, angle - branch_angle, new_length, level - 1)
        
        # Start from bottom center
        height = 40
        width = 80
        draw_branch(width // 2, height, 90, 10, depth)
        
        # Create grid
        grid = [[' ' for _ in range(width)] for _ in range(height)]
        
        for x1, y1, x2, y2 in lines:
            if 0 <= x1 < width and 0 <= y1 < height:
                grid[y1][x1] = '│' if abs(x2 - x1) < abs(y2 - y1) else '/'
        
        return '\n'.join([''.join(row) for row in grid])
    
    @staticmethod
    def mandala(rings: int = 5, points: int = 8) -> str:
        """Generate a mandala pattern."""
        size = rings * 4 + 1
        grid = [[' ' for _ in range(size)] for _ in range(size)]
        center = size // 2
        
        for ring in range(1, rings + 1):
            radius = ring * 2
            for i in range(points * ring):
                angle = 2 * math.pi * i / (points * ring)
                x = int(center + radius * math.cos(angle))
                y = int(center + radius * math.sin(angle))
                if 0 <= x < size and 0 <= y < size:
                    if ring % 2 == 0:
                        grid[y][x] = '●'
                    else:
                        grid[y][x] = '○'
        
        # Add center
        grid[center][center] = '◉'
        
        return '\n'.join([''.join(row) for row in grid])
    
    @staticmethod
    def wave(amplitude: int = 5, frequency: float = 0.5, width: int = 60) -> str:
        """Generate a wave pattern."""
        lines = []
        height = amplitude * 2 + 1
        
        for y in range(height):
            line = []
            for x in range(width):
                wave_y = amplitude + amplitude * math.sin(frequency * x)
                if abs(y - wave_y) < 0.5:
                    line.append('~')
                else:
                    line.append(' ')
            lines.append(''.join(line))
        
        return '\n'.join(lines)
    
    @staticmethod
    def grid_pattern(rows: int = 10, cols: int = 10, style: str = "box") -> str:
        """Generate a grid pattern."""
        if style == "box":
            h_line = "─"
            v_line = "│"
            cross = "┼"
            corner_tl = "┌"
            corner_tr = "┐"
            corner_bl = "└"
            corner_br = "┘"
            t_down = "┬"
            t_up = "┴"
            t_right = "├"
            t_left = "┤"
        else:  # dots
            h_line = "·"
            v_line = "·"
            cross = "·"
            corner_tl = corner_tr = corner_bl = corner_br = "·"
            t_down = t_up = t_right = t_left = "·"
        
        lines = []
        cell_width = 3
        
        # Top border
        line = corner_tl
        for col in range(cols):
            line += h_line * cell_width
            line += t_down if col < cols - 1 else corner_tr
        lines.append(line)
        
        # Rows
        for row in range(rows):
            # Cell row
            line = v_line
            for col in range(cols):
                line += " " * cell_width
                line += v_line
            lines.append(line)
            
            # Separator (except after last row)
            if row < rows - 1:
                line = t_right
                for col in range(cols):
                    line += h_line * cell_width
                    line += cross if col < cols - 1 else t_left
                lines.append(line)
        
        # Bottom border
        line = corner_bl
        for col in range(cols):
            line += h_line * cell_width
            line += t_up if col < cols - 1 else corner_br
        lines.append(line)
        
        return '\n'.join(lines)
    
    @staticmethod
    def sierpinski(depth: int = 4) -> str:
        """Generate Sierpinski triangle."""
        size = 2 ** depth
        grid = [[' ' for _ in range(size * 2)] for _ in range(size)]
        
        def draw_triangle(x: int, y: int, size: int):
            if size == 1:
                grid[y][x] = '▲'
                return
            
            half = size // 2
            draw_triangle(x, y, half)  # Top
            draw_triangle(x - half, y + half, half)  # Bottom left
            draw_triangle(x + half, y + half, half)  # Bottom right
        
        draw_triangle(size, 0, size)
        return '\n'.join([''.join(row) for row in grid])
    
    @staticmethod
    def diamond(size: int = 7) -> str:
        """Generate a diamond pattern."""
        lines = []
        
        # Top half (including middle)
        for i in range(size):
            spaces = ' ' * (size - i - 1)
            stars = '◆' * (2 * i + 1)
            lines.append(spaces + stars)
        
        # Bottom half
        for i in range(size - 2, -1, -1):
            spaces = ' ' * (size - i - 1)
            stars = '◆' * (2 * i + 1)
            lines.append(spaces + stars)
        
        return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description='Generate ASCII art patterns')
    parser.add_argument('pattern', choices=[
        'spiral', 'tree', 'mandala', 'wave', 'grid', 'sierpinski', 'diamond'
    ], help='Pattern type to generate')
    parser.add_argument('--size', type=int, default=10, help='Pattern size')
    parser.add_argument('--depth', type=int, default=5, help='Recursion depth (for tree/sierpinski)')
    parser.add_argument('--rings', type=int, default=5, help='Number of rings (for mandala)')
    parser.add_argument('--points', type=int, default=8, help='Points per ring (for mandala)')
    parser.add_argument('--amplitude', type=int, default=5, help='Wave amplitude')
    parser.add_argument('--frequency', type=float, default=0.5, help='Wave frequency')
    parser.add_argument('--width', type=int, default=60, help='Pattern width')
    parser.add_argument('--rows', type=int, default=10, help='Grid rows')
    parser.add_argument('--cols', type=int, default=10, help='Grid columns')
    parser.add_argument('--style', default='box', choices=['box', 'dots'], help='Grid style')
    parser.add_argument('--char', default='●', help='Character to use')
    
    args = parser.parse_args()
    
    generator = PatternGenerator()
    
    if args.pattern == 'spiral':
        print(generator.spiral(args.size, args.char))
    elif args.pattern == 'tree':
        print(generator.fractal_tree(args.depth))
    elif args.pattern == 'mandala':
        print(generator.mandala(args.rings, args.points))
    elif args.pattern == 'wave':
        print(generator.wave(args.amplitude, args.frequency, args.width))
    elif args.pattern == 'grid':
        print(generator.grid_pattern(args.rows, args.cols, args.style))
    elif args.pattern == 'sierpinski':
        print(generator.sierpinski(args.depth))
    elif args.pattern == 'diamond':
        print(generator.diamond(args.size))


if __name__ == '__main__':
    main()
