
"""SOLUTION: I set up a hash table and added one to the table for the letter key of s1.
Afterwards I subtracted 1 for every letter key of s2. If the letter values of s1 in hashtable
didn't equal zero in the third for loop then they aren't permutes of each other.
"""

def permute (s1, s2):
    memo = {}
    
    for letter in s1: 
        if memo.get(letter) == None:
            memo[letter] = 1
        else:
            memo[letter] += 1
    
    for letter in s2:
        if letter in memo:
            memo[letter] -= 1
        else:
            return False
        
    for letter in s1:
        if memo[letter] != 0:
            return False
        
    return True

print permute('3563476','7334566') #True

print permute('abcd', 'd2cba') #False
