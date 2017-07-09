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

def lca(root, n1, n2):
    if (root == None): return None

    if (root.key == n1 or root.key == n2): return root

    left = lca(root.left,n1,n2)

    right = lca(root.right,n1,n2)

    if(left and right): return root.key

    if(left == None and right == None):
        return None

    if left:
        return left.key
    else:
        return right.key
    
## Largest Contiguous Sum

from sys import maxint
def maxSubArraySum(a,size):
    max_so_far = -maxint - 1
    max_ending_here = 0

    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
 
        if max_ending_here < 0:
            max_ending_here = 0  
    return max_so_far

# You bring it back to zero if max_end_here is beneath it because that would mean it is contributing to future sums with a negative value
# which can never be better then if you just start at that value itself

