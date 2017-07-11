   def minWindow(self, S, T):
        indices = {}
        for char in T:
            indices[char] = []
        miss = list(T)
        start = 0
        end = len(S)
        for i in range(len(S)):
            if S[i] in T:
                if S[i] not in miss and indices[S[i]] != []:
                    indices[S[i]].pop(0)
                elif S[i] in miss:
                    miss.remove(S[i])
                indices[S[i]].append(i)
            if miss == []:
                maximum = max([x[-1] for x in indices.values()])
                minimum = min([x[0] for x in indices.values()])
                if maximum-minimum+1 < end-start+1:
                    start = minimum
                    end = maximum
        if miss != []:
            return ""
        else:
            return S[start:end+1]
        
Basically I kept a dictionary to record the index of each character of T. Each time I found a window, (when miss == []), 
I checked the length of this window by subtracting the maximum index and the minimum index of the characters. 
If this window is the smallest one so far, I record its beginning and ending index as "start" and "end."

# Coin Change DP O(k*n) types of money * amount [you have to iterate through each amount before and check each money for it]

def coinChange(coins, amount):
    MAX = float('inf')
    
    dp = [MAX] * (amount+1)
    result = []
    dp[0] = 0
    for i in xrange(1, amount+1):
        for c in coins:
            if i >= c:
                dp[i] = min(dp[i], dp[i-c] + 1)
    if dp[amount] == MAX:
        return -1
    result = printChange(valused,amount)
    return [dp[amount],result]

## CASES

'30' -> Would fail for brute force if 20,15,5
'0' -> just no amount - could write edge case

30 [25,15,5] -> 25,5 x -> 15 15
30 [25,15,1] -> 25,1,1,1,1,1

## THE ALTERNATIVE COIN CHANGE THAT COUNTS CHANGE

def printChange(valused,amount):
    index = amount
    coins = []
    while index != 0:
        coins.append(valused[index])
        index -= valused[index]

    return coins

def coinChange(coins, amount):
    MAX = float('inf')
    
    dp = [MAX] * (amount+1)
    valused = [MAX] * (amount+1) //UNNEEDED
    result = []
    dp[0] = 0
    for i in xrange(1, amount+1):
        for c in coins:
            if i >= c:
                dp[i] = min(dp[i], dp[i-c] + 1)
                if (dp[i] == dp[i-c]+1): //UNNEEDED
                    valused[i] = c //UNNEEDED
    if dp[amount] == MAX:
        return -1
    result = printChange(valused,amount)
    return [dp[amount],result]

#######

# CHECKING FOR VALID BRACKETS O(N)

def is_matched(expression):
    if expression == '': return
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
    return not s //Checks if empty at end

# EDGE CASES:

'}' -> Insta fail
'{[}' -> No closing bracket
'' -> No value
'{([])}' -> Success
'{}[' -> Ends on open bracket


  
# Common ancestor O(n)

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
    
#EDGE CASES
n1 is a child of n2 -> Then the code will have one side return null and one side return one number so the ancestor is that one
n1 and n2 are children of some ancestor, not of each other -> that node will get left and right value return itself
no tree -> edge case
    
## Largest Contiguous Sum O(n)

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

## EDGE CASE

[4,3,2,-4,10] -> The sum needs to include -4 which will provide the largest value of total 15
[4,3,2,-10,10] -> Needs to restart after -10 because before that it won't contribute anything valuable
[-1,-2,-3,-4] -> all negative values
[] -> nothing -> edge case just write return case

# You bring it back to zero if max_end_here is beneath it because that would mean it is contributing to future sums with a negative value
# which can never be better then if you just start at that value itself

## Stack using queue O(N) push / O(1) pop

class Stack:

    def __init__(self):
        self._queue = collections.deque()

    def push(self, x):
        q = self._queue
        q.append(x)
        for _ in range(len(q) - 1):
            q.append(q.popleft())
        
    def pop(self):
        return self._queue.popleft()

    def top(self):
        return self._queue[0]
    
    def empty(self):
        return not len(self._queue)

    
    
    
## PHONE NUMBER LETTER COMBOS
def letterCombinations(digits):
    mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
               '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    if len(digits) == 0:
        return []
    if len(digits) == 1: // if it's just one value return with the values it represents
        return list(mapping[digits[0]])
    prev = letterCombinations(digits[:-1]) // take everything before the last value
    additional = mapping[digits[-1]] // last value
    return [s + c for s in prev for c in additional] // take every previous permutation and attach the permutations of this number to it

print letterCombinations('54') -> happy case
print letterCombinations('501') -> bad values


    
# ZIG ZAG LEVEL ORDER TRAVERSAL

def zigzagLevelOrder(self, root):
    if not root: return []
    res, temp, stack, flag = [], [], [root], 1
    while stack:
        for i in range(0,len(stack)):
            node = stack.pop(0)
            temp += [node.val]
            if node.left: stack +=[node.left]
            if node.right: stack +=[node.right]
        res+=[temp[::flag]]
        temp = []
        flag*= -1
    return res


# TIC TAC TOE VICTORY

def CheckVictory(board, x, y):

    #check if previous move caused a win on vertical line 
    if board[0][y] == board[1][y] == board [2][y]:
        return True

    #check if previous move caused a win on horizontal line 
    if board[x][0] == board[x][1] == board [x][2]:
        return True

    #check if previous move was on the main diagonal and caused a win
    if x == y and board[0][0] == board[1][1] == board [2][2]:
        return True

    #check if previous move was on the secondary diagonal and caused a win
    if x + y == 2 and board[0][2] == board[1][1] == board [2][0]:
        return True

    return False  




