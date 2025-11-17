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

## Time Division Multiplexing

```
  A: ●__●__●__
  B: _●__●__●_
  C: __●__●__●
  
  MUX: ●●●●●●●●●
```

## Frequency Division

```
  f₃: ──A──A──
  f₂: ──B──B──
  f₁: ──C──C──
  [SEPARATE BANDS]
```

## ARQ Protocol

```
  SEND: ●──→
  
  ERROR: ×←──
  
  RESEND: ●──→
  
  ACK: ✓←──
```

## Sliding Window

```
  [●●●●____]
   ↑  ↑
   SEND ACK
   
  [_●●●●___]
   [ADVANCE]
```

## CSMA/CD

```
  LISTEN: ∿∿∿∿
          │
  COLLISION: ╳
          │
  BACKOFF: ⏸
          │
  RETRY: ●──→
```

## Echo Cancellation

```
  SEND:     ●──→
  
  ECHO:     ●←──
  
  SUBTRACT: ●─●=0
```

## Equalization

```
  INPUT:  ∿∿∿∿∿
          ↓
  FILTER: ▓▓▓
          ↓
  OUTPUT: ═══
  [FLATTEN]
```

## Trellis Coding

```
      ●
     ╱│╲
    ● ● ●
   ╱│X│X│╲
  ● ● ● ● ●
  [STATES]
```

## Cyclic Redundancy Check

```
  DATA: ●●●●●●
        │││││
  POLY: 1011
        ↓
  CRC:  ●●●
```

## Packet Switching

```
  ●─┐ ┌─●
    ├─┤
  ●─┘ └─●
  [SHARED PATH]
```

## Shannon's Theorem

```
  C = B log₂(1 + S/N)
  
  ┌────────────┐
  │ CAPACITY  │
  │    =      │
  │ BANDWIDTH │
  │    ×      │
  │   LOG₂    │
  │    SNR    │
  └────────────┘
```

## Nyquist Sampling

```
  SIGNAL:  ∿∿∿∿∿
           │ │ │
  SAMPLE:  ● ● ●
           
  fs ≥ 2×fmax
```

## Quantization

```
  ANALOG:  ∿∿∿∿
           ├─┤
  DIGITAL: ███
           
  [STEPS]
```

## Differential Encoding

```
  DATA:    ●─●─●─●
           ╲ ╱ ╲ ╱
  ENCODED: ─●─●─●─
  [XOR WITH PREV]
```

## Manchester Encoding

```
  0: ╲╱
  1: ╱╲
  
  DATA: 1 0 1 1
  WAVE: ╱╲╲╱╱╲╱╲
```

## Pulse Code Modulation

```
      ∿∿∿
     ↓ ↓ ↓
  3: █   █
  2: █ █ █
  1: █ █ █
  0: █ █ █
```

## Adaptive Modulation

```
  GOOD SNR:  ●●●●
             [64-QAM]
             
  POOR SNR:  ●  ●
             [QPSK]
```

## Network Topology

```
  STAR:    ●─●─●
             │
             
  RING:   ●─●─●
          │   │
          ●───●
          
  MESH:   ●─●─●
          ├╳├╳├
          ●─●─●
```

## Quality of Service

```
  HIGH: ●●●●●●●●
        ↓
  [PRIORITIZE]
        ↓
  LOW:  ●  ●  ●
```

## Beamforming

```
     ╱│╲
    ╱ │ ╲
   ╱  →  ╲
  ●───●───●
  [DIRECTED]
```

## Diversity

```
  PATH 1: ●──→●
          ↓
  PATH 2: ●──→●
          ↓
  COMBINE: ●
```

## Turbo Coding

```
  ┌──→ENCODE──┐
  │           ↓
DATA──→INTERLEAVE
  │           ↓
  └──→ENCODE──┘
```

## OFDM

```
  f₀: ∿∿∿∿∿∿
  f₁: ∿∿∿∿∿∿
  f₂: ∿∿∿∿∿∿
  f₃: ∿∿∿∿∿∿
  [ORTHOGONAL]
```

## Broadcast

```
      ●
     ╱│╲
    ╱ │ ╲
   ●  ●  ●
  [ONE TO ALL]
```

## Unicast

```
  ●─────────→●
  [ONE TO ONE]
```

## Multicast

```
      ●
     ╱│
    ╱ │
   ●  ●
  [ONE TO MANY]
```
