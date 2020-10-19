'''
Convert a decimal number to binary using divide by 2 algorithm. You repeatedly
divide the given decimal number and note down the remainder. The remainders in
reverse order gives you the binary value.

The Divide by 2 algorithm assumes that we start with an integer greater than 0.
A simple iteration then continually divides the decimal number by 2 and keeps
track of the remainder. The first division by 2 gives information as to whether
the value is even or odd. An even value will have a remainder of 0. It will have
the digit 0 in the ones place. An odd value will have a remainder of 1 and will
have the digit 1 in the ones place. We think about building our binary number as
a sequence of digits; the first remainder we compute will actually be the last
digit in the sequence. 

The function divide_by_2 can be modified to accept not only a decimal value but
also a base for the intended conversion. The “Divide by 2” idea is simply
replaced with a more general “Divide by base.” 
'''
from stack import Stack

def div_by_base(dec_val, base):    
    s = Stack()
    hex_dict = {
                10: "a", 
                11: "b", 
                12: "c",
                13: "d",
                14: "e",
                15: "f"
                }

    while dec_val > 0:
        rem = dec_val % base
        if rem > 9:
            rem = hex_dict[rem]
        s.push(rem)
        dec_val = dec_val // base

    binary_result = ""
    while not s.is_empty():
        binary_result += str(s.pop())

    return binary_result


dec_val = 256
base = 16
result = div_by_base(dec_val, base)
print("Decimal", dec_val, "in base", base, "is:", result)

if (base == 2 and ("0b" + result == bin(dec_val))) \
        or (base == 8 and ("0o" + result == oct(dec_val))) \
        or (base == 16 and ("0x" + result == hex(dec_val))):
    print("Result Validation: Success")
else:
    print("Result Validation: Failure")