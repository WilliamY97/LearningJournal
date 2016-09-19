#1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters. 
#What if you cannot use additional data structures?

# With data structures

#SET
"""This implementation runs with the set data structure which
can only have distinct values in it. So I've added letters into
the set as the for loop runs and if a letter matches a letter already
in the set then it isn't unique. """
def is_unique2(x):
	seen = set ()
	for letter in x:
		if letter in seen:
			return False
		seen.add(letter)
	return True

# Without data structures

"""For every letter in the string x I check if the 
letter exists more than once with the .count() function.
This runs in quadratic time as the count itself must iterate
through the entire string."""

def is_unique(x):
	for letter in x:
		if x.count(letter) > 1:
			return False
	return True

"""test cases"""

print is_unique('a')
print is_unique('aa')
print is_unique('ab')
print is_unique('ab ')
print is_unique('')
print is_unique(' ')
print is_unique('  ')
print is_unique('qwerty')
print is_unique('qwerte')

# T F TTTT F TT
