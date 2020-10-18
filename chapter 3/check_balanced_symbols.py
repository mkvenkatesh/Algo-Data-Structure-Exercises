'''
The balanced parentheses problem shown above is a specific case of a more
general situation that arises in many programming languages. The general problem
of balancing and nesting different kinds of opening and closing symbols occurs
frequently. For example, in Python square brackets, [ and ], are used for lists;
curly braces, { and }, are used for dictionaries; and parentheses, ( and ), are
used for tuples and arithmetic expressions.
'''
# ({})

from stack import Stack

def is_balanced_symbol(inputstr):
    s = Stack()
    for char in inputstr:
        if char in "({[":
            s.push(char)
        elif char in ")}]":
            if (not s.is_empty()):
                temp = s.pop()
                if (temp == "(" and char == ")") or (temp == "{" and char == "}") or (temp == "[" and char == "]"):
                    continue
                else:
                    return False
            else:
                return False    
    if s.is_empty():
        return True

p = "{{([][])}()}"
print(p, "is balanced: ", is_balanced_symbol(p))

p = "[[{{(())}}]]"
print(p, "is balanced: ", is_balanced_symbol(p))

p = "([)]"
print(p, "is balanced: ", is_balanced_symbol(p))

p = "((()]))"
print(p, "is balanced: ", is_balanced_symbol(p))
