# Section IV: Synchronization, Data Generation, and Data Transfer

## Producer/Consumer Model of Data Transfer

**Producer** Either a software or hardware component responsible for producing data and/or events for the consumer

**Consumer** Either a software or hardware component responsible for consuming data and/or events provided by the producer

**Data** The state information transferred from the producer to the consumer

**Event** The control information transferred from producer to consumer to represent the occurence
of some activity.

## Comunicating Events and Data

**Events Only** An event occurs (door opens) and this occurence is transferred from producer
to consumer

**Event and Data** An event occurs, message arrives, processor produces a value to print, so the
event and the data are transferred to the consumer

**Data Only** Some data value is produced (or changed) but the consumer is not directly
notified of this change.

## A Finite State Machine Model of Interface Communication

- This represents a state machine for producer/consumer. Producer needs to produce data
to have communication (consumer waits for valid data). Consumer then performs additional
functions and transmits it to consumer.

## Synchronization Occurs at Several Levels - A Hierarchical Perspective

1) **Data Generation** How is the data creation controlled (if it is). How is it started?
How is it stopped? Is this done by producer or consumer?

2) **Data Notification/Initiation of Transfer: Once the producer has the data, how does
the producer notify the consumer that it is ready for the data to be consumed? Or
alternatively how does the consumer request the data?

3) **Data Transfer** Once the producer has the data and the consumer is ready for the
data, how is the timing (synchronization) of the transfer handled?

