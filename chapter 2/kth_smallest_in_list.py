''' 
Given a list of numbers in random order write a linear time algorithm to find
the 𝑘th smallest number in the list. Explain why your algorithm is linear.

Can you improve the algorithm from the previous problem to be 𝑂(𝑛 log(𝑛))?
'''

import random
import timeit
from timeit import Timer


def smallest_linear(l, k):
    tries = 1
    while tries <= k:
        # Find smallest
        smallest = None
        for i in l:
            if smallest == None:
                smallest = i
            if i < smallest:
                smallest = i

        # print(tries, "smallest: ", smallest)
        # remove smallest
        l.remove(smallest)    

        tries += 1
    return smallest

def smallest_loglinear(l, k):
    l.sort()
    return l[k-1]

l_size = 20
l = []
for i in range(l_size):
    l.append(random.randrange(10000))
print(f"\nRandomly generated list: ", l, "\n")

k = random.randrange(1, l_size + 1)
print("K is set to: ", k, "\n")

print(f"{k} smallest with linear algorithm is:", smallest_linear(l[:], k))
print(f"{k} smallest with log linear algorithm is:", smallest_loglinear(l[:], k))

linear_time = Timer("smallest_linear(l[:], k)", "from __main__ import smallest_linear, l, k")
loglinear_time = Timer("smallest_loglinear(l[:], k)", "from __main__ import smallest_loglinear, l, k")

print("\nLinear time: ", linear_time.timeit(number=100000))
print("Log Linear time: ", loglinear_time.timeit(number=100000))