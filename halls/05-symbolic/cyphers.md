# Cyphers

## Caesar Cipher Wheel

```
        ╭───╮
       ╱ A B ╲
      │C ╭─╮ D│
     │E ╱   ╲ F│
     │G│  ●  │H│
     │I ╲   ╱ J│
      │K ╰─╯ L│
       ╲ M N ╱
        ╰───╯
```

## Binary Code

```
  01001000 01000101 01001100
  01001100 01001111 00100001
  
  ░█░░ ░░█░ ░░██ ░░██ ░███
  █░░░ █░░█ █░░█ █░░█ █░░█
```

## Pigpen Cipher

```
  ┌─┬─┬─┐   ╲ │ ╱
  ├─┼─┼─┤    ╲│╱
  ├─┼─┼─┤    ─┼─
  └─┴─┴─┘    ╱│╲
  A B C     ╱ │ ╲
  D E F    J K L
  G H I    M N O
```

## Morse Code

```
  ▄   ▄▄▄       ▄▄▄   ▄▄▄   ▄▄▄
  ▄   ▄         ▄     ▄▄▄
  ━   ━━━       ━━━   ━━━   ━━━
  ━   ━         ━     ━━━
  
  S   O         S     O     S
```

## Substitution Grid

```
  ┌───┬───┬───┬───┬───┐
  │ ⊕ │ ⊗ │ ⊙ │ ⊚ │ ⊛ │
  ├───┼───┼───┼───┼───┤
  │ ◎ │ ◉ │ ◌ │ ◍ │ ◐ │
  ├───┼───┼───┼───┼───┤
  │ ◑ │ ◒ │ ◓ │ ◔ │ ◕ │
  ├───┼───┼───┼───┼───┤
  │ ◖ │ ◗ │ ◘ │ ◙ │ ◚ │
  └───┴───┴───┴───┴───┘
```

## Polybius Square

```
    1  2  3  4  5
  ┌──┬──┬──┬──┬──┐
1 │A │B │C │D │E │
  ├──┼──┼──┼──┼──┤
2 │F │G │H │I │K │
  ├──┼──┼──┼──┼──┤
3 │L │M │N │O │P │
  ├──┼──┼──┼──┼──┤
4 │Q │R │S │T │U │
  ├──┼──┼──┼──┼──┤
5 │V │W │X │Y │Z │
  └──┴──┴──┴──┴──┘
```

## ROT13

```
  A B C D E F G H I J K L M
  ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓
  N O P Q R S T U V W X Y Z
```

## Vigenère Square

```
    A B C D E
  A│A B C D E
  B│B C D E F
  C│C D E F G
  D│D E F G H
  E│E F G H I
```

## Enigma Rotor

```
      ╭─────╮
     ╱ ●   ● ╲
    │ ● ╱─╲ ● │
    │ ●│ ◉ │● │
    │ ● ╲─╱ ● │
     ╲ ●   ● ╱
      ╰─────╯
       ║║║║║
```

## One-Time Pad

```
  Message:  ●─●─●──●─●──●
  Key:      ─●──●─●──●─●─●
  ────────────────────────
  Cypher:   ●●─●●●─●●─●●─●
```

## Steganography

```
  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
  ▓▓░░▓▓▓▓░░▓▓░░▓▓
  ▓▓░░▓▓▓▓░░▓▓░░▓▓
  ▓▓░░░░▓▓░░▓▓░░▓▓
  ▓▓▓▓░░▓▓░░▓▓░░▓▓
  ▓▓▓▓░░▓▓░░▓▓░░▓▓
  ▓▓░░░░▓▓░░░░░░▓▓
  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
```

## Transposition Cipher

```
  1 2 3 4 5
  ─ ─ ─ ─ ─
  H E L L O
  W O R L D
  │ │ │ │ │
  ↓ ↓ ↓ ↓ ↓
  H W E O L R L O L D
```

## Rail Fence Cipher

```
  H . . . O . . . L . . .
  . E . L . W . R . D . .
  . . L . . . O . . . !
  
  HEOLWRD L EL WR D L O !
```

## Pigpen Cipher

```
  ┌─┬─┬─┐  ╲ │ ╱
  │A│B│C│   ╲│╱
  ├─┼─┼─┤    N
  │D│E│F│   ╱│╲
  ├─┼─┼─┤  ╱ │ ╱
  │G│H│I│
  └─┴─┴─┘
```

## Atbash Cipher

```
  A B C D E ... Z
  │ │ │ │ │     │
  ↓ ↓ ↓ ↓ ↓     ↓
  Z Y X W V ... A
  
  Mirror reflection
```

## Book Cipher

```
  Page:Line:Word
  
    42:7:3
      ↓
  [Secret message]
```

## Playfair Cipher

```
  ┌─────────────┐
  │ P L A Y F │
  │ I R B C D │
  │ E G H K M │
  │ N O Q S T │
  │ U V W X Z │
  └─────────────┘
  
  Digraph cipher
```

## One-Time Pad

```
  Message: 1 0 1 1 0
  Key:     0 1 1 0 1
           ─────────
  Cipher:  1 1 0 1 1
  
  ⚠ Use key once only
```

## Vigenère Square

```
    A B C D E ...
  A a b c d e
  B b c d e f
  C c d e f g
  D d e f g h
  E e f g h i
  ...
```

## Zodiac Cipher

```
  ⊕ ◎ ⊗ ⊙ ☉
  ⊚ ◉ ⊛ ☀ ⊝
  
  Multiple symbol sets
```
