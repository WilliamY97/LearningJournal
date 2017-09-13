# defaultdic

Dictionaries are used to store data for later retrieval by name (key). Keys must be unique, immutable objects, and are typically strings.
The values in a dictionary can be anything. For many applications the values are simple types such as integers and strings.

## What is the different between defaultdic and a normal dict structure?

A **defaultdict** works exactly like a normal dict, but it is initialized with a function ("default factory") that takes no arguments
and provides the default value for a nonexistent key.

**A defaultdict will never raise a KeyError.** Any key that does not exist gets the value returned by the default factory.

```
from collections import defaultdict

d = collections.defaultdict(int)

print d['a']
# prints 0
```
