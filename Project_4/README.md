# Project 4 – Machine Language Programming

## Overview

Project 4 introduces machine language programming on the Hack computer platform. Unlike previous projects that focused on hardware construction, this project explores how software interacts directly with computer hardware through assembly language.

The objective was to write low-level Hack assembly programs that execute directly on the Hack computer. These programs manipulate memory, perform arithmetic operations, control program flow, and interact with memory-mapped hardware devices.

This project provides insight into how high-level programming languages are ultimately translated into machine instructions executed by a processor.

---

## Project Objectives

- Learn the Hack Assembly Language
- Understand instruction execution at the hardware level
- Develop programs using low-level memory manipulation
- Implement arithmetic and control-flow logic
- Gain experience with machine-level programming
- Understand the relationship between software and hardware

---

## Programs Implemented

### Mult.asm
A program that multiplies two positive integers stored in memory and places the result in a destination memory location.

**Inputs**
- `R0` = x
- `R1` = y

**Output**
- `R2` = x × y

Since the Hack platform does not include a hardware multiplication instruction, multiplication is implemented using repeated addition.

```text
x × y
=
x + x + x + ... + x
      y times
```

---

### Fill.asm
A program that interacts with the Hack computer's memory-mapped screen and keyboard.

**Behavior**

- Continuously monitors the keyboard memory location
- If a key is pressed:
  - Fill the screen completely black
- If no key is pressed:
  - Clear the screen completely white

```text
Keyboard
    ↓
Check Key State
    ↓
Key Pressed?
 ┌───────┴───────┐
 │               │
Yes             No
 │               │
 ▼               ▼
Fill Screen   Clear Screen
```

This project demonstrates direct interaction between software and hardware peripherals.

---

## Hack Assembly Language

The Hack computer supports two instruction types.

### A-Instructions

Used to load addresses or constants.

```assembly
@100
```

Loads the value `100` into the A register.

---

### C-Instructions

Used to perform computations and control program flow.

```assembly
D=M
D=D+1
M=D
```

Examples include:

- Arithmetic operations
- Logical operations
- Memory access
- Conditional branching
- Loops

---

## Program Design

### Multiplication Algorithm

The multiplication program performs repeated addition.

```text
Initialize Result = 0
       ↓
Add x to Result
       ↓
Decrement Counter
       ↓
Counter > 0 ?
       ↓
Repeat
```

This demonstrates how higher-level arithmetic operations can be implemented using simpler instructions.

---

### Screen Fill Algorithm

The screen fill program continuously polls the keyboard.

```text
Read Keyboard
       ↓
Key Pressed?
    ┌──┴──┐
    │     │
   Yes    No
    │     │
    ▼     ▼
 Fill   Clear
Screen Screen
```

The program writes directly to screen memory locations to update every pixel on the display.

---

## Memory-Mapped I/O

One of the most important concepts introduced in this project is memory-mapped input/output.

### Keyboard

```text
KBD = 24576
```

Reading this memory location allows programs to detect keyboard input.

---

### Screen

```text
SCREEN = 16384
```

Writing values to screen memory directly updates pixels on the display.

```text
Program
   ↓
Memory Write
   ↓
Screen Hardware
   ↓
Visible Display
```

This mechanism is widely used in embedded systems and computer architecture.

---

## Verification

Programs were tested using the supplied CPU Emulator.

Verification included:

### Mult.asm
- Correct multiplication results
- Loop execution correctness
- Memory output validation

### Fill.asm
- Keyboard detection
- Screen fill operation
- Screen clear operation
- Continuous execution behavior

All supplied test scripts were successfully passed.

---

## Skills Demonstrated

- Assembly Language Programming
- Machine-Level Computing
- Memory Manipulation
- Program Control Flow
- Loop Construction
- Conditional Branching
- Memory-Mapped I/O
- Low-Level Debugging
- Computer Architecture Fundamentals

---

## Key Concepts Learned

### Machine Language Execution

Every software program ultimately becomes machine instructions executed directly by hardware.

```text
Source Code
     ↓
Assembly
     ↓
Machine Code
     ↓
CPU Execution
```

---

### Control Flow

Programs control execution using jumps and labels.

Examples:

```assembly
D;JGT
0;JMP
```

These instructions provide the foundation for loops and decision-making.

---

### Hardware Interaction

Software can directly control hardware by reading and writing memory locations.

```text
Program
   ↓
Memory
   ↓
Hardware Device
```

This concept is fundamental in:

- Embedded Systems
- Device Drivers
- Operating Systems
- Computer Architecture

---

## Repository Structure

```text
Project_4/
├── Mult.asm
├── Fill.asm
├── Mult.tst
├── Fill.tst
├── Mult.cmp
├── Fill.cmp
└── README.md
```

---

## What I Learned

This project demonstrated how software executes at the machine level and interacts directly with hardware resources. Writing programs in assembly language provided a deeper understanding of memory management, control flow, instruction execution, and hardware interfaces.

The project also reinforced the importance of abstraction layers by showing what occurs beneath high-level programming languages and operating systems.

---

## Why This Project Matters

Modern software development typically occurs in high-level languages, but every application eventually executes as machine instructions. Understanding assembly language provides valuable insight into how processors execute programs, how memory is managed, and how software communicates with hardware.

These concepts are fundamental for:

- Computer Engineering
- Embedded Systems
- FPGA Development
- Operating Systems
- Computer Architecture
- Low-Level Software Development

---

## Next Steps

The assembly programs developed in this project will lead into future projects involving:

- CPU Construction
- Computer Architecture Integration
- Assembler Development
- Virtual Machines
- Compiler Design

These projects continue building the complete Hack computer system from the ground up.
