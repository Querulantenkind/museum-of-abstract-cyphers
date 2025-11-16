# Entropy & Information

Measuring disorder and information content.

## Shannon Entropy

```
  H(X) = -Σ p(x)log₂p(x)
  
    HIGH ENTROPY
    ░▒▓█▒░▓▒░█▓
    RANDOM = MORE INFO
    
    LOW ENTROPY
    ████████████
    ORDERED = LESS INFO
```

## Information Content

```
  RARE EVENT:
  ●─────────────
  │ HIGH INFO  │
  └─────────────┘
  
  COMMON EVENT:
  ●─────────────
  │ LOW INFO   │
  └─────────────┘
```

## Compression

```
  BEFORE:
  ●●●●●●●●●●●●
  
  AFTER:
  12×●
  
  [PATTERN = COMPRESSION]
```

## Redundancy

```
  MESSAGE:
  ●─●─●─●─●─●
  │ │ │ │ │ │
  ●─●─●─●─●─●
  [BACKUP INFO]
```

## Noise

```
  SIGNAL:  ───●───●───
           
  NOISE:   ░▒▓█▓▒░▒▓█
           
  RECEIVED: ∿∿●∿∿●∿∿
```

## Channel Capacity

```
  INPUT    CHANNEL    OUTPUT
    ●───────║───────●
    ●───────║───────●
    ●───────║───────●
  [SHANNON LIMIT: C = B log₂(1+S/N)]
```

## Bit Entropy

```
  p=0.5, p=0.5
  ┌─────────┐
  │ 0  │  1 │
  │ ●  │  ● │
  └─────────┘
  H = 1 bit (MAXIMUM)
```

## Kolmogorov Complexity

```
  RANDOM:
  ●░●▓●▒●░●▓●
  K(x) ≈ length
  
  PATTERNED:
  ●●●●●●●●●●●
  K(x) << length
```

## Data Flow

```
  ●──→●──→●──→●
  │    │    │    │
  ↓    ↓    ↓    ↓
  ●──→●──→●──→●
  [INFORMATION PROPAGATION]
```

## Error Correction

```
  SENT:     ●─●─●
  
  ERROR:    ●─X─●
  
  CORRECTED: ●─●─●
  [PARITY CHECK]
```

## Mutual Information

```
  X         Y
  ●─────────●
  │   I(X;Y)│
  ●─────────●
  [SHARED INFO]
```

## Entropy Rate

```
  H(X₁X₂X₃...)
      n
      
  ●→●→●→●→●→●
  [PER SYMBOL]
```

## Code Tree

```
      ROOT
       ●
      ╱ ╲
    0╱   ╲1
    ●     ●
   ╱╲    ╱╲
  0  1  0  1
  ●  ●  ●  ●
[HUFFMAN CODING]
```

## Information Gain

```
  BEFORE:
  ░░░░░░░░
  UNCERTAIN
  
  AFTER:
  ████████
  CERTAIN
  
  ΔH = LEARNED
```

## Surprise

```
  EXPECTED: ●●●●●●●
            │
            [LOW SURPRISE]
  
  UNEXPECTED: ●
              │
              [HIGH SURPRISE]
```

## Redundancy Ratio

```
  ACTUAL:   ●●●●●●●●
            ││││││││
  MINIMUM:  ●●●
            
  R = 1 - 3/8
```

## Cross Entropy

```
  P: ●●●●●●
     ││││││
  Q: ●●●░░░
     
  H(P,Q) > H(P)
```

## Conditional Entropy

```
  H(Y|X)
  
  KNOWN X: ●
           │
           ↓
  Y OPTIONS: ●●●
  [REMAINING UNCERTAINTY]
```

## Relative Entropy

```
  P(x)  Q(x)
   ●     ●
   │     │
  D(P||Q)
  [KL DIVERGENCE]
```

## Source Coding

```
  SOURCE → COMPRESS → TRANSMIT
  
  ●●●●●● → ●●● → ∿∿∿ → ●●●●●●
  
  [LOSSLESS]
```

## Joint Entropy

```
  H(X,Y)
  
  ┌───────────┐
  │ X    XY   │
  │      ╱╲   │
  │     ╱  ╲  │
  │    Y    Z │
  └───────────┘
  [TOTAL UNCERTAINTY]
```

## Information Bottleneck

```
  INPUT      BOTTLENECK    OUTPUT
  ●●●●●●  →    ●●●     →  ●●●●●●
  [COMPRESS]   [KEEP RELEVANT]
```

## Entropy Pool

```
  ░░░░░░░░░░░░
  ░▒▒▒▒▒▒▒▒▒░
  ░▒▓▓▓▓▓▓▓▒░
  ░▒▓█████▓▒░
  ░▒▓▓▓▓▓▓▓▒░
  ░▒▒▒▒▒▒▒▒▒░
  ░░░░░░░░░░░░
  [RANDOMNESS RESERVOIR]
```

## Binary Symmetric Channel

```
  0 ──→ 0 (1-p)
    ╲ ╱
     ╳   p
    ╱ ╲
  1 ──→ 1 (1-p)
  [ERROR PROBABILITY]
```

## Entropy Coding Efficiency

```
  OPTIMAL:  ═══●═══
            H(X)
            
  ACTUAL:   ═══●═══●
            L(C)
            
  η = H(X)/L(C)
```

## Typical Set

```
  ALL SEQUENCES:
  ░░░░░░░░░░░░
  ░▒▒▒▒▒▒▒▒▒░
  
  TYPICAL:
  ░▒▓▓▓▓▓▓▓▒░
  [MOST PROBABLE]
```

## Asymptotic Equipartition

```
  n→∞
  
  ●●●●●●●●●●
  ●●●●●●●●●●
  ●●●●●●●●●●
  
  → 2^(nH) typical
```

## Min-Entropy

```
  H_∞(X) = -log₂(max p(x))
  
  ●●●●●●●●●●█
           ↑
  [MOST LIKELY]
```

## Rényi Entropy

```
  H_α(X) = 1/(1-α) log₂(Σ p^α)
  
  α=0: ●●●●●● (max)
  α=1: ●●●●   (Shannon)
  α=∞: ●●     (min)
```

## Differential Entropy

```
  h(X) = -∫ f(x)log₂f(x)dx
  
      ╱─╲
     ╱   ╲
    ╱     ╲
  ╱________╲
  [CONTINUOUS]
```
