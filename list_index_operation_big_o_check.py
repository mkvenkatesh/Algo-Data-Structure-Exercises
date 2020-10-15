'''
Devise an experiment to verify that the list index operator is 𝑂(1).

'''
import random
import timeit
from timeit import Timer

for i in range(1000000, 10000000, 1000000):
    x = list(range(i))
    t1 = Timer(f"x[random.randrange({i})] = None", "from __main__ import x, random")
    print(f"10000 list index access operation on list size of {i}: ", t1.timeit(number=10000))

