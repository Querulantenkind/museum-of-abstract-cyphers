# Syntax Trees

Grammatical structure visualized.

## Simple Sentence

```
        S
       ╱│╲
      │ │ │
     NP VP
     │  │╲
    Det │ NP
     │  │  │
    The cat sat
```

## Noun Phrase

```
       NP
      ╱│╲
    Det Adj N
     │  │  │
    The big dog
```

## Verb Phrase

```
        VP
       ╱│╲
      V NP PP
      │ │  │╲
    saw it on TV
```

## Question

```
         S
        ╱│╲
       │ │ │
      Wh NP VP
      │  │  │
    What you want
```

## Nested Clauses

```
          S
         ╱│╲
       NP │ VP
       │  │ │╲
      She │ V  S
         said │ │╲
             NP VP
             │  │
             I  left
```

## Coordination

```
        NP
       ╱│╲
      │ │ │
     NP and NP
     │      │
    Bob   Alice
```

## Passive Voice

```
         S
        ╱│╲
      NP │ VP
      │  │ │╲
    Ball │ V PP
         was │ │╲
           hit by me
```

## Adjective Phrase

```
        AP
       ╱│╲
     Adv A PP
      │  │ │╲
    very big for me
```

## Prepositional Phrase

```
       PP
      ╱│╲
     P  NP
     │  │╲
    in Det N
       │  │
      the box
```

## Relative Clause

```
         NP
        ╱│╲
       │ │ │
       N │ S
       │ │ │╲
     book that I read
```

## Complement

```
        VP
       ╱│╲
      V  S
      │  │╲
   think NP VP
         │  │
         I  go
```

## Recursive Structure

```
         S
        ╱│╲
      NP │ VP
      │  │ │╲
      │  │ V  S
      │  │ │  │╲
     This is S  ↻
```

## X-Bar Theory

```
        XP
       ╱│╲
    Spec X'
        ╱│╲
       X  YP
```

## Dependency Arc

```
  The cat sat on mat
   │   │   │  │  │
   └───┴───┴──┴──┘
```

## Context-Free Rule

```
  S → NP VP
  
     S
    ╱ ╲
  NP   VP
```

## Ambiguous Parse

```
  PARSE 1:     PARSE 2:
      S            S
     ╱│╲          ╱│╲
   NP VP        NP  VP
```

## Chomsky Normal Form

```
  A → BC
  
    A
   ╱ ╲
  B   C
```

## Parse Forest

```
      S
     ╱│╲
    ╱ │ ╲
   ●  ●  ●
  [MULTIPLE]
```

## Lexical Category

```
       N
      ╱│╲
    N  N  N
    │  │  │
   dog cat bird
```

## Head Movement

```
  BEFORE:     AFTER:
    XP          XP
   ╱ ╲         ╱ ╲
  X   YP →   X+Y  YP
```
