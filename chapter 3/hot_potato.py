'''
Hot Potato

We will implement a general simulation of Hot Potato. Our program will input a
list of names and a constant, call it “num” to be used for counting. It will
return the name of the last person remaining after repetitive counting by num.
What happens at that point is up to you. 

To simulate the circle, we will use a queue. Assume that the child holding the
potato will be at the front of the queue. Upon passing the potato, the
simulation will simply dequeue and then immediately enqueue that child, putting
her at the end of the line. She will then wait until all the others have been at
the front before it will be her turn again. After num dequeue/enqueue
operations, the child at the front will be removed permanently and another cycle
will begin. This process will continue until only one name remains (the size of
the queue is 1).
'''

from random import randrange
from queues import Queue

def hot_potato(q, num):
    q = Queue()
    for name in name_list:
        q.enqueue(name)

    while q.size() != 1:
        for i in range(num):
            # take the first element and push it to the rear
            q.enqueue(q.dequeue())
        # hot potato! remove the first person from the queue
        q.dequeue()

    return q.dequeue()

if __name__ == "__main__":
    name_list = ["John", "Jack", "Jill", "Jake", "Jane", "Jumbo", "Jimathy"]
    num = randrange(0, 100)
    print("Random num:", num)
    print("Last remaining person is:", hot_potato(name_list, num))