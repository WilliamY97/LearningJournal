# Caching
Is a component that transparently stores data so that future requests of that data can be served faster.

**tldr;** Caching is done by some component (ex. beaker) to store data so that requests of the same data can be server again quicker

Caching can reduce the server load by storing the results of common operations and serving the precomputed answers to clients

For example... instead of retrieving data from database tables that rarely change, you can store the values in-memory - which is far faster than from the DB. When the cached values change - the system can invalidate the cache and retrieve the updated values for future requests.
