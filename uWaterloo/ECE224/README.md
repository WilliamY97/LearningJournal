# ECE224

## Introduction to Embedded Systems

Embedded System: Special purpose computer system designd to perform a task without user's knowledge of its existence. The user may
provide input to embedded system via controls and sensors but the user need not be aware of the presence of the system.

## Embedded System Design

- Simple embedded systems are constructed out of electronics w/o processor/software, however
there will be state.

- Complex embedded systems incorporate one or more processors with sophisticated development control
software

Hardware / Software Codesign: Term given to task of simulatenously designing hardware/software components of a combined
hardware/software system.

## Why is Embedded System Design Challenging?

- Multidisciplinary design problems
- Complex Device Interactions
- Unpredicatable external environment

- Security/reliability are very important

## Embedded Systems and Real-time

Real-time System: Correctness of a result depends on time which it is delivered

Soft real-time: Timing violation leads to degradation in the usefulness of the
embedded system

Hard real-time: A timing violation leads to total system failure

Real-time requirements typically emerge from control constraints:

Ex. system must send a command to an actuator 100 times a second

## Board-level / PC-like architecture

Microprocessor: A chip that implements the CPU only.

- CPU can compromise one or multiple cores (Processors)
- Also typically includes (some levels of) caches.

All other functional blocks (I/O, main memory) are implemented using seperate chips.

Chips are connected to a printed circuit board (motherboard) which implements the
interconnection network.

Motherboards come in different **form factors**

## Microcontroller

Microcontroller: A complete embedded computer on a single chip.

This term commonly refers to system incorporating low-power processor.

- Small / cost-effective / built-in main memory (SRAM) and storage (flash memory)
- Specialized built-in interface support generally includes: analog inputs / general digital inputs/outputs
- Designed to meet the needs of a wide range of applications

## System-on-a-Chip

**System-on-a-Chip (SoC):** A complete computer (possibly excluding main memory) on a single chip.

This term commonly refers to systems incorporating higher performance processors / complex interfaces.

- Multiple cores, heterogeneous processors (ex. graphic processing units).
- Large amount of DRAM main memory, generally on a seperate chip
- Interfaces might include Ethernet, Wi-Fi, Serial ATA...
- Designed to meet needs of specific class of devices (ex. smartphones)

## Circuit Technology

**Application Specific Integrated (ASIC)**

- A chip designed for a specific hardware system
- High to extremely high fixed cost, relatively lower variable cost
- Higher performance and lower power consumption

**Programmable Logic Device (PLD)**

- A chip that can be configured after production to implemenet a specific hardware system

- The configuration is stored in a memory. Alternatives:
1. One-time programmable vs reconfigurable
2. Volatile memory vs non-volatile

## The Lab Project

- Creating System-on-a-Programmable-Chip (SoPC): A SoC implemeneted using PLD
- Specific PLD we use is a Field Programmable Gate Array (FPGA).
SRAM-based device
The configuraton data for a hardware system is called a **bitstream**

You will use tools to specify configuration (including processor and I/O) and automatically
generate a bitstream

Internally, the tool uses a hardware description language (VHDL) to model the functionality of the implemented hardware

## Introduction to FPGA

- An array of **Configurable Logic Blocks (CLB)** with configurable connections
- Each CLB implements both sequential logic (register) and combinational logic (**lookup table**)

## Connections

- Each CLB has horizontal and vertical conenctions with neighbouring blocks and general purpose (long) wires.

- The FPGA comprises columsn of CLBS, connections between distant nodes can use general purpose wires.
