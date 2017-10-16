# Collections

The collections module provides specialized container datatypes providing altneratives to Python's general purpose built-in containers:
dict, list, set, and tuple.

## defaultdict objects

Dictionaries are used to store data for later retrieval by name (key). Keys must be unique, immutable objects, and are typically strings.
The values in a dictionary can be anything. For many applications the values are simple types such as integers and strings.

### What is the different between defaultdic and a normal dict structure?

A **defaultdict** works exactly like a normal dict, but it is initialized with a function ("default factory") that takes no arguments
and provides the default value for a nonexistent key.

**A defaultdict will never raise a KeyError.** Any key that does not exist gets the value returned by the default factory.

```
from collections import defaultdict

d = collections.defaultdict(int)

print d['a']
# prints 0
```

Another example is defaulting the value of the dict to be a list.

```
>>> s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
>>> d = defaultdict(list)
>>> for k, v in s:
...     d[k].append(v)
...
>>> d.items()
[('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]
```

## counter objects

A counter tool is provided to support convenient and rapid tallies. For example:

```
test = 'hello'
c = collections.Counter(hello)
print c => {h:1, e:1, l:2, o:1}
```
