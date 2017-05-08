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

## Synchronization

**Synchronization** For our purposes, synchronization refers to the interaction required to
make two entities (with different views of time) interact.

**Active Synchronization** One of the entities is capable of **forcing** a change in the
operational characteristics of the other. Ex. Setting an interrupt signal can force the
processor to execute the interrupt service routine.

**Passive Synchronization** One of the communicating entities signals a request for
service, however the entity receiving the request is not forced to respond.

## Synchronization Needs

**Active, demand-oriented service** The event at one of the peers must be serviced. This
could be implemented as an interrupt.

**Passive, request-oriented service** The event at one of the pers may be serviced. One
side keeps testing the other to see if an event has occured.

## Generation

Data generation requires action by producer - creation can be initiated by producer/consumer

**Spontaneous Sources** Data is produced in the device independent of the actions of the
consumer accepting the data.

**Consumer Sensitive Sources** Data is produced by the device only after the previous data
has been consumed by the consumer.

**Consumer Responsive Sources** Data is produced by the device only after requested by the
consumer
