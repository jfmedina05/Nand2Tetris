# Project 2 – Boolean Arithmetic

## Overview

Project 2 builds upon the logic gates developed in Project 1 by implementing arithmetic circuits capable of performing binary addition and arithmetic operations. These circuits form the foundation of the Arithmetic Logic Unit (ALU), one of the most important components of a computer processor.

The objective of this project was to construct increasingly complex arithmetic hardware modules using previously developed logic gates and to understand how computers perform mathematical operations at the hardware level.

All components were implemented using the Nand2Tetris Hardware Description Language (HDL) and verified using the provided Hardware Simulator and automated test suites.

---

## Project Objectives

- Learn how arithmetic operations are implemented in digital hardware
- Design binary adders using logic gates
- Build multi-bit arithmetic circuits
- Understand carry propagation in binary addition
- Implement a complete Arithmetic Logic Unit (ALU)
- Gain experience with hierarchical hardware design

---

## Components Implemented

### Arithmetic Building Blocks
- HalfAdder
- FullAdder

### Multi-Bit Arithmetic Circuits
- Add16
- Inc16

### Arithmetic Logic Unit
- ALU

---

## Design Methodology

The project follows a hierarchical design approach where simple arithmetic components are combined to create more sophisticated hardware.

### Step 1 – Half Adder

A Half Adder performs the addition of two single-bit inputs.

```text
A ──┐
    ├── Half Adder ── Sum
B ──┘
                  └─ Carry
```

---

### Step 2 – Full Adder

A Full Adder extends the Half Adder by incorporating a carry input from a previous stage.

```text
A ──┐
    ├── Full Adder ── Sum
B ──┤
    │
Cin ┘
          └─ Carry Out
```

---

### Step 3 – 16-Bit Adder

Multiple Full Adders are connected together to create a ripple-carry adder capable of adding two 16-bit numbers.

```text
Bit 0 Adder
     ↓
Bit 1 Adder
     ↓
Bit 2 Adder
     ↓
 ...
     ↓
Bit 15 Adder
```

---

### Step 4 – Arithmetic Logic Unit

The ALU combines arithmetic and logical operations into a single hardware module.

```text
            x
            │
            ▼
      ┌───────────┐
      │           │
      │    ALU    │
      │           │
      └───────────┘
            ▲
            │
            y

Output → out
Flags  → zr, ng
```

The ALU supports:

- Addition
- Subtraction
- Bitwise AND
- Constants
- Negation
- Zeroing inputs
- Status flag generation

---

## ALU Functionality

The ALU is controlled through six control bits:

| Control Bit | Purpose |
|------------|---------|
| zx | Zero x input |
| nx | Negate x input |
| zy | Zero y input |
| ny | Negate y input |
| f | Select Add or AND |
| no | Negate output |

These control bits allow the ALU to perform a wide variety of operations using a single hardware circuit.

Examples include:

| Operation | Description |
|-----------|------------|
| x + y | Addition |
| x - y | Subtraction |
| x AND y | Bitwise AND |
| 0 | Constant zero |
| 1 | Constant one |
| -1 | Constant negative one |
| NOT x | Bitwise inversion |
| NOT y | Bitwise inversion |

---

## Verification

Each circuit was tested using the provided Nand2Tetris test scripts.

Verification included:

- Correct arithmetic behavior
- Carry propagation validation
- Multi-bit addition testing
- ALU control signal verification
- Status flag validation

All components successfully passed the supplied test suites.

---

## Skills Demonstrated

- Digital Arithmetic Design
- Binary Number Systems
- Hardware Description Language (HDL)
- Adder Design
- Arithmetic Logic Unit Design
- Combinational Logic
- Processor Fundamentals
- Hardware Verification

---

## Key Concepts Learned

### Binary Addition

Computers perform arithmetic using binary addition. More complex operations such as subtraction are implemented using addition and complement arithmetic.

---

### Carry Propagation

Multi-bit arithmetic requires carries to propagate between stages of the adder.

```text
Bit0 → Carry
          ↓
Bit1 → Carry
          ↓
Bit2 → Carry
```

This concept becomes increasingly important in processor performance and hardware optimization.

---

### Arithmetic Logic Units

The ALU serves as the computational core of a processor.

It is responsible for:

- Arithmetic operations
- Logical operations
- Comparison support
- Status flag generation

Nearly every instruction executed by a CPU eventually relies on the ALU.

---

## Repository Structure

```text
Project_2/
├── HalfAdder.hdl
├── FullAdder.hdl
├── Add16.hdl
├── Inc16.hdl
├── ALU.hdl
└── README.md
```

---

## What I Learned

This project demonstrated how computers perform arithmetic at the hardware level. By building adders from logic gates and combining them into a complete ALU, I gained a deeper understanding of how processors execute mathematical and logical instructions.

The project reinforced the importance of hierarchical design, hardware abstraction, and modular development while providing insight into one of the most critical components of modern computer architectures.

---

## Why This Project Matters

Every modern processor contains one or more Arithmetic Logic Units that execute the computations required by software. Understanding how arithmetic circuits are constructed provides a strong foundation for computer architecture, FPGA development, embedded systems, processor design, and digital hardware engineering.

The ALU developed in this project becomes a core component of the Hack CPU constructed in later Nand2Tetris projects.

---

## Next Steps

The arithmetic circuits developed in this project will be used to build:

- Registers
- Memory Systems
- Program Counters
- CPUs
- Complete Computer Architectures

Future projects expand these arithmetic foundations into fully functioning computer hardware systems.
