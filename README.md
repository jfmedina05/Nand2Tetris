# Nand2Tetris

A comprehensive exploration of computer systems engineering through the Nand2Tetris curriculum, building a complete computer system from first principles.

---

## Overview

This repository contains my implementations and project work from the Nand2Tetris course and textbook, *The Elements of Computing Systems* by Noam Nisan and Shimon Schocken.

Beginning with a single NAND gate, the curriculum progressively develops every major layer of a modern computing system, including digital logic, arithmetic circuits, memory hierarchies, computer architecture, assembly language, virtual machines, compilers, operating systems, and application software.

Rather than treating computers as black boxes, Nand2Tetris demonstrates how complex computing systems emerge from a hierarchy of abstractions built on simple hardware and software foundations.

---

## Project Progress

| Project | Topic | Status |
|----------|--------|----------|
| Project 1 | Boolean Logic | ✅ Complete |
| Project 2 | Boolean Arithmetic | ✅ Complete |
| Project 3 | Sequential Logic & Memory | ✅ Complete |
| Project 4 | Machine Language Programming | ✅ Complete |
| Project 5 | Computer Architecture | ✅ Complete |
| Project 6 | Assembler | ✅ Complete |
| Project 7 | Virtual Machine I: Stack Arithmetic | ✅ Complete |
| Project 8 | Virtual Machine II: Program Control | 🔄 In Progress |
| Project 9 | High-Level Language | ⏳ Planned |
| Project 10 | Compiler I | ⏳ Planned |
| Project 11 | Compiler II | ⏳ Planned |
| Project 12 | Operating System | ⏳ Planned |

---

## Learning Objectives

Through these projects, I have developed experience in:

- Digital Logic Design
- Hardware Description Language (HDL)
- Computer Architecture
- Assembly Language Programming
- Memory Systems
- Virtual Machine Implementation
- Compiler Fundamentals
- Operating System Concepts
- Systems Programming
- Software Abstraction Layers
- End-to-End Computer System Design

---

## System Architecture Journey

The Nand2Tetris curriculum follows the complete computing stack.

```text
NAND Gates
    ↓
Logic Gates
    ↓
Arithmetic Circuits
    ↓
Memory Systems
    ↓
CPU
    ↓
Hack Computer
    ↓
Assembly Programs
    ↓
Assembler
    ↓
Virtual Machine
    ↓
Compiler
    ↓
Operating System
```

Each project builds upon the previous one, ultimately resulting in a fully functional computer system and software stack.

---

## Hardware Projects

### Project 1 — Boolean Logic
Implemented fundamental logic gates and routing components using only NAND gates.

Key Components:
- Not
- And
- Or
- Xor
- Mux / DMux
- Multi-bit logic circuits

---

### Project 2 — Boolean Arithmetic
Built arithmetic circuits and the Hack ALU.

Key Components:
- HalfAdder
- FullAdder
- Add16
- Inc16
- ALU

---

### Project 3 — Sequential Logic & Memory
Constructed the memory hierarchy for the Hack computer.

Key Components:
- Bit
- Register
- RAM8
- RAM64
- RAM512
- RAM4K
- RAM16K
- Program Counter

---

### Project 4 — Machine Language Programming
Developed Hack assembly programs that execute directly on the hardware platform.

Programs:
- Mult.asm
- Fill.asm

Concepts:
- Assembly Language
- Memory-Mapped I/O
- Program Control Flow

---

### Project 5 — Computer Architecture
Integrated CPU, memory, and I/O devices into a complete Hack computer.

Key Components:
- CPU
- Memory
- Computer

---

## Software Projects

### Project 6 — Assembler
Built a two-pass assembler that translates Hack assembly language into machine code.

Concepts:
- Parsing
- Symbol Tables
- Binary Translation
- Language Processing

---

### Project 7 — Virtual Machine I
Developed a VM Translator that converts stack-based VM commands into Hack assembly language.

Features:
- Stack Arithmetic
- Memory Access Commands
- VM Translation
- Assembly Generation

---

## Technical Concepts Demonstrated

### Digital Logic
- NAND-based Circuit Construction
- Combinational Logic
- Sequential Logic
- Multiplexers & Demultiplexers
- Arithmetic Logic Units
- Registers & Memory

### Computer Architecture
- CPU Design
- Memory Hierarchies
- Program Counters
- Instruction Execution
- Datapath Design
- Memory-Mapped I/O

### Systems Programming
- Assembly Language
- Virtual Machines
- Parsing
- Symbol Resolution
- Memory Management
- Software Translation

### Compiler & Language Systems
- Lexical Analysis
- Parsing
- Syntax Analysis
- Code Generation
- VM Translation
- Language Abstraction

---

## Repository Structure

```text
Nand2Tetris/
├── Project_1/
├── Project_2/
├── Project_3/
├── Project_4/
├── Project_5/
├── Project_6/
├── Project_7/
├── Project_8/
├── Project_9/
├── Project_10/
├── Project_11/
├── Project_12/
└── README.md
```

---

## Skills Developed

- Computer Engineering
- Digital Systems Design
- Computer Architecture
- Hardware Description Languages
- Assembly Programming
- Systems Programming
- Compiler Construction
- Virtual Machine Design
- Operating Systems
- Software Architecture
- Algorithm Design

---

## Why This Project Matters

Most engineering courses focus on individual layers of computing systems. Nand2Tetris is unique because it connects every major abstraction layer into a single cohesive project.

Beginning with NAND gates and progressing toward compilers and operating systems, this repository demonstrates how modern computing systems are built from the ground up. It provides a comprehensive understanding of the relationship between hardware, software, and system architecture, making it one of the most valuable computer engineering projects for understanding how computers actually work.
