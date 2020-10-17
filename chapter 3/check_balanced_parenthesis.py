'''
Balanced parentheses means that each opening symbol has a corresponding closing
symbol and the pairs of parentheses are properly nested. Given a string of
open/closed parenthesis, check if it's balanced or not.
'''

from stack import Stack

def is_balanced_paren(inputstr):
    s = Stack()
    for char in inputstr:
        if char == "(":
            s.push(char)
        elif char == ")":
            if (not s.is_empty()) and s.pop() == "(":
                continue
            else:
                return False    
    if s.is_empty():
        return True

p = "((()()())(()))"
print(p, "is balanced: ", is_balanced_paren(p))

p = "((()()()(()))"
print(p, "is balanced: ", is_balanced_paren(p))

p = ")))"
print(p, "is balanced: ", is_balanced_paren(p))

p = "()()()()()()()()()"
print(p, "is balanced: ", is_balanced_paren(p))
