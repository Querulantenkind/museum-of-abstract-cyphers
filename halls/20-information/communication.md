# Communication Theory

Transmitting information reliably.

## Channel Model

```
  SOURCE → ENCODER → CHANNEL → DECODER → DEST
    ●         ●         ║         ●       ●
             noise ↓    ║
```

## Signal to Noise

```
  SIGNAL:  ───●───●───
           
  NOISE:   ∿∿∿∿∿∿∿∿∿∿
           
  SNR = S/N (dB)
```

## Modulation

```
  CARRIER: ∿∿∿∿∿∿∿∿
           
  DATA:    ●─●─●─●
           
  MODULATED: ∿●∿●∿●∿
```

## Bandwidth

```
  NARROW:  │
           │●│
           │
           
  WIDE:    │
         ●●●●●
           │
```

## Multiplexing

```
  A: ●──┐
  B: ●──┤
  C: ●──┼──→ ●●●
  D: ●──┤
  E: ●──┘
  [COMBINE]
```

## Demultiplexing

```
  ●●●●●──┬──→ ●
         ├──→ ●
         ├──→ ●
         ├──→ ●
         └──→ ●
  [SEPARATE]
```

## Error Detection

```
  DATA:   ●─●─●
          │ │ │
  PARITY: ●─●─●─●
              ↑
          [CHECK BIT]
```

## Hamming Distance

```
  A: ●●●○○
  B: ●○●●○
     ╲│╱
  d=2 bits differ
```

## Forward Error Correction

```
  SEND: ●●● + redundancy
        │││   ▓▓▓
        
  RECEIVE: ●X● ▓▓▓
           ↓   ↓
  CORRECT: ●●●
```

## Interleaving

```
  DATA:   123 456 789
          ↓↓↓ ↓↓↓ ↓↓↓
  BURST:  147 258 369
  
  [SPREAD ERRORS]
```

## Constellation Diagram

```
      Q
      │ ●   ●
      │
  ────┼──── I
      │
      │ ●   ●
  [QAM]
```

## Frequency Hopping

```
  f₃: ─●───●─
  f₂: ───●───●
  f₁: ●───●───
      TIME →
```

## Spread Spectrum

```
  NARROW: │●│
          
  SPREAD: ●●●●●●●
          
  [WIDER BAND]
```

## Packet Structure

```
  ┌──────┬──────┬──────┬──────┐
  │HEADER│ DATA │ DATA │ CRC  │
  └──────┴──────┴──────┴──────┘
```

## Flow Control

```
  SENDER      RECEIVER
    ●──────→●
    │←──ACK─┤
    ●──────→●
    │←──ACK─┤
```

## Congestion

```
  ●●●●●●●●
   ╲│╱│╲│╱
    ╲│╱│╱
     ╲│╱
      ●
  [BOTTLENECK]
```

## Routing

```
      ●
     ╱│╲
    ● ● ●
   ╱ ╲│╱ ╲
  ●───●───●
  [FIND PATH]
```

## Handshake

```
  A → B: SYN
  B → A: SYN-ACK
  A → B: ACK
  
  ●──→●
  ●←──●
  ●──→●
```

## Duplex

```
  HALF:  ●──→●
         ●←──●
         
  FULL:  ●⇄●
```

## Protocol Stack

```
  ╔══════════╗ APP
  ╠══════════╣ TRANSPORT
  ╠══════════╣ NETWORK
  ╠══════════╣ LINK
  ╚══════════╝ PHYSICAL
```
