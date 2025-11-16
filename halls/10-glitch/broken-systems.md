# Broken Systems

When the code fails spectacularly.

## Stack Overflow

```
    ERROR
    ERROR
    ERROR
  │ ERROR │
  │ ERROR │
  │ ERROR │
  ▼ ERROR ▼
    ERROR
     ▼▼▼
```

## Memory Corruption

```
[DATA][DATA][DATA]
[DATA][DA█A][DATA]
[DATA][████][DATA]
[DA█A][████][DA█A]
[████][████][████]
```

## Segmentation Fault

```
┌─────────────┐
│ ACCESSING   │
│ MEMORY AT   │
│ 0x00000000  │
│             │
└─────────────┘
    SEGFAULT
      ▼
    ☠☠☠
```

## Race Condition

```
Thread A →→→→→
             ╲
              ●← COLLISION
             ╱
Thread B →→→→→
```

## Infinite Loop

```
  START
    │
    ↓
  ┌───┐
  │ ● │←──┐
  └─┬─┘   │
    │     │
    └─────┘
  ENDLESS
```

## Zombie Process

```
  PROCESS [DEAD]
      ↓
   ╭─────╮
   │ ▓▓▓ │
   │ ░░░ │ <UNDEAD>
   ╰─────╯
   WAITING...
```

## Pointer Chaos

```
   ●→●→●
   ↓ ↗ ↓
   ●←●→●
   ↗ ↓ ↘
   ●←●←●
```

## Buffer Underrun

```
████████____
████____....
____........
............
............
```

## Heap Fragmentation

```
▓▓▓░░░▓▓░░▓▓▓▓░
░▓▓▓░▓▓▓░░░▓▓░░
░░▓░▓▓░░▓▓░░▓▓▓
▓░░░▓▓▓░▓░░░░▓░
```

## Integer Overflow

```
999999999
↓↓↓↓↓↓↓↓↓
000000000
MAX EXCEEDED
```

## Deadlock

```
Process A: [██] ← WAITING
             ×
Process B: [██] ← WAITING
  
  DEADLOCK DETECTED
```

## Unhandled Exception

```
try {
  ████████
} catch {
  ░░░░░░░░
}
⚠ UNCAUGHT ⚠
    ▼▼▼
   CRASH
```

## Memory Leak Visual

```
HEAP: ▓▓▓░░░░░
      ▓▓▓▓░░░░
      ▓▓▓▓▓░░░
      ▓▓▓▓▓▓░░
      ▓▓▓▓▓▓▓░
      ▓▓▓▓▓▓▓▓
   OUT OF MEMORY
```

## Dangling Pointer

```
  PTR → [FREED]
    ↓       ↓
   ???     ☠☠☠
```

## Register Dump

```
RAX: ██████████
RBX: ▓▓▓▓▓▓▓▓▓▓
RCX: ▒▒▒▒▒▒▒▒▒▒
RDX: ░░░░░░░░░░
```

## Cache Miss

```
CACHE: [ ][ ][ ]
         ╲│╱
          ●
        MISS
          ↓
      RAM [●]
```

## Bit Flip

```
BEFORE: 01010101
         ↓↓↓↓↓↓↓↓
AFTER:  01011101
           ↑
        FLIPPED
```

## Thread Explosion

```
    MAIN
      │
   ┌──┴──┐
   │  │  │
  ╱│╱ │╲ │╲
 ● ● ● ● ● ●
╱│╱│╱│╱│╱│╱│
●●●●●●●●●●●●
```

## Stack Trace Collapse

```
main()
  ↓
function1()
  ↓
function2()
  ↓
function3()
  ↓
[████████]
   CRASH
```

## Async Mayhem

```
Promise.all([
  ●→→→→→→●
  ●→→→→✗
  ●→→✗
  ●✗
])
REJECTED
```
