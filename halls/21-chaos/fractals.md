# Fractal Dimensions

Non-integer dimensions in chaotic systems.

## Cantor Set

```
  ██████████
  ███░░░███
  ██░█░█░██
  █░██░██░█
  [D ≈ 0.631]
```

## Koch Curve

```
      ╱╲
     ╱  ╲
    ╱╲  ╱╲
   ╱  ╲╱  ╲
  ╱╲  ╱╲  ╱╲
[D ≈ 1.262]
```

## Sierpiński Triangle

```
      ▲
     ▲ ▲
    ▲   ▲
   ▲ ▲ ▲ ▲
  ▲   ▲   ▲
 ▲ ▲ ▲ ▲ ▲ ▲
[D ≈ 1.585]
```

## Menger Sponge

```
  ███████
  █░░░░░█
  █░███░█
  █░█░█░█
  █░███░█
  █░░░░░█
  ███████
[D ≈ 2.727]
```

## Dragon Curve

```
    ╱─╲
   ╱   ╲
  │ ╱─╲ │
   ╲│ │╱
    ╲─╱
[D ≈ 1.5]
```

## Lévy C Curve

```
    ╱╲
   ╱  ╲
  │╱╲╱╲│
   ╲╱╲╱
[D ≈ 1.934]
```

## Minkowski Sausage

```
  ██╱╲██
  █╱╲╱╲█
  ╱╲██╱╲
  ╲╱██╲╱
[D ≈ 1.5]
```

## Hilbert Curve

```
  ╱─╲─╮
  │ ╱╯ │
  ├─╮╱─┤
  │ ╰─╮│
  ╰─╯ ╰╯
[D = 2]
```

## Box-Counting

```
  ┌─┬─┬─┐
  │●│●│ │
  ├─┼─┼─┤
  │●│●│●│
  ├─┼─┼─┤
  │ │●│●│
  └─┴─┴─┘
[COUNT BOXES]
```

## Hausdorff Dimension

```
  D = log(N)/log(1/r)
  
  N: copies
  r: scale
  
  ●──→●●
       ││
       ●●
```

## Fractal Coastline

```
  ∿∿∿∿∿∿∿
  ∿░∿░∿░∿
  ░∿░∿░∿░
[INFINITE LENGTH]
```

## Self-Similarity

```
    ●
   ╱│╲
  ● ● ●
  │ │ │
  ●─●─●
[SCALE INVARIANT]
```

## Capacity Dimension

```
  D_C = lim[log(N(ε))/log(1/ε)]
        ε→0
  
  ε: box size
  N: count
```

## Information Dimension

```
  D_I = lim[Σ p_i log(p_i)/log(ε)]
        ε→0
  
  [WEIGHTED]
```

## Correlation Dimension

```
  D_C = lim[log(C(r))/log(r)]
        r→0
  
  ●─●─●
  │╲│╱│
  ●─●─●
```

## Mandelbrot Perimeter

```
   ●●●●●
  ●░░░░●
  ●░▒▒░●
  ●░▒▒░●
  ●░░░░●
   ●●●●●
[D ≈ 2]
```

## Fractal Basin

```
  ●●●○○○
  ●●○○○○
  ●○○░○○
  ○○░░░○
  ○○○░░○
[BOUNDARY D > 1]
```

## Devil's Staircase

```
  ───┐
     │
     ├─┐
     │ │
     │ ├┐
     │ ││
[CANTOR FUNCTION]
```

## Multifractal

```
  ██░▒▓█▓▒░
  [VARYING D]
  
  D(q) varies
```

## Strange Attractor Dimension

```
  ●●●●●●
  ●░░░░●
  ●░▒▒░●
  ●░▒●░●
  ●░░░░●
  ●●●●●●
[D ≈ 2.06]
```
