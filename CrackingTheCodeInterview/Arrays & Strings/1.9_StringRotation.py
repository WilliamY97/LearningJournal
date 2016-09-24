def isSubstring(s1,s2):
    s3 = s2 + s2
    if s1 in s3:
        return True
    else:
        return False
    
print isSubstring('erbottlewat','waterbottle')
