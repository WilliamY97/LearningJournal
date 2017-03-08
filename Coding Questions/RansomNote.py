# A kidnapper wrote a ransom note but is worried it will be traced back to him. He found a magazine and wants
# to know if he can cut out whole words from it and use them to create an untraceable replica of his ransom note.
# The words in his note are case-sensitive and he must use whole words available in the magazine, meaning he
# cannot use substrings or concatenation to create the words he needs.

# Given the words in the magazine and the words in the ransom note, print Yes if he can replicate his ransom note
# exactly using whole words from the magazine; otherwise, print No.

#Note to Self: Careful when multiples of the same word occur in the ransom. You need to make sure to check for that by
#increment/decrementing value of hashtable from magazine values.

def ransom_note(magazine, ransom):
    memo = {}
    for word in magazine:
        if word in memo:
            memo[word] += 1
        else:
            memo[word] = 1
    for word in ransom:
        if word in memo:
            if memo[word] > 0:
                memo[word] -= 1
            else:
                return False
        else:
            return False
    return True

magazine = 'give me one grand today night'
ransom = 'give one grand today'

print ransom_note(magazine, ransom)
