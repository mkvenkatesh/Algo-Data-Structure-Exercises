'''
Calculator

Using the direct inflix evaluator code as base, build a calculator out of it.

'''

import sys
from stack import Stack
from check_balanced_parenthesis import is_balanced_paren

def validate_input(infix_expr):
    ops = ("*", "/", "+", "-", "**")
    if not infix_expr \
        or infix_expr.strip() == "" \
            or not is_balanced_paren(infix_expr):
        return False
    
    idx = 0
    for char in infix_expr.split():        
        if char.isdecimal() \
                or char in ops \
                    or char in (" ", "(", ")"):
            # an operator should not come before a closing parenthesis in infix expression
            if char == ")" and infix_expr[idx - 1] in ops:
                return False
            else:
                idx += len(char)
                continue
        else:
            return False
        
    return True

def eval_postfix(operand_stack, operator_stack):
    optr = operator_stack.pop()
    opnd1 = str(operand_stack.pop())
    opnd2 = str(operand_stack.pop())
    operand_stack.push(eval(opnd2 + optr + opnd1))    

def direct_infix_eval():
    
    operator_stack = Stack()
    operand_stack = Stack()

    while True:
        infix_expr = input()
        if infix_expr == '.':
            sys.exit()

        if (validate_input(infix_expr)):
            op_precedence = {
                "**": 0,
                "*": 1,
                "/": 1,
                "+": 2,
                "-": 2
            }

            for char in infix_expr.split():
                # if you encounter a left parenthesis, push it to the stack
                if char == "(":
                    operator_stack.push(char)
                elif char in op_precedence:        
                    # check for any equal or higher precedence operators in stack and
                    # pop them to output
                    while (not operator_stack.is_empty()) and (operator_stack.peek() in op_precedence) and (op_precedence[char] >= op_precedence[operator_stack.peek()]):
                        eval_postfix(operand_stack, operator_stack)                       
                    # if lower precedence, push operator into stack
                    operator_stack.push(char)
                elif char == ")":
                    # pop all the operators in the stack to the output until you
                    # encounter a left parenthesis
                    while operator_stack.peek() != "(":
                        eval_postfix(operand_stack, operator_stack)
                    # get rid off the "(" in the stack
                    operator_stack.pop()
                else:
                    operand_stack.push(char)

            # if there's anything left in the stack, pop it out to output
            while not operator_stack.is_empty():
                eval_postfix(operand_stack, operator_stack)

            print(operand_stack.peek())
        else:
            print(f"ERROR: Unknown expression. To terminate calculator, type '.'")

if __name__ == "__main__":        
    # driver code
    direct_infix_eval()
