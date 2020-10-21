'''
Postfix expression evaluation - given a postfix expression, evaluate it

Assume the postfix expression is a string of tokens delimited by spaces. The
operators are *, /, +, and −, and the operands are assumed to be single-digit
integer values. The output will be an integer result.
1. Create an empty stack called operand_stack.
2. Convert the string to a list by using the string method split. 
3. Scan the token list from left to right.
    • If the token is an operand, convert it from a string to an integer and
    push the value onto the operand_stack.
    • If the token is an operator, *, /, +, or −, it will need two operands. Pop
    the operand_stack twice. The first pop is the second operand and the second
    pop is the first operand. Perform the arithmetic operation. Push the result
    back on the operand_stack.
4. When the input expression has been completely processed, the result is on
the stack. Pop the operand_stack and return the value.

'''

from stack import Stack

def postfix_eval(expr):
    s = Stack()
    for char in expr:
        if char == " ":
            continue
        elif char in "*/+-":
            op1 = str(s.pop())
            op2 = str(s.pop())
            s.push(eval(op2 + char + op1))
        else:
            s.push(char)

    return s.pop()

expr = "456*+"
print("Postfix Expression", expr, "evaluates to:", postfix_eval(expr))

expr = "78+32+/"
print("Postfix Expression", expr, "evaluates to:", postfix_eval(expr))

expr = "93/"
print("Postfix Expression", expr, "evaluates to:", postfix_eval(expr))