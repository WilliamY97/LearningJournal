# Chapter 1 - Combinatorial Analysis

## 1.1 Introduction

This chapter deals with methods to count the number of ways things can occur. Many problems in probability can be solve simply by counting the different numbers of ways that a certain event can occur. This mathematical theory of counting is called combinatorial analysis.

## 1.2 The Basic Principle of Counting

### Numbers of ways of to perform two procedures in succession:
If we perform two procedures in succession, and the first takes n1 ways, and for each of these ways, the second procedure can be done in n2 ways, then there are n1 x n2 ways in which the two procedures can be performed successively.

### Number of ways to perform several procedures in succession:
Similarly, if we are performing r procedures, the ith procedure capable of being performed in ni ways regardless of the ways in which the first (i-1) procs were performed, then the r procs can be performed in n1*n2...nr different ways.

## 1.3 Permutations

### Number of ways to order n distinct elements
If we have n distinct elements, there are n x (n-1) x (n-2) x ... x 2 x 1 ways of ordering them. We denote this quantity by n! and in words
by n factorial

### Number of ways to order n elements (some of which are not distinct):
The number of distinct orderings of n objects, n1 of which are type 1, n2 of which are of type 2, ..., and nr of which are type r, is
equal to:

n! / (n1!n2!...nr!), n1 + n2 + ...nr = n

### Number of ways to select r elements from n elements (order is important)
The total number of ways of ordering r elements, chosen from n distinct elements, is equal to: n(n-1)(n-2)...(n-r+1)

This quantity can be also expressed as n!(n-r)!.. This is denoted by nPr, the number of permutations of n things taken r at a time.

## 1.4 Combinations
