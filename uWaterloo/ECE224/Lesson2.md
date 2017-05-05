# Software, Synchronization, and Device Drivers

**Abstraction Layers:** A comparison of the abstraction layers for embedded software development

**Software Synchronization:** An examination of synchronization from the software perspective. Examines types of
synchronization.

**Device Drivers:** Definition of device drivers and their needs

## Software Development

- Microprocessor systems require both hardware / software design

- Low level functions typically interact directly w/ hardware devices to do:
Initialize device configuration, read or write data, synchronize using polling or interrupts

## Software Synchronization

- When a device completes its task, the device must synchronize with the processor
- Events may be assigned priorities to ensure minimum latency for high priority events

**CPU Latency and Device Latency:** CPU latency is the time between the receipt of a service
request and the initiation of service. Latency can involve both hardware/softwar delays.

**Real-Time System:** A system that guarantees a worst-case latency for critical events.
