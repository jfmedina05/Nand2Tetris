# Project 5 – Computer Architecture

## Overview

Project 5 brings together all previously developed hardware components to construct a complete computer system. Using the Arithmetic Logic Unit (ALU) from Project 2, the memory hierarchy from Project 3, and the machine language concepts from Project 4, this project implements the Hack Computer architecture.

The objective was to build the central processing unit (CPU), integrate memory and input/output devices, and create a fully functional computer capable of executing Hack machine language programs.

This project represents the culmination of the hardware portion of the Nand2Tetris curriculum and demonstrates how processors, memory systems, and peripherals work together to execute software.

---

## Project Objectives

- Construct a complete CPU
- Implement instruction decoding and execution
- Integrate memory and input/output devices
- Build the Hack Computer architecture
- Execute machine language programs on real hardware
- Understand the interaction between processor, memory, and software

---

## Components Implemented

### Central Processing Unit
- CPU

### Memory System
- Memory

### Complete Computer
- Computer

---

## System Architecture

The Hack computer consists of three primary subsystems:

```text
            ┌─────────────┐
            │    CPU      │
            └──────┬──────┘
                   │
                   ▼
            ┌─────────────┐
            │   Memory    │
            └──────┬──────┘
                   │
                   ▼
            ┌─────────────┐
            │   Screen    │
            │ Keyboard    │
            └─────────────┘
```

Together these components form a complete stored-program computer capable of executing machine language instructions.

---

## CPU Design

The CPU serves as the computational core of the Hack computer.

### Responsibilities

- Fetch instructions
- Decode instructions
- Execute arithmetic operations
- Manage registers
- Generate memory addresses
- Control program flow

The CPU integrates:

```text
ALU
 ↓
Registers
 ↓
Instruction Decoder
 ↓
Program Counter
```

---

### CPU Data Flow

```text
Instruction
     ↓
Decode
     ↓
ALU Operation
     ↓
Memory Access
     ↓
Program Counter Update
```

The CPU executes one machine instruction during each clock cycle.

---

## Instruction Execution

The Hack computer supports two instruction types.

### A-Instruction

Loads a constant or address into the A register.

```text
@value
```

Example:

```assembly
@100
```

Loads 100 into the A register.

---

### C-Instruction

Performs computation and control operations.

```text
dest = comp ; jump
```

Examples:

```assembly
D=M
M=D+1
D;JGT
```

These instructions drive the operation of the CPU and ALU.

---

## Memory System

The Memory module integrates multiple memory-mapped devices.

```text
RAM16K
   ↓
Screen
   ↓
Keyboard
```

### Address Map

| Address Range | Device |
|--------------|--------|
| 0 – 16383 | RAM16K |
| 16384 – 24575 | Screen |
| 24576 | Keyboard |

This design allows software to interact with hardware through memory operations.

---

## Memory-Mapped I/O

The Hack computer uses memory-mapped input/output.

### Screen

```text
SCREEN = 16384
```

Writing values to screen memory updates pixels on the display.

```text
Program
   ↓
Memory Write
   ↓
Screen Hardware
   ↓
Display Output
```

---

### Keyboard

```text
KBD = 24576
```

Reading from this location provides keyboard input.

```text
Keyboard
   ↓
Memory Location
   ↓
Program
```

This concept is widely used in embedded systems and computer architecture.

---

## Program Counter (PC)

The Program Counter tracks the next instruction to execute.

Capabilities:

- Increment
- Load
- Reset
- Jump

```text
Current Instruction
         ↓
   Program Counter
         ↓
Next Instruction
```

The PC enables loops, branching, and program execution flow.

---

## Complete Computer

The final Computer chip combines:

```text
CPU
 ↓
Memory
 ↓
ROM (Program Storage)
```

The completed system can:

- Fetch instructions
- Execute computations
- Read and write memory
- Display graphics
- Receive keyboard input
- Run complete machine language programs

---

## Verification

The Hack Computer was tested using the supplied Hardware Simulator and CPU Emulator.

Verification included:

### CPU Testing
- Instruction decoding
- ALU operations
- Register updates
- Jump execution

### Memory Testing
- RAM access
- Screen access
- Keyboard access

### Computer Testing
- Program execution
- Memory interaction
- Instruction sequencing

All supplied tests were successfully passed.

---

## Skills Demonstrated

- Computer Architecture
- CPU Design
- Processor Datapaths
- Instruction Decoding
- Memory Systems
- Hardware Description Language (HDL)
- Program Counter Design
- Memory-Mapped I/O
- Digital Systems Integration
- Hardware Verification

---

## Key Concepts Learned

### Stored Program Architecture

Programs and data are stored in memory and executed sequentially by the CPU.

```text
Program
   ↓
Memory
   ↓
CPU Execution
```

This principle forms the basis of modern computing systems.

---

### Instruction Cycle

Every instruction follows the same execution pattern.

```text
Fetch
 ↓
Decode
 ↓
Execute
 ↓
Write Back
```

Modern processors use more advanced versions of this same concept.

---

### Processor Control

The CPU must coordinate:

- Arithmetic operations
- Memory access
- Instruction sequencing
- Program flow

These functions collectively determine system behavior.

---

## Repository Structure

```text
Project_5/
├── CPU.hdl
├── Memory.hdl
├── Computer.hdl
├── CPU.tst
├── Memory.tst
├── Computer.tst
├── CPU.cmp
├── Memory.cmp
├── Computer.cmp
└── README.md
```

---

## What I Learned

This project demonstrated how individual hardware components combine to create a functioning computer system. Building the CPU and integrating memory devices provided insight into instruction execution, processor design, and the interaction between hardware and software.

The project also reinforced concepts such as abstraction, modular design, and system integration that are fundamental to computer engineering and digital systems development.

---

## Why This Project Matters

Every modern computer—from embedded microcontrollers to high-performance processors—relies on the same core architectural principles explored in this project.

Understanding CPU design and computer architecture provides a strong foundation for:

- FPGA Development
- Embedded Systems
- Processor Design
- Computer Engineering
- Hardware Acceleration
- Operating Systems
- Systems Programming

The Hack Computer represents a complete computing platform built entirely from components developed throughout the Nand2Tetris curriculum.

---

## Next Steps

With the hardware platform complete, future projects move into software development and system software, including:

- Assembler Construction
- Virtual Machine Translation
- Compiler Design
- Operating System Development

These projects build the software stack that runs on the Hack computer, completing the journey from logic gates to a fully functional computing system.
