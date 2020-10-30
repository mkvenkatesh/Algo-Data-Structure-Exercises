'''
Deque (pronounced as "deck") ADT

Deque are double ended queues where inserts and removals can happen at either
end. Note that this is different from the work "dequeue" which is an operation
on the Queue ADT.

The deque abstract data type is defined by the following structure and
operations. A deque is structured, as described above, as an ordered collection
of items where items are added and removed from either end, either front or
rear. The deque operations are given below.

• Deque() creates a new deque that is empty. It needs no parameters and returns
an empty deque.
• add_front(item) adds a new item to the front of the deque. It needs the item
and returns nothing.
• add_rear(item) adds a new item to the rear of the deque. It needs the item and
returns nothing.
• remove_front()removes the front item from the deque.It needs no parameters and
returns the item. The deque is modified.
• remove_rear() removes the rear item from the deque. It needs no parameters and
returns the item. The deque is modified.
• is_empty() tests to see whether the deque is empty. It needs no parameters and
returns a boolean value.
• size() returns the number of items in the deque. It needs no parameters and
returns an integer.

'''

class Deque:
    def __init__(self):
        self.d = []

    def add_front(self, item):
        self.d.insert(0, item)
    
    def add_rear(self, item):
        self.d.append(item)
    
    def remove_front(self):
        return self.d.pop(0)
    
    def remove_rear(self):
        return self.d.pop()

    def size(self):
        return len(self.d)

    def is_empty(self):
        return self.d == []


if __name__ == "__main__":
    d = Deque()
    print("\nDeque is empty?:", d.is_empty())
    print("Add 5 to the front")
    d.add_front(5)
    print("Add 'code' to the rear")
    d.add_rear('code')
    print("Add 10 to the front")
    d.add_front(10)
    print("Deque size:", d.size())
    print("Deque is empty?:", d.is_empty())
    print("\nDeque:", d.d, "\n")
    
    print("Remove item from front:", d.remove_front())
    print("Remove item from rear:", d.remove_rear())
    print("\nDeque:", d.d, "\n")
    print("Remove item from rear:", d.remove_rear())
    print("Deque is empty?:", d.is_empty())