'''
Deque (pronounced as "deck") ADT using Doubly Linked List

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

class Node:
    def __init__(self, data = None):
        self.next = None
        self.prev = None
        self.data = data

    def get_data(self):
        return self.data
    
    def set_data(self, data):
        self.data = data
    
    def get_next(self):
        return self.next
    
    def set_next(self, node):
        self.next = node
    
    def get_prev(self):
        return self.prev
    
    def set_prev(self, node):
        self.prev = node

class DequeDLL:
    def __init__(self):
        '''
        DequeDLL() creates a new deque that is empty. It needs no parameters and returns
        an empty deque.
        '''
        self.head = None
        self.tail = None

    def add_front(self, data):
        '''add_front(item) adds a new item to the front of the deque. It needs
        the item and returns nothing'''
        print(f"Adding {data} to front of the queue")
        old_head = self.head
        new_node = Node(data)
        
        self.head = new_node        
        if old_head:
            new_node.set_next(old_head)
            old_head.set_prev(new_node)
        else:
            self.tail = new_node

    def add_rear(self, data):
        '''add_rear(item) adds a new item to the rear of the deque. It needs the item and
        returns nothing.'''
        print(f"Adding {data} to rear of the queue")
        old_tail = self.tail
        new_node = Node(data)
        
        self.tail = new_node
        if old_tail:
            old_tail.set_next(new_node)
            new_node.set_prev(old_tail)
        else:
            self.head = new_node

    def remove_front(self):
        '''remove_front()removes the front item from the deque.It needs no
        parameters and returns the item. The deque is modified.'''

        print("Remove node at front of the queue: ", end="")
        if self.is_empty():
            return None
    
        ret_data = self.head.get_data()
        self.head = self.head.get_next()
        if self.head:
            self.head.set_prev(None)

        return ret_data

    def remove_rear(self):
        '''remove_rear()removes the rear item from the deque.It needs no
        parameters and returns the item. The deque is modified.'''

        print("Remove node at rear of the queue: ", end="")
        if self.is_empty():
            return None      

        ret_data = self.tail.get_data()
        self.tail = self.tail.get_prev()
        if self.tail:
            self.tail.set_next(None)

        return ret_data

    def is_empty(self):
        '''is_empty() tests to see whether the deque is empty. It needs no parameters and
        returns a boolean value.'''
        return self.head == None

    def size(self):
        '''size() returns the number of items in the deque. It needs no parameters and
        returns an integer.'''
        ptr = self.head
        size = 0
        while ptr:
            size += 1
            ptr = ptr.get_next()
        return size

    def __str__(self):
        ptr = self.head
        ret_str = ""
        while ptr:
            ret_str += str(ptr.get_data()) + " "
            ptr = ptr.get_next()
        return ret_str


if __name__ == "__main__":
    d = DequeDLL()
    print(d.remove_front())
    print(d.remove_rear())
    print("Queue Is Empty? ", d.is_empty())
    print("Queue size: ", d.size())
    d.add_front(10)    
    print(d)
    print("Queue Is Empty? ", d.is_empty())
    print("Queue size: ", d.size())
    d.add_front(20)
    print(d)
    d.add_front(30)
    print(d)    
    d.add_rear(40)
    print(d)
    d.add_front(35)
    print(d)
    d.add_rear(30)
    print(d)
    d.add_rear(10)
    print(d)    
    print("Queue size: ", d.size())
    print(d.remove_front())
    print(d.remove_rear())
    print(d.remove_front())
    print(d)
    print(d.remove_rear())
    print(d.remove_rear())
    print(d.remove_rear())
    print(d)