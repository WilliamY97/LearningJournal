#Pipelining

##Basic Pipelining Concepts

- Performance optimization
- Reducing overall latency of billions of instructions

- Take 5 stages of RISC Processor and Pipelining

- Every clock signal you have an instruction to fetch to put into 5 stage pipelining

Pipelining: Multiple stages are active simultaneous for different instructions.

- I'm fetching the AND and decoding the SUBTRACT

- Ideal case is 5 instructions occupying all stages so every cycle we can finish one instruction. Otherwise it would take
five cycles for one instruction.

##Basic Stage Operation

- THe result of logic circuit moves to the next stage every clock edge
- Every clock cycle we want to move the stage to next one
- Pipelining - the result of one logic circuit in stage 1 is the input for logic circuit in stage 2 at next clock cycle

##Ideal Case

- Ideal case in pipelining - you want to go through all five stages
- You need to generate control signals for every stage
- Do we have enough data path components? You might need more intermediate registers.
- Add more interstage registers to pipeline control signals

##Pipeline Organization

- A new instruction enters pipeline every cycle.
- Carry along instruction-specific information as instructions flow through the different stages
- Use interstage buffer/registers to hold this information
- Carry any instruction from a stage forward
- Not only do this for data but for control signals

##Pipelining Issues

- Data Hazards: RAW Hazards -> Read-after-write

##Stalling the Pipeline for RAW Hazard

- Allow subtract to continue so long as Add completes the write-back

![Reference Image](http://people.engr.ncsu.edu/efg/521/s06/common/lectures/notes/lec18_files/image003.gif)

##A Closer Inspection (Slide 15)

- We can allow the subtract to continue to the next stage without stalling. The computed result for R2 is available at end of cycle 3.
- Pass this as an input to the Execute stage (ALU) when the Subtract reaches there.
- This is called **Operand Forwarding**: Handles dependencies w/o need to stall the pipeline

##Operand Forwarding

- For the next sequence of instructions, the new value of R2 is gonnab e ready at the end of cycle 3
- **Forward** value to where it is needed in cycle 4

##Implementing Forwarding

- Introduce multiplexers before ALU inputs to use contents of RZ as forwarded value

- Control circuitry notices that there is a dependency in cycle 4 when Subtract is in Execute stage

- Compare destination of Add in Memory stage with source(s) of Subtract in Execute stage

- Set multiplexer control based on comparison



