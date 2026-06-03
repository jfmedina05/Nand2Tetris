# Project 6 – Assembler

## Overview

Project 6 introduces the software layer that bridges human-readable assembly language and machine-executable binary instructions. In this project, I developed an assembler capable of translating Hack assembly programs into Hack machine code.

The assembler serves as the first major software tool in the Nand2Tetris curriculum and represents a critical component of the software development toolchain. It automates the conversion of symbolic assembly instructions into binary machine instructions that can be executed directly by the Hack computer constructed in Project 5.

This project demonstrates the relationship between programming languages, machine instructions, and computer architecture while introducing concepts that are foundational to compilers, interpreters, and software toolchains.

---

## Project Objectives

- Develop a two-pass assembler for the Hack computer
- Translate symbolic assembly language into binary machine code
- Implement symbol resolution and label handling
- Build a symbol table for variables and labels
- Automate machine code generation
- Understand language translation systems

---

## Problem Statement

The Hack computer executes binary instructions:

```text
0000000000010000
1110110000010000
1110001100001000
```

However, programmers prefer writing symbolic assembly code:

```assembly
@i
M=1

(LOOP)
@i
M=M+1
@LOOP
0;JMP
```

The assembler translates assembly language into machine language:

```text
Assembly Program
        ↓
     Assembler
        ↓
Binary Machine Code
        ↓
     Hack CPU
```

---

## Assembler Architecture

The assembler was implemented using a two-pass design.

### First Pass – Symbol Resolution

The assembler scans the source file and records label definitions.

Example:

```assembly
(LOOP)
```

The symbol table stores:

```text
LOOP → 12
```

This allows jump instructions to reference symbolic locations.

---

### Second Pass – Code Translation

The assembler processes instructions and generates binary machine code.

Example:

```assembly
@10
```

becomes:

```text
0000000000001010
```

And:

```assembly
D=A
```

becomes:

```text
1110110000010000
```

---

## Translation Workflow

```text
Assembly Source
       ↓
Lexical Parsing
       ↓
Symbol Resolution
       ↓
Instruction Translation
       ↓
Machine Code Output
```

---

## Instruction Types

The Hack assembly language supports three major instruction categories.

### A-Instructions

Load constants or addresses.

```assembly
@123
```

Machine code:

```text
0000000001111011
```

---

### C-Instructions

Perform computations and control operations.

```assembly
D=M+1
```

Machine code:

```text
1111110111010000
```

Components:

```text
dest = comp ; jump
```

---

### Labels

Used to define symbolic jump locations.

```assembly
(LOOP)
```

Labels do not generate machine code but are stored in the symbol table.

---

## Symbol Table

The assembler maintains a symbol table containing:

### Predefined Symbols

| Symbol | Address |
|----------|----------|
| SP | 0 |
| LCL | 1 |
| ARG | 2 |
| THIS | 3 |
| THAT | 4 |
| SCREEN | 16384 |
| KBD | 24576 |

---

### Register Symbols

```text
R0 → 0
R1 → 1
...
R15 → 15
```

---

### User Variables

Variables are automatically assigned memory locations beginning at address 16.

Example:

```assembly
@counter
```

becomes:

```text
counter → 16
```

---

### Labels

Example:

```assembly
(END)
```

becomes:

```text
END → ROM Address
```

---

## Core Components

The assembler consists of several major subsystems.

### Parser

Responsible for:

- Reading source code
- Removing whitespace
- Removing comments
- Identifying instruction types

```text
Assembly Line
      ↓
    Parser
      ↓
Instruction Type
```

---

### Code Module

Responsible for converting symbolic instructions into binary codes.

Example:

```assembly
D=A
```

↓

```text
1110110000010000
```

---

### Symbol Table

Stores:

- Labels
- Variables
- Predefined symbols

```text
Symbol
   ↓
Address Lookup
   ↓
Binary Translation
```

---

## Verification

The assembler was tested using the supplied Hack assembly programs.

Verification included:

### Translation Correctness

- A-instruction translation
- C-instruction translation
- Label handling
- Variable allocation

### Program Execution

Generated machine code was executed on the Hack computer to verify functionality.

Programs tested included:

- Add.asm
- Max.asm
- Rect.asm
- Pong.asm

All translated programs executed correctly.

---

## Skills Demonstrated

- Systems Programming
- Language Translation
- Compiler Fundamentals
- Symbol Table Design
- Parsing
- Binary Encoding
- Software Toolchain Development
- Computer Architecture
- Data Structures
- Software Verification

---

## Key Concepts Learned

### Assemblers

Assemblers translate symbolic assembly instructions into machine-executable binary code.

```text
Assembly
   ↓
Assembler
   ↓
Machine Code
```

This forms a critical layer between software and hardware.

---

### Symbol Resolution

Labels and variables improve program readability while allowing machine code generation.

Example:

```assembly
@counter
```

is easier to understand than:

```assembly
@16
```

The assembler automatically resolves symbolic references.

---

### Language Translation

The assembler is an example of a translator:

```text
Source Language
       ↓
 Translator
       ↓
Target Language
```

This concept extends to:

- Compilers
- Interpreters
- Linkers
- Virtual Machines

---

## Repository Structure

```text
Project_6/
├── Assembler.py
├── Parser.py
├── Code.py
├── SymbolTable.py
├── Test Programs/
├── Generated Machine Code/
└── README.md
```

---

## What I Learned

This project demonstrated how software tools bridge the gap between human-readable programs and machine-executable instructions. Building an assembler provided valuable experience with parsing, symbol management, binary encoding, and software architecture.

The project also introduced concepts that form the foundation of compiler construction, operating systems, and modern software toolchains.

---

## Why This Project Matters

Every software program must eventually be translated into machine code before execution. Assemblers represent one of the earliest and most fundamental forms of language translation.

Understanding how assemblers work provides a strong foundation for:

- Compiler Design
- Operating Systems
- Embedded Systems
- Systems Programming
- Computer Architecture
- Software Toolchain Development

The assembler developed in this project becomes a key component of the complete software stack built throughout the remainder of the Nand2Tetris curriculum.

---

## Next Steps

With the assembler complete, future projects move to higher abstraction levels, including:

- Virtual Machine Translation
- High-Level Programming Languages
- Compiler Construction
- Operating System Development

These projects continue building the software infrastructure that runs on the Hack computer, ultimately completing the journey from NAND gates to a modern computing system.
