'''
Queues

The queue abstract data type is defined by the following structure and
operations. A queue is structured, as described above, as an ordered collection
of items which are added at one end, called the “rear,” and removed from the
other end, called the “front.” Queues maintain a FIFO ordering property. The
queue operations are given below.

• Queue() creates a new queue that is empty. It needs no parameters and returns
an empty queue.
• enqueue(item) adds a new item to the rear of the queue. It needs the item and
returns nothing.
• dequeue() removes the front item from the queue. It needs no parameters and
returns the item. The queue is modified.
• is_empty() tests to see whether the queue is empty. It needs no parameters and
returns a boolean value.
• size() returns the number of items in the queue. It needs no parameters and
returns an integer.

'''

class Queue:
    def __init__(self):
        self.q = []

    def enqueue(self, item):
        self.q.append(item)
    
    def dequeue(self):
        return self.q.pop(0)

    def size(self):
        return len(self.q)
    
    def is_empty(self):
        return self.q == []

    def __str__(self):
        retstr = ""
        for num in self.q:
            retstr += str(num) + " "

        return retstr

if __name__ == "__main__":
    q = Queue()
    
    print("Queue is empty?:", q.is_empty())

    print("Enqueue: hello")
    q.enqueue("hello")

    print("Enqueue: world")
    q.enqueue("world")

    print("Enqueue: 33")
    q.enqueue(33)

    print("Queue size:", q.size())
    print("Dequeue:", q.dequeue())
    print("Queue size:", q.size())
    print("Queue is empty?:", q.is_empty())