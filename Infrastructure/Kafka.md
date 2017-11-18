# KAFKA: Distributed Streaming / Messaging System

## What is a Cluster?

A group of computers sharing workload for a common purpose.

**Topic**: Which data? From Producer ABC... but it pushes three different types of records... which do you want? A topic answers
this question as it acts as a unique name for Kafka streams.

## What is a Partition?

Break data to multiple computers. Every partition sits on a single machine (You can't break it up more than that).

## What is a Offset?

A sequence id given to messages as they arrive in a partition?

# How do you select from a stream?

Topic Name -> Partition Number -> Offset

## What is a Consumer Group?

A group of consumers acting as a single logical unit

# Failure

If consumer fails or is a batch consumer (not live) it just wakes up and asks broker to give all data since a specific timestamp

## Retention Policies

Kafka holds data but not main storage when machine gets full we can:

- Delete old data
- Delete old version of data if we have newer versions of that data coming in
