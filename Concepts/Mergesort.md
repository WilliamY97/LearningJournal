## Mergesort

```
Merge-Sort A[1..n]
1. If n = 1, done.
2. Recursively sort A[1..ceiling(n/2)]
3. "Merge" the 2 sorted lsits.
```

- We omit the base case when T(n) = tight(1) for sufficiently small n, but only when it
has no effect on the asymptotic solution to the recurrence.

- Has a run time of tight(n log n)
