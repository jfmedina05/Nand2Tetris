# Project 3 – Sequential Logic & Memory

## Overview

Project 3 introduces sequential logic and memory systems, marking the transition from combinational circuits to stateful hardware. Unlike the logic gates and arithmetic circuits developed in previous projects, sequential circuits can store information and maintain state across clock cycles.

The objective of this project was to build the memory hierarchy of the Hack computer, beginning with a single-bit storage element and progressing to registers and RAM modules capable of storing thousands of values.

All components were implemented using the Nand2Tetris Hardware Description Language (HDL) and verified using the provided Hardware Simulator and automated test suites.

---

## Project Objectives

- Understand the difference between combinational and sequential logic
- Learn how computers store information
- Implement memory devices using clocked circuits
- Build hierarchical memory systems
- Understand addressing and memory access
- Create the foundation for CPU and computer architecture design

---

## Components Implemented

### Basic Storage Element
- Bit

### Register
- Register

### RAM Modules
- RAM8
- RAM64
- RAM512
- RAM4K
- RAM16K

### Counter
- Program Counter (PC)

---

## Design Methodology

The project follows a hierarchical approach where small memory components are combined into increasingly larger storage systems.

### Step 1 – Bit

A Bit stores a single binary value.

```text
Input
  │
  ▼
 Load
  │
  ▼
 DFF
  │
  ▼
Output
```

The Bit uses a Data Flip-Flop (DFF) as the fundamental memory element.

---

### Step 2 – Register

A Register combines 16 Bits to store a 16-bit value.

```text
16 Bits
   ↓
Register
```

Registers are used extensively within processors for temporary storage and instruction execution.

---

### Step 3 – RAM8

Eight Registers are combined using multiplexers and demultiplexers.

```text
8 Registers
     ↓
   RAM8
```

An address selects which register is read or written.

---

### Step 4 – RAM Hierarchy

Memory capacity is expanded hierarchically.

```text
RAM8
 ↓
RAM64
 ↓
RAM512
 ↓
RAM4K
 ↓
RAM16K
```

Each larger memory module is built from multiple instances of the previous design.

---

### Step 5 – Program Counter

The Program Counter (PC) is a specialized register that tracks instruction execution.

Functions include:

- Increment
- Load
- Reset
- Hold value

```text
Current Address
        │
        ▼
 Program Counter
        │
        ▼
 Next Instruction
```

---

## Memory Architecture

The memory hierarchy developed in this project forms the storage subsystem of the Hack computer.

```text
Bit
 ↓
Register
 ↓
RAM8
 ↓
RAM64
 ↓
RAM512
 ↓
RAM4K
 ↓
RAM16K
```

Each level increases storage capacity while maintaining the same fundamental design principles.

---

## Key Concepts

### Sequential Logic

Unlike combinational circuits, sequential circuits depend on both:

- Current inputs
- Previous state

```text
Output = f(Input, Previous State)
```

This allows hardware systems to remember information.

---

### Data Flip-Flops (DFFs)

The DFF is the fundamental storage element used throughout the memory hierarchy.

Characteristics:

- Stores one bit
- Updates on clock edge
- Retains value between cycles

---

### Addressing

Memory locations are selected using binary addresses.

Example:

```text
Address = 101
```

Selects one of eight locations within RAM8.

This concept scales to larger memory modules.

---

### Hierarchical Design

Large systems can be constructed by repeatedly combining smaller verified modules.

```text
Bits
 ↓
Registers
 ↓
RAM
 ↓
Memory System
```

This design philosophy is widely used in modern processor and FPGA development.

---

## Verification

Each component was tested using the Nand2Tetris Hardware Simulator.

Verification included:

- Data storage correctness
- Read/write functionality
- Address selection validation
- Clocked behavior testing
- Program Counter operation

All memory components successfully passed the provided test suites.

---

## Skills Demonstrated

- Sequential Logic Design
- Memory Architecture
- Hardware Description Language (HDL)
- Register Design
- RAM Construction
- Addressing Systems
- Clocked Circuit Design
- Hierarchical Hardware Development
- Digital Systems Verification

---

## Repository Structure

```text
Project_3/
├── Bit.hdl
├── Register.hdl
├── RAM8.hdl
├── RAM64.hdl
├── RAM512.hdl
├── RAM4K.hdl
├── RAM16K.hdl
├── PC.hdl
└── README.md
```

---

## What I Learned

This project demonstrated how computers store and retrieve information. By building memory systems from individual storage elements, I gained a deeper understanding of sequential logic, state retention, addressing, and memory hierarchy design.

The project also highlighted the importance of modular design, as larger RAM structures were constructed entirely from previously verified components.

---

## Why This Project Matters

Memory is a fundamental component of every computing system. Modern processors rely on registers, caches, RAM, and storage systems to execute instructions and manage data efficiently.

Understanding how memory is constructed from simple storage elements provides a strong foundation for:

- Computer Architecture
- FPGA Design
- Embedded Systems
- Processor Design
- Digital Systems Engineering

The memory hierarchy developed in this project becomes a critical subsystem of the Hack computer and CPU constructed in later projects.

---

## Next Steps

The memory systems built in this project will be integrated into future components, including:

- CPU Design
- Instruction Execution
- Computer Architecture
- Machine Language Programs

These developments move the Hack platform closer to becoming a fully functioning computer system.
