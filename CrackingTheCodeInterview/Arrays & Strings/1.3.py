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
