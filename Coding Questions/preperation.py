# Coin Change DP

def printChange(valused,amount):
    index = amount
    coins = []
    while index != 0:
        coins.append(valused[index])
        index -= valused[index]

    return coins

def coinChange(coins, amount):
    MAX = float('inf')
    
    rs = [MAX] * (amount+1)
    valused = [MAX] * (amount+1)
    result = []
    rs[0] = 0
    for i in xrange(1, amount+1):
        for c in coins:
            if i >= c:
                rs[i] = min(rs[i], rs[i-c] + 1)
                if (rs[i] == rs[i-c]+1):
                    valused[i] = c
    if rs[amount] == MAX:
        return -1
    result = printChange(valused,amount)
    return [rs[amount],result]

# Brackets

def is_matched(expression):
    e = {'(': ')', '{': '}', '[': ']'}
    s = []
    for bracket in expression:
        if bracket in ['(','{','[']:
            s.append(e[bracket])
        elif bracket in e.values():
            if not s or bracket is not s[-1]:
                return False
            s.pop()
        else:
            return False
    return not s
  
# Common ancestor
