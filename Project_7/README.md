# Project 7 – Virtual Machine I: Stack Arithmetic

## Overview

Project 7 marks the beginning of the software portion of the Nand2Tetris curriculum. In this project, I developed a Virtual Machine (VM) Translator capable of converting stack-based VM commands into Hack assembly language.

Rather than compiling high-level programs directly into machine code, modern computing systems often use an intermediate representation. The Hack Virtual Machine serves as this abstraction layer, allowing programs to be translated into platform-independent VM instructions before being converted into hardware-specific assembly code. Project 7 focuses on translating stack arithmetic and memory access commands from VM code into executable Hack assembly instructions. :contentReference[oaicite:0]{index=0}

---

## Project Objectives

- Build a VM-to-Hack translator
- Implement stack arithmetic commands
- Implement memory access commands
- Translate VM instructions into Hack assembly
- Manage stack operations using the Hack memory model
- Understand virtual machine architecture and abstraction

---

## Problem Statement

High-level programs are often translated into an intermediate virtual machine language before reaching machine code.

```text
High-Level Language
         ↓
      VM Code
         ↓
   VM Translator
         ↓
  Hack Assembly
         ↓
     Assembler
         ↓
    Machine Code
```

The goal of this project was to create the translator responsible for converting VM instructions into Hack assembly code. :contentReference[oaicite:1]{index=1}

---

## Virtual Machine Architecture

The Hack VM uses a stack-based architecture.

Unlike register-based machines, operations are performed using values stored on a stack.

```text
Push Operand A
Push Operand B
      ↓
     Add
      ↓
 Push Result
```

Example:

```vm
push constant 7
push constant 8
add
```

Result:

```text
15
```

stored on top of the stack. :contentReference[oaicite:2]{index=2}

---

## VM Translator Architecture

The translator was designed around three major components.

### Parser

Responsible for:

- Reading VM commands
- Ignoring whitespace and comments
- Identifying command types
- Extracting arguments

```text
VM File
   ↓
 Parser
   ↓
Command Objects
```

---

### Code Writer

Responsible for:

- Generating Hack assembly instructions
- Translating arithmetic operations
- Translating memory access commands
- Managing stack behavior

```text
VM Command
     ↓
 Code Writer
     ↓
Hack Assembly
```

---

### Translator Driver

Responsible for:

- Coordinating parsing and code generation
- Managing input/output files
- Producing final assembly programs

```text
VM Program
     ↓
 Translator
     ↓
Assembly Program
```

---

## Stack Arithmetic Commands

The translator supports all arithmetic and logical VM operations.

### Arithmetic Operations

| Command | Operation |
|----------|-----------|
| add | x + y |
| sub | x - y |
| neg | -x |

### Comparison Operations

| Command | Operation |
|----------|-----------|
| eq | x == y |
| gt | x > y |
| lt | x < y |

### Logical Operations

| Command | Operation |
|----------|-----------|
| and | x & y |
| or | x \| y |
| not | !x |

These commands operate directly on values stored at the top of the stack. :contentReference[oaicite:3]{index=3}

---

## Memory Access Commands

Project 7 also introduces VM memory segments.

### Push Command

```vm
push segment index
```

Copies a value from memory onto the stack.

---

### Pop Command

```vm
pop segment index
```

Removes a value from the stack and stores it in memory.

---

## Memory Segments Implemented

| Segment | Purpose |
|-----------|-----------|
| constant | Immediate values |
| local | Local variables |
| argument | Function arguments |
| this | Object data |
| that | Object data |
| temp | Temporary storage |
| pointer | THIS/THAT references |
| static | Global file-level variables |

These segments provide a consistent abstraction independent of the underlying hardware implementation. :contentReference[oaicite:4]{index=4}

---

## Stack Implementation

The Hack VM uses a stack beginning at RAM address 256.

```text
RAM[256]
    ↓
 Stack
    ↓
Top of Stack
```

The stack pointer (SP) always references the next available location.

### Push Operation

```text
Store Value
      ↓
Increment SP
```

### Pop Operation

```text
Decrement SP
      ↓
Read Value
```

This mechanism enables arithmetic, logical operations, and temporary storage. :contentReference[oaicite:5]{index=5}

---

## Translation Workflow

```text
VM Program
     ↓
Parser
     ↓
Command Type Detection
     ↓
Code Generation
     ↓
Hack Assembly Output
```

Example:

### VM Input

```vm
push constant 5
push constant 3
add
```

### Generated Behavior

```text
Push 5
Push 3
Pop 3
Pop 5
Add
Push Result
```

---

## Testing

The VM Translator was tested using the supplied Nand2Tetris test programs.

### Arithmetic Tests

- SimpleAdd.vm
- StackTest.vm

### Memory Access Tests

- BasicTest.vm
- PointerTest.vm
- StaticTest.vm

Successful execution verified:

- Correct stack manipulation
- Arithmetic operations
- Comparison operations
- Memory segment access
- Static variable handling
- Pointer operations

:contentReference[oaicite:6]{index=6}

---

## Skills Demonstrated

- Systems Programming
- Compiler Back-End Development
- Virtual Machine Design
- Stack-Based Architectures
- Assembly Language Generation
- Parser Design
- Software Translation Systems
- Computer Architecture
- Data Structures
- Software Verification

---

## Key Concepts Learned

### Virtual Machines

Virtual machines provide an abstraction layer between software and hardware.

```text
Application
     ↓
 Virtual Machine
     ↓
 Hardware
```

This approach improves portability and simplifies compiler design. :contentReference[oaicite:7]{index=7}

---

### Stack Machines

Many virtual machines operate using a stack rather than CPU registers.

```text
Push
Push
Operate
Result
```

This simplifies code generation and language implementation. :contentReference[oaicite:8]{index=8}

---

### Translation Systems

The VM Translator represents another stage in the software toolchain.

```text
Source Code
     ↓
 Compiler
     ↓
 VM Code
     ↓
 VM Translator
     ↓
 Assembly
     ↓
 Machine Code
```

This layered architecture is similar to systems such as the JVM and .NET CLR. :contentReference[oaicite:9]{index=9}

---

## Repository Structure

```text
Project_7/
├── VMTranslator.py
├── Parser.py
├── CodeWriter.py
├── SimpleAdd/
├── StackTest/
├── BasicTest/
├── PointerTest/
├── StaticTest/
└── README.md
```

---

## What I Learned

This project demonstrated how virtual machines serve as an intermediate abstraction layer between programming languages and hardware. By implementing a VM Translator, I gained hands-on experience with stack-based architectures, memory management, parsing, and assembly code generation.

The project also highlighted how modern compilers break translation into multiple stages, making software development more portable and manageable.

---

## Why This Project Matters

Modern software systems rarely compile directly to machine code. Instead, they often rely on intermediate representations such as JVM bytecode, .NET IL, or LLVM IR.

The VM Translator developed in this project performs a similar role by translating platform-independent VM commands into hardware-specific assembly instructions. Understanding this process provides valuable insight into:

- Compiler Design
- Virtual Machines
- Operating Systems
- Computer Architecture
- Systems Programming
- Software Toolchains

---

## Next Steps

Project 7 establishes the foundation for a complete VM implementation. Future projects extend the translator to support:

- Branching Commands
- Function Calls
- Function Returns
- Program Control Flow
- Multi-File VM Programs

These capabilities transform the basic VM Translator into a full-scale execution environment for higher-level programming languages.
