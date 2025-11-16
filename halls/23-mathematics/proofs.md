# Proof Techniques

Mathematical reasoning visualized.

## Direct Proof

```
  PREMISE
     │
     ↓
  STEP 1
     │
     ↓
  STEP 2
     │
     ↓
  CONCLUSION
```

## Proof by Contradiction

```
  ASSUME ¬P
     │
     ↓
  DERIVE ⊥
     │
     ↓
  CONCLUDE P
```

## Proof by Induction

```
  BASE: P(0)
     │
     ↓
  STEP: P(k)→P(k+1)
     │
     ↓
  ∀n: P(n)
```

## Contrapositive

```
  P → Q
  
  ≡
  
  ¬Q → ¬P
```

## Case Analysis

```
      P
     ╱│╲
    │ │ │
   C1 C2 C3
    │ │ │
    └─┴─┘
      Q
```

## Counterexample

```
  CLAIM: ∀x P(x)
  
  FIND: x₀
  
  ¬P(x₀) → ╳
```

## Construction Proof

```
  EXISTS x: P(x)
  
  BUILD: x₀
     │
     ↓
  VERIFY: P(x₀) ✓
```

## Pigeonhole Principle

```
  N+1 items
  N boxes
  
  ●●●●●
  ├─┤├─┤
  [ONE BOX HAS ≥2]
```

## Diagonalization

```
  a₁₁ a₁₂ a₁₃
  a₂₁ a₂₂ a₂₃
  a₃₁ a₃₂ a₃₃
   ↘   ↘   ↘
  [CONSTRUCT NEW]
```

## Proof by Exhaustion

```
  CHECK ALL:
  
  ●─✓
  ●─✓
  ●─✓
  ●─✓
  [ALL CASES]
```

## Reductio ad Absurdum

```
  ASSUME P
     │
  DERIVE Q
     │
  DERIVE ¬Q
     │
     ⊥
     │
  ∴ ¬P
```

## Combinatorial Proof

```
  COUNT:
     n
  ●──●
     
  SAME AS:
     n
  ●──●
```

## Double Counting

```
  METHOD 1: ●●●●● = 5
            
  METHOD 2: ●●●●● = 5
            
  ∴ EQUAL
```

## Proof by Symmetry

```
    P(x,y)
     ╱╲
    ╱  ╲
  P(y,x)
  [SAME]
```

## Intermediate Value

```
  f(a) < 0
     │
    ╱│╲
   ╱ ● ╲
  │  c  │
  f(b) > 0
```

## Squeeze Theorem

```
  g(x) ≤ f(x) ≤ h(x)
  
  ═══●═══
     │
  ───●───
     │
  ___●___
```

## Proof by Computation

```
  CALCULATE:
  
  ●──→●──→●
  │   │   │
  ✓   ✓   ✓
```

## Existential Proof

```
  ∃x: P(x)
  
  EXHIBIT: x₀
           ●
           │
         P(x₀)
```

## Universal Proof

```
  ∀x: P(x)
  
  LET x arbitrary
      │
      ↓
    P(x)
```

## Probabilistic Proof

```
  Pr[P] > 0
     │
     ↓
  ∃ outcome
  where P holds
```

## Bijective Proof

```
  SET A ↔ SET B
   ●●●  ←→ ●●●
   
  |A| = |B|
```

## Proof by Example

```
  CLAIM: ∃x P(x)
  
  WITNESS: x = 5
           ●
           │
         P(5) ✓
```

## Well-Ordering

```
  S ⊆ ℕ, S ≠ ∅
      │
      ↓
  ∃ min(S)
      ●
```

## Strong Induction

```
  BASE: P(0)
     │
  STEP: P(0)∧...∧P(k) → P(k+1)
     │
     ↓
  ∀n: P(n)
```

## Fixed Point

```
  f(x) = x
     │
     ●
    ╱│╲
   f(●) = ●
```

## Cantor's Diagonal

```
  0.1415...
  0.7182...
  0.6931...
   ↘ ↘ ↘
  CONSTRUCT NEW
```

## Zorn's Lemma

```
  CHAIN:
  a₁ ⊆ a₂ ⊆ a₃ ...
   │    │    │
   └────┴────┘
       ∪
   [MAXIMAL]
```

## Proof by Cases

```
     CLAIM
     ╱  ╲
   C1    C2
   │     │
   Q     Q
   └──┬──┘
      Q
```

## Structural Induction

```
  BASE: atoms
     │
  STEP: compound
     │
     ↓
  ∀ structure
```

## Descending Chain

```
  a₁ ⊇ a₂ ⊇ a₃ ...
   │    │    │
   └────┴────●
     TERMINATE
```

````
```

## Probabilistic Proof

```
  Pr[P] > 0
     │
     ↓
  ∃ outcome
  where P holds
```
