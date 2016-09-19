#1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures

"""MY SOLUTION: I write a function that accepts a string. A for loop is implemented to run through the string by letter and compare it with the check string. If the contents of check is the same as the current letter from the loop then it must be not unique. However if the loop runs through the entire string without hitting this case - then it is a unique string."""

def is_unique(x):
    check = ''
    for letter in x:
        if letter == check:
            return False
        else:
            check = letter
    return True

#true
print is_unique('abcdefg')

#false
print is_unique('abcc')

#Assuming user inputs an actual string but this returns true
print is_unique('')