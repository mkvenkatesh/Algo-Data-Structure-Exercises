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


def is_float_int(char):
    try:
        float(char)
        return True
    except:
        return False

def validate_input(expr):
    expr = expr.split()
    if expr[0] in "*/+-" or is_float_int(expr[-1]) or len(expr) < 3:
        return False

    for char in expr:
        if is_float_int(char) or char in "*/+-":
            continue
        else:
            return False
    return True

def postfix_eval(expr):
    expr_val = validate_input(expr)
    if (expr_val):
        s = Stack()
        for char in expr.split():
            if char in "*/+-":
                op1 = str(s.pop())
                op2 = str(s.pop())
                s.push(eval(op2 + char + op1))
            else:
                s.push(char)
    if not expr_val or s.size() != 1:
        print(f"\nERROR: Potfix expression '{expr}' failed validation.")
        return

    return s.pop()

expr = "4 5 6 * +"
print("Postfix Expression", expr, "evaluates to:", postfix_eval(expr))

expr = "7 8 + 3 2 + /"
print("Postfix Expression", expr, "evaluates to:", postfix_eval(expr))

expr = "9 3 /"
print("Postfix Expression", expr, "evaluates to:", postfix_eval(expr))

expr = "9a 3 /"
print("Postfix Expression", expr, "evaluates to:", postfix_eval(expr))

expr = "* 3 /"
print("Postfix Expression", expr, "evaluates to:", postfix_eval(expr))

expr = "3 1 / 3"
print("Postfix Expression", expr, "evaluates to:", postfix_eval(expr))

expr = "3 3 3 *"
print("Postfix Expression", expr, "evaluates to:", postfix_eval(expr))