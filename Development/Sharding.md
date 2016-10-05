#Sharding

- Sharding is a kind of database partitioning that turns very large databases into data shards which are smaller, faster, and more easily managed.

- These shards can then be spread amongst multiple servers

- As the size of a database and the number of transactions increases per unit of time linearly - the response time for querying the
database increases exponentially

- Example: Split a customer database geographically. Customers on the East Coast can be placed in one server, while customers on the
West Coast can be placed in another. Assuming there is no costumer with multiple locations, the split is easy to maintain and build rules around.
