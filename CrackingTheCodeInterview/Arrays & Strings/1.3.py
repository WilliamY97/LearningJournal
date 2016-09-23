"""SOLUTION: I set up a new string variable and for every letter in s,
I reduce from the integer counter and check if the letter is ' ',
if it is I add %20 to the new string or else I add the letter itself.
When i reaches < 0 then we have gone through the true length of the
string and everything after is not necessary to add. Finally return new
"""

def URLify (s,i):
    new = ''
    for letter in s:
        i -= 1
        if i < 0:
            break
        elif (letter == ' '):
            new += ('%20')
        else:
            new += (letter)
    return new

print URLify('Mr John Smith    ',13)
print URLify('much ado about nothing      ', 22)

#Mr%20John%20Smith 
#much%20ado%20about%20nothing 
