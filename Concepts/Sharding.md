# Sharding

![Reference Image](https://docs.mongodb.com/v3.0/_images/sharded-collection.png)

- Sharding is a kind of database partitioning that turns very large databases into data shards which are smaller, faster, and more easily managed.

- These shards can then be spread amongst multiple servers

- As the size of a database and the number of transactions increases per unit of time linearly - the response time for querying the
database increases exponentially

- Example: Split a customer database geographically. Customers on the East Coast can be placed in one server, while customers on the
West Coast can be placed in another. Assuming there is no costumer with multiple locations, the split is easy to maintain and build rules around.

## Disadvantages of Sharding

- Sharding should only be used when all other optimizations prove inadequate

1. Increased complexity of SQL Queries: Developer may cause more bugs because they must write more complicated sql logic to handle shard logic.

2. Backups are more complex: Database backups of individual shards must be coordinated w/ backups of other shards.

3. Operational complexity added: Added/removing columns, indexes, and modifying schema is more difficult.

These problems and many more have now been addressed by independent software vendors who do autosharding
