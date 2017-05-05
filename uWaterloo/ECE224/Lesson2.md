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

## Performance, Latency, and Throughput

Latency: Delay between arrival of request and completion of service. One could also
consider the average latency or the maximum latency by considering more results.

Throughput: A measure of how many items can be processed per unit of time.
Ex. A system could have a very high latency (5 years for Waterloo Engineering) but
still have a throughput of 900 graduates per year.

## Synchronization Mechanisms

**Blind Cycle**: Software waits for some amount of time and then acts on data whether
or not the device is ready (Dont sync at all)

**Occasional Polling**: Device status is checked at the convenience of the designer

**Periodic Polling**: Device status is checked after a pre-determined amount of time
and this repeats until the device is done. Usually implemented with time-interrupt

**Tight Polling Loop (Gadfly or Busy Waiting)**: Software continously checks the I/O
status, waiting for the device to be done. Although this is implemented as a very tight
loop (i.e. continously testing one status register and looping until the device is ready),
it could be implemented as a sequence of tests (i.e. continously testing a set of status
registers and looping until a device in the set is ready).

**Interrupt Handling**: Device generates a hardware interrupt to request service immediately

## Performance of Synchronization Mechanisms

- First three sync mechanisms (Blind cycle, Occasional Polling, and Periodic Polling) are CPU-oriented.
This means device waits for CPU to initiate synchronization

- Last two sync mechanisms (Tight Polling Loop and Interrupt Handling) are device-oriented:
Device demands immediate service to reduce device latency

## Polling Loop Synchronization - Processing Input Data

- Poll the device, wait until data is available, and then read the input data.

## Polling Loop Synchronization - Outputting Data

Conservative Option: Assume the device is not initially ready, poll the device, wait
until the device is ready and then output the data.

Ex. Tight polling loop example

```
while (not ready_to_output) loop
clear ready_to_output
output data
return
```

Optimistic Option: Assume the device is initially ready, output the data, poll the device
and wait until device is ready.

```
clear ready_to_output
output data
while (not ready_to_output) loop
return
```
## Interrupt Synchronization

1. Device notifies CPU of interrupt request
2. CPU completes execution of current instruction
3. Execution of the main program is suspended
4. Interrupts are disabled (processor specific)
5. Some internal registers are saved (including program counter)
6. Device may be acknowledged
7. Interrupt service routine is selected
8. Interrupt service routine is executed
9. Registers are restored, if required, including the program counter
10. Interrupts are enabled (processor specific)
11. Execution of the main program resumes
