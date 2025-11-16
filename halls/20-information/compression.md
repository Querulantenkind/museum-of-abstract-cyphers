# Data Compression

Making information smaller.

## Run-Length Encoding

```
  INPUT:  ████░░░░░██
  
  OUTPUT: 4█ 5░ 2█
  
  [COUNT + SYMBOL]
```

## Huffman Tree

```
        ╔═══╗
        ║ * ║ 1.0
        ╚═╤═╝
      ╔═══╧═══╗
    0.6║     ║0.4
    ╔═╧═╗ ╔═╧═╗
    ║ A ║ ║ * ║
    ╚═══╝ ╚═╤═╝
        0.2║ ║0.2
        ╔═╧╗╔╧═╗
        ║B║║C║
        ╚═╝╚═╝
```

## Dictionary Coding

```
  DICTIONARY:
  ┌─────────┐
  │ 1: THE  │
  │ 2: AND  │
  │ 3: FOR  │
  └─────────┘
  
  TEXT: 1 cat 2 dog
```

## Lempel-Ziv

```
  ●●●●▓▓▓▓●●●●
      ↑   ↑
      └───┘
    [BACK REFERENCE]
```

## Arithmetic Coding

```
  [0.0 ─────────── 1.0]
  │  A  │ B │  C  │
  0.0  0.6 0.8  1.0
  
  ENCODE: 0.xxxxx
```

## Delta Encoding

```
  VALUES: 100,102,105,103
  
  DELTAS:  +2 +3  -2
  
  ●──→●──→●──→●
```

## Quantization

```
  CONTINUOUS:
  ░▒▓█▓▒░▒▓█
  
  QUANTIZED:
  ░░▓▓▓▓░░▓▓
  [LEVELS: 4]
```

## Burrows-Wheeler

```
  ORIGINAL:
  BANANA
  
  TRANSFORM:
  ANNBAA
  
  [EASIER TO COMPRESS]
```

## Move-to-Front

```
  LIST: [A,B,C,D]
  
  INPUT: B
  
  LIST: [B,A,C,D]
  OUTPUT: 1
```

## Prediction

```
  PAST:   ●─●─●
          │ │ │
  PREDICT:   ●?
  
  ERROR: actual - predicted
```

## Bit Packing

```
  8-BIT:  ●●●●●●●●
  
  3-BIT:  ●●● ●●● ●●
  
  [FEWER BITS]
```

## Zero Suppression

```
  DATA: 000●0●●000
  
  COMPRESSED: ●_●●
  
  [REMOVE ZEROS]
```

## Pattern Matching

```
  TEXT:  ●●●▓▓●●●▓▓
         └──┬──┘
    MATCH: ▓▓
```

## Golomb Coding

```
  n = qM + r
  
  q: ●●●●●0
  r: ●●
  
  [OPTIMAL FOR GEOMETRIC]
```

## Context Modeling

```
  CONTEXT: ●●●
           │
           ↓
  PREDICT: ●?
  
  [PROBABILITY]
```

## Adaptive Coding

```
  ●──→ UPDATE
  │    MODEL
  ↓      ↓
  ●──→ ENCODE
  
  [LEARNS]
```

## Wavelet Transform

```
  SIGNAL:  ∿∿∿∿∿∿
           ↓
  COEFFS: ●░░●░░
  
  [MULTI-SCALE]
```

## Entropy Coding

```
  HIGH PROB: 0
  MED PROB:  10
  LOW PROB:  110
  RARE:      111
```

## Lossy Compression

```
  ORIGINAL:  ●●●●●●
             │││││
  COMPRESSED: ●●●
  
  [INFORMATION LOST]
```

## Frame Differencing

```
  FRAME 1: ████
           ↓
  FRAME 2: ██▓▓
           
  DELTA:   00●●
```

## Variable Length Codes

```
  SHORT: A → 0
  MED:   B → 10
  LONG:  C → 110
  LONGER: D → 1110
  
  [FREQUENT = SHORT]
```

## Block Coding

```
  ┌────┬────┬────┐
  │ A1 │ B1 │ C1 │
  ├────┼────┼────┤
  │ A2 │ B2 │ C2 │
  ├────┼────┼────┤
  │ A3 │ B3 │ C3 │
  └────┴────┴────┘
  [PROCESS TOGETHER]
```

## Adaptive Dictionary

```
  T=0: [A,B,C]
  
  USE A → MOVE FRONT
  
  T=1: [A,B,C]
  
  [UPDATES]
```

## Subsampling

```
  FULL: ●●●●●●●●
        ││││││││
        
  HALF: ●_●_●_●_
        
  [REDUCE RATE]
```

## Predictive Coding

```
  PREDICT: ●̂
           │
  ACTUAL:  ●
           │
  ERROR: ε = ● - ●̂
  
  [ENCODE ERROR]
```

## Transform Coding

```
  SPATIAL:
  ●●●●
  ●●●●
  
  ↓ DCT
  
  FREQUENCY:
  █░░░
  ░░░░
```

## Entropy Encoding

```
  SYMBOL   PROB   CODE
    A      0.5    0
    B      0.25   10
    C      0.125  110
    D      0.125  111
```

## Range Encoding

```
  [0.0 ──────────── 1.0]
  │    A   │  B  │ C │
  0.0    0.5   0.75 1.0
  
  [NARROWING RANGE]
```

## Fractal Compression

```
    ●●●●
   ●░░░●
  ●░▒▒░●
  ●░▒▒░●
   ●░░░●
    ●●●●
  [SELF-SIMILAR]
```

## Sparse Coding

```
  DENSE:  ●●●●●●
          
  SPARSE: ●__●__●
  
  [FEW NON-ZERO]
```
