# Project 1 – Boolean Logic

## Overview

Project 1 introduces the foundations of digital logic design by constructing a complete set of elementary logic gates using only the primitive NAND gate. Since NAND is a functionally complete gate, every Boolean function can be implemented using combinations of NAND gates alone.

The objective of this project was to build and verify the fundamental hardware components that serve as the foundation for all future projects in the Nand2Tetris curriculum. These components will later be used to construct arithmetic circuits, memory systems, CPUs, and ultimately a complete computer.

All circuits were implemented using the Nand2Tetris Hardware Description Language (HDL) and verified using the provided Hardware Simulator and test suites.

---

## Project Objectives

- Understand how complex digital systems are built from simple logic gates
- Learn hierarchical hardware design principles
- Implement fundamental combinational logic circuits
- Gain experience using Hardware Description Language (HDL)
- Verify circuit correctness through simulation and testing

---

## Components Implemented

### Basic Logic Gates
- Not
- And
- Or
- Xor

### Data Routing Components
- Mux
- DMux

### Multi-Bit Logic Components
- Not16
- And16
- Or16
- Mux16

### Multi-Way Logic Components
- Or8Way
- Mux4Way16
- Mux8Way16
- DMux4Way
- DMux8Way

---

## Design Methodology

The project began with the implementation of the simplest gates using only NAND gates.

```text
NAND
 ├── NOT
 ├── AND
 └── OR
```

These gates were then used to construct more advanced components.

```text
Basic Gates
      ↓
Multiplexers / Demultiplexers
      ↓
16-Bit Gates
      ↓
Multi-Way Components
```

This hierarchical design process mirrors how modern digital systems are built, allowing increasingly complex hardware to be constructed from previously verified modules.

---

## Example Architecture

```text
                NAND
                  │
        ┌─────────┴─────────┐
        │                   │
       NOT                 AND
        │                   │
        └───────┬───────────┘
                │
               OR
                │
        ┌───────┴────────┐
        │                │
       XOR              MUX
        │                │
        └───────┬────────┘
                │
          16-Bit Circuits
                │
        Multi-Way Components
```

---

## Verification

Each component was tested using the provided Nand2Tetris test scripts and comparison files.

Verification included:

- Functional correctness
- Truth table validation
- Multi-bit signal testing
- Input/output routing validation
- Hierarchical component integration

All implemented circuits successfully passed the provided test suites.

---

## Skills Demonstrated

- Digital Logic Design
- Boolean Algebra
- Combinational Circuit Design
- Hardware Description Language (HDL)
- Multiplexer Design
- Demultiplexer Design
- Hierarchical Hardware Construction
- Digital Systems Verification

---

## Key Concepts Learned

### Functional Completeness
The NAND gate is functionally complete, meaning any Boolean function can be constructed exclusively from NAND gates.

### Hierarchical Design
Complex systems can be built by combining smaller verified modules into larger components.

### Hardware Abstraction
HDL enables designers to describe circuit behavior at a higher level while maintaining hardware implementation details.

### Verification and Testing
Digital systems must be systematically tested to ensure correctness before being integrated into larger architectures.

---

## Repository Structure

```text
Project_1/
├── And.hdl
├── And16.hdl
├── DMux.hdl
├── DMux4Way.hdl
├── DMux8Way.hdl
├── Mux.hdl
├── Mux16.hdl
├── Mux4Way16.hdl
├── Mux8Way16.hdl
├── Not.hdl
├── Not16.hdl
├── Or.hdl
├── Or16.hdl
├── Or8Way.hdl
├── Xor.hdl
└── README.md
```

---

## Why This Project Matters

Modern processors contain billions of transistors and millions of logic gates. Understanding how these systems are built begins with mastering the fundamental logic structures that power all digital computation.

This project provides a foundation for computer engineering, computer architecture, FPGA design, embedded systems, and hardware acceleration by demonstrating how complex computing systems emerge from simple logical building blocks.

---

## Next Steps

The components developed in this project serve as the foundation for future Nand2Tetris projects, including:

- Boolean Arithmetic
- Arithmetic Logic Units (ALUs)
- Memory Systems
- CPU Design
- Computer Architecture
- Assembly Language Programming

These projects ultimately culminate in the construction of a complete computer system from first principles.
