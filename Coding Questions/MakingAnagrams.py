# Given two strings, and, that may or may not be of the same length, determine the minimum number of character deletions
# required to make  and  anagrams. Any characters can be deleted from either of the strings.

# The idea is to find the values of each set, string A,	string B, that don't intersect. These are the values that need to be
# removed.

# Remember to consider the strategy of preloading - using the alphabet string helps condense the code

def number_needed(a, b):
    d = {}
    c = 0
    for letter in a:
        if letter in d:
            d[letter] += 1
        else:
            d[letter] = 1
    for letter in b:
        if letter in d and d[letter] > 0:
            d[letter] -= 1
        else:
            c += 1
    for v in d:
        c += d[v]
    return c

a = 'ade'
b = 'abc'

print number_needed(a,b)

#Better solution - doesn't require three loops

def number_needed_2(a, b):
    abet = 'abcdefghijklmnopqrstuvwxyz'
    delta = 0
    for i in abet:
        delta += abs(b.count(i) - a.count(i))
    return delta

print number_needed_2(a,b)
