def palindrome(s):
    memo = {}
    odd = 0
    s= s.lower()
    for letter in s:
        letter.lower()
        if memo.get(letter) == None:
            memo[letter] = 1
        else:
            memo[letter] += 1
    
    for letter in s:
        
        if letter != ' ':
            if memo[letter] % 2 != 0:
                odd += 1
    
        if odd > 1:
            return False
    
    return True

print palindrome('Tact Coa')
print palindrome('jhsabckuj ahjsbckj')
print palindrome('Able was I ere I saw Elba')
print palindrome('So patient a nurse to nurse a patient so')
print palindrome('Random Words')
print palindrome('Not a Palindrome')
print palindrome('no x in nixon')
print palindrome('azAZ')

#T T T F F F T T 
