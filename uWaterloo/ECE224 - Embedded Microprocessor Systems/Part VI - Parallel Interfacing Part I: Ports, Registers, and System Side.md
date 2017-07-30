# Part VI - Parallel Interfacing Part I: Ports, Registers, and System Side

## Interface

- An I/O interface connects a device to a computer system.

- The interface translates between the physical signals (ex. current, voltage level) and the protocol (ex. synchronous bus) of the
interconnection network used by the computer system and those required by the device.

- We divide the interface in two parts:

System Side: Depends on interconnection network
Device Side: Depends on device

## Device Side: Ports

- An interface connects to devices through **ports**

- In the most general case, each port carries both data and control information

## Ports and Direction of Transfer

Unidirectional: Data/event exchanged in one direction only (input or output)

Bidirectional, single-duplex: data/events can be exchanged in both directions (input/output), but only one direction at a time

Bidirectional, full-duplex: Data/event exchanged in both directions at the same time. It's equivalent to having a pair of input and
output unidirectional ports.

## Ports and Interface Type

**Parallel Interface**: Digital data is exchanged multiple bits at a time.
- The device signals include a data bus (multiplew wires)
- The device signals also usually incldue dedicated wires for control information (**out-of-band signalling**)

**Serial Interface**: Digital data is exchanged one bit at a time.
- Control and data are usually exchanged through the same one-bit signal (**in-band signaling**)

**Analog Interface**: Data is exchanged through an analog signal.
- Usually no need for control information due to blind synchronization

## Ports and Registers

- The system side uses a set of **registers**. Each register represents an address in the address range of the interface that bus
Masters (ex: CPU) can read from/write to.

Register Types:

- Data In (read): One register for each input port
- Data Out (write): One register for each output port
- Status (read): Different bits of the same status register can be used to determine the state of the interface and devices attached
to multiple ports.
- Control (write): Different bits of the same control register can be used to set the state of the interface and devices attached to
multiple ports.

Note 1: Interface registers are often implemented using D flip-flops.
Note 2: A read and write register can share address. This is common for Status / Control, and for Data in / Data out in bidirectional ports.

## Ports, Registers, and System Bus: Data Width

- The width of a port is the number of bits/wires used by the data signal of the port.
- The width of a register is the number of bits of the register
- When connected to system bus, the width of a register must be less than or equal to the width of the system data bus.
- The width of a port can be any value. **If the width of the port is greater than the width of the system data bus, then
multiple Data in / Data out registers can be used to connect the port**.


