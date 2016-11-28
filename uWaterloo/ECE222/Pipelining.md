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


