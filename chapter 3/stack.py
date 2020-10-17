'''
Implement Stack ADT that has the following operations;

• Stack() creates a new stack that is empty. It needs no parameters and returns
an empty stack.
• push(item) adds a new item to the top of the stack. It needs the item and
returns nothing.
• pop() removes the top item from the stack. It needs no parameters and returns
the item. The stack is modified.
• peek() returns the top item from the stack but does not remove it. It needs no
parameters. The stack is not modified.
• is_empty() tests to see whether the stack is empty. It needs no parameters and
returns a boolean value.
• size() returns the number of items on the stack. It needs no parameters and
returns an integer.
'''

class Stack:
    def __init__(self):
        self.s = []

    def push(self, item):
        self.s.append(item)

    def pop(self):
        return self.s.pop()

    def peek(self):
        return self.s[-1]
    
    def is_empty(self):
        return self.s == []

    def size(self):
        return len(self.s)


print("Creating new stack.")
s = Stack()
print("Stack is empty? ", s.is_empty())
print("pushing item into stack: 10")
s.push(10)
print("pushing item into stack: True")
s.push(True)
print("pushing item into stack: 8.9")
s.push(8.9)
print("pushing item into stack: 'inter'")
s.push("inter")
print("Peek into stack: ", s.peek())
print("Stack size: ", s.size())
print("Pop item from stack: ", s.pop())
print("Stack is empty? ", s.is_empty())
print("Stack size: ", s.size())
print("Peek into stack: ", s.peek())