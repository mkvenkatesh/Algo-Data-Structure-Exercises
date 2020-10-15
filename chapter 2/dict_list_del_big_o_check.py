''' 
Devise an experiment that compares the performance of the del operator on
lists and dictionaries. 
'''

import random
import timeit
from timeit import Timer

retries = 1000
for i in range(1000000, 10000000, 1000000):    
    # list del performance check
    x = list(range(i))
    list_del_timer = Timer(f"del x[random.randrange({i-retries})]", "from __main__ import x, random")
    list_del_timer_final = list_del_timer.timeit(number=retries)
    print(f"{retries} random del item from a list on list size of {i}: ", list_del_timer_final)

    # dict del performance check
    x = {k:None for k in range(i)}
    dict_del_timer = Timer(f"del x[random.randrange({i-retries})]", "from __main__ import x, random")
    dict_del_timer_final = dict_del_timer.timeit(number=retries)    
    print(f"{retries} random del item from a dict on dict size of {i}: ", dict_del_timer_final)

