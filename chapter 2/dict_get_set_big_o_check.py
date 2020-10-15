'''
Devise an experiment to verify that get item and set item are 𝑂(1) for dictionaries.

'''
import random
import timeit
from timeit import Timer

retries = 100000
for i in range(1000000, 10000000, 1000000):
    x = {k:None for k in range(i)}
    t1 = Timer(f"temp = x[random.randrange({i})]", "from __main__ import x, random")
    get_time = t1.timeit(number=retries)
    t1 = Timer(f"x[random.randrange({i})] = {i}", "from __main__ import x, random")
    set_time = t1.timeit(number=retries)
    print(f"{retries} random get, set item from a dictionary operation on dict size of {i}: ", get_time, ", ", set_time)

