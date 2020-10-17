'''
Reverse a string using a Stack
'''

from stack import Stack

str_to_reverse = "intercodes"
reversed_str = ""
s = Stack()

for char in str_to_reverse:
    s.push(char)

for i in range(s.size()):
    reversed_str += s.pop()

print(f"Reversed string for '{str_to_reverse}' is: {reversed_str}")    