# Methods for Solving Recurrences

http://www.cs.cornell.edu/courses/cs3110/2012sp/lectures/lec20-master/lec20.html

- A recurrence is an equation or inequality that describes a function in terms of its value on smaller inputs.

## Recursion-Tree Method 

- A recursion tree is useful for visualizing what happens when a recurrence is iterated. It diagrams the tree of recursive calls and the amount of work done at each call.

## Repeated Substitution

- Substitute a few times until you see a pattern

- Write a formula in terms of n and the number
of substitutions i

- Choose i so that all references to the base
case

- Solve the resulting summation

## Master Method

![alt tag](https://acrocontext.files.wordpress.com/2014/01/master-method.png)

If the algorithm takes on the form **T(n) = aT(n/b) + Theta(n^k log Pn)** where a >= 1, b > 1, and
f is asymptotically positive

leaves = n^(log_b(a))

- Running time **dominated by cost at leaves**

- Running time **evenly distributed throughout the tree**

- Running time **dominated by cost at the root**

### Master Method Strategy

1. Extract a, b, and f(n) from a given recurrence
2. Determine nlog_b(a)
3. Compare f(n) and n^(log_b(a)) asymptotically
4. Determine appropriate Master Theorem Case, and apply it
