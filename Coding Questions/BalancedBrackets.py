""" A bracket is considered to be any one of the following characters: (, ), {, }, [, or ].

Two brackets are considered to be a matched pair if the an opening bracket (i.e., (, [, or {) occurs to the left
 of a closing bracket (i.e., ), ], or }) of the exact same type. There are three types of matched pairs of brackets: [], {}, and ().

A matching pair of brackets is not balanced if the set of brackets it encloses are not matched.
For example, {[(])} is not balanced because the contents in between { and } are not balanced.
The pair of square brackets encloses a single, unbalanced opening bracket, (, and the pair of parentheses encloses a
 single, unbalanced closing square bracket, ].
"""

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

print is_matched('{[()]}')
print is_matched('{[(])}')
print is_matched('{{[[(())]]}}')
