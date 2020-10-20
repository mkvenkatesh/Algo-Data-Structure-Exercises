'''
Infix Expression (𝐴 + 𝐵) * 𝐶

Prefix Expression
* + 𝐴𝐵𝐶

Postfix Expression 𝐴𝐵 + 𝐶*

Consider these three expressions. Something very important has happened. Where
did the parentheses go? Why don’t we need them in prefix and postfix? The answer
is that the operators are no longer ambiguous with respect to the operands that
they work on. Only infix notation requires the additional symbols. The order of
operations within prefix and postfix expressions is completely determined by the
position of the operator and nothing else. In many ways, this makes infix the
least desirable notation to use. 

In order to convert an expression, no matter how complex, to either prefix or
postfix notation, fully parenthesize the expression using the order of
operations. Then move the enclosed operator to the position of either the left
or the right parenthesis depending on whether you want prefix or postfix
notation. 

# Algorithm
Assume the infix expression is a string of tokens delimited by spaces. The
operator tokens are *, /, +, and −, along with the left and right parentheses,
( and ). The operand tokens are the single-character identifiers 𝐴, 𝐵, 𝐶, and
so on. The following steps will produce a string of tokens in postfix order.

1. Create an empty stack called op_stack for keeping operators. Create an empty
   list for output.
2. Convert the input infix string to a list by using the string method split.
3. Scan the token list from left to right.
   • If the token is an operand, append it to the end of the output list.
   • If the token is a left parenthesis, push it on the op_stack.
   • If the token is a right parenthesis, pop the op_stack until the
   corresponding left parenthesis is removed. Append each operator to the end of
   the output list.
   • If the token is an operator, *, /, +, or −, push it on the op_stack.
   However, first remove any operators already on the op_stack that have higher
   or equal precedence and append them to the output list. 
   
When the input expression has been completely processed, check the op_stack. Any
operators still on the stack can be removed and appended to the end of the
output list.
'''

from stack import Stack

def infix_to_postfix(infix_expr):
    op_precedence = {
        "*": 1,
        "/": 1,
        "+": 2,
        "-": 2
    }
    postfix_output = ""
    s = Stack()

    for char in infix_expr:
        # skip any spaces in input expression
        if char == " ":
            continue
        # if you encounter a left parenthesis, push it to the stack
        elif char == "(":
            s.push(char)
        elif char in op_precedence:        
            # check for any equal or higher precedence operators in stack and
            # pop them to output
            while (not s.is_empty) and (s.peek() in op_precedence) and (op_precedence[char] <= op_precedence[s.peek]):
                postfix_output += s.pop()                        
            # if lower precedence, push operator into stack
            s.push(char)
        elif char == ")":
            # pop all the operators in the stack to the output until you
            # encounter a left parenthesis
            while s.peek() != "(":
                postfix_output += s.pop()
            # get rid off the "(" in the stack
            s.pop()
        else:
            postfix_output += char

    # if there's anything left in the stack, pop it out to output
    while not s.is_empty():
        postfix_output += s.pop()

    return postfix_output

# driver code
expr = "a+b*c"
print("Infix expression", expr, "in postfix is", infix_to_postfix(expr))

expr = "(a+b)*c"
print("Infix expression", expr, "in postfix is", infix_to_postfix(expr))

expr = "A * B + C * D"
print("Infix expression", expr, "in postfix is", infix_to_postfix(expr))

expr = "(A+B)*C-(D-E)*(F+G)"
print("Infix expression", expr, "in postfix is", infix_to_postfix(expr))

expr = "( A + B ) * ( C + D )"
print("Infix expression", expr, "in postfix is", infix_to_postfix(expr))

expr = "( A + B ) * ( C + D )"
print("Infix expression", expr, "in postfix is", infix_to_postfix(expr))