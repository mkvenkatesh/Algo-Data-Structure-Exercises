'''
Use timeit module to performance analyze the various ways to create a list.
The time returned by timeit is in microseconds
'''

import timeit
from timeit import Timer

# List creation using list concatenation
def list_concat():
    l = []
    for i in range(10000):
        l = l + [i]

# List creation using append function
def list_append():
    l = []
    for i in range(10000):
        l.append(i)

# List creation using list comprehension
def list_comprehension():
    l = [i for i in range(10000)]

# List creation using list comprehension
def list_range():
    l = list(range(10000))

x1 = list(range(2000000))
x2 = list(range(2000000))

# the test statement " from ..." below imports the function from main namespace
# to timeit's namespace. The timeit module does this because it wants to run the
# timing tests in an environment that is uncluttered by any stray variables you
# may have created, that may interfere with your function’s performance in some
# unforeseen way.
t1 = Timer("list_concat()", "from __main__ import list_concat")
t2 = Timer("list_append()", "from __main__ import list_append")
t3 = Timer("list_comprehension()", "from __main__ import list_comprehension")
t4 = Timer("list_range()", "from __main__ import list_range")
t5 = Timer("x1.pop()", "from __main__ import x1")
t6 = Timer("x2.pop(0)", "from __main__ import x2")

print("List concatenation: ", t1.timeit(number=100))
print("List append: ", t2.timeit(number=100))
print("List comprehension: ", t3.timeit(number=100))
print("List range: ", t4.timeit(number=100))
print("List pop: ", t5.timeit(number=100))
print("List pop(0): ", t6.timeit(number=100))