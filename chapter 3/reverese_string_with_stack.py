'''
Reverse a string using a Stack
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

str_to_reverse = "intercodes"
reversed_str = ""
s = Stack()

for char in str_to_reverse:
    s.push(char)

for i in range(s.size()):
    reversed_str += s.pop()

print(f"Reversed string for '{str_to_reverse}' is: {reversed_str}")    