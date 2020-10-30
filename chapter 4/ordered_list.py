'''
Ordered List

The structure of an ordered list is a collection of items where each item holds
a relative position that is based upon some underlying characteristic of the
item. The ordering is typically either ascending or descending and we assume
that list items have a meaningful comparison operation that is already defined.
Many of the ordered list operations are the same as those of the unordered list.

• OrderedList() creates a new ordered list that is empty. It needs no parameters
and returns an empty list.
• add(item) adds a new item to the list making sure that the order is preserved.
It needs the item and returns nothing. Assume the item is not already in the
list.
• remove(item) removes the item from the list. It needs the item and modifies
the list. Assume the item is present in the list.
• search(item) searches for the item in the list. It needs the item and returns
a boolean value.
• is_empty() tests to see whether the list is empty. It needs no parameters and
returns a boolean value.
• size() returns the number of items in the list. It needs no parameters and
returns an integer.
• index(item) returns the position of item in the list. It needs the item and
returns the index. Assume the item is in the list.
• pop() removes and returns the last item in the list. It needs nothing and
returns an item. Assume the list has at least one item.
• pop(pos) removes and returns the item at position pos. It needs the position
and returns the item. Assume the item is in the list.
'''

class Node:
    def __init__(self, item):
        self.data = item
        self.next = None
    
    def get_data(self):
        return self.data
    
    def set_data(self, item):
        self.data = item

    def get_next(self):
        return self.next
    
    def set_next(self, node):
        self.next = node

class OrderedList:
    def __init__(self):
        '''
        OrderedList() creates a new ordered list that is empty. It needs no parameters
        and returns an empty list
        '''
        self.head = None

    def add(self, item):
        '''
        add(item) adds a new item to the list making sure that the order is
        preserved. It needs the item and returns nothing. Assume the item is not
        already in the list
        '''
        print("Adding item to list:", item)
        new_node = Node(item)
        if not self.head:
            self.head = new_node
        else:
            ptr = self.head
            prev_ptr = None
            while True:
                if ptr and (ptr.get_data() < item):
                    prev_ptr = ptr
                    ptr = ptr.get_next()
                else:
                    if not prev_ptr:                        
                        self.head = new_node
                        new_node.set_next(ptr)
                    else:
                        prev_ptr.set_next(new_node)
                        new_node.set_next(ptr)    
                    break                

    def remove(self, item):
        '''
        remove(item) removes the item from the list. It needs the item and
        modifies the list. Assume the item is present in the list
        '''
        print("Remove from list:", item)
        ptr = self.head
        prev_ptr = None
        while ptr:
            if ptr.get_data() == item:
                if not prev_ptr:
                    self.head = ptr.get_next()
                else:
                    prev_ptr.set_next(ptr.get_next())
            
            prev_ptr = ptr
            ptr = ptr.get_next()

    def search(self, item):
        '''
        search(item) searches for the item in the list. It needs the item and
        returns a boolean value.
        '''
        ptr = self.head
        while ptr:
            if ptr.get_data() == item:
                return True
            ptr = ptr.get_next()
        
        return False

    def is_empty(self):
        '''
        is_empty() tests to see whether the list is empty. It needs no
        parameters and returns a boolean value.
        '''
        return self.head == None

    def size(self):
        '''
        size() returns the number of items in the list. It needs no parameters
        and returns an integer.
        '''
        l_size = 0
        ptr = self.head
        while ptr:
            l_size += 1
            ptr = ptr.get_next()
        return l_size

    def index(self, item):
        '''
        index(item) returns the position of item in the list. It needs the item
        and returns the index. Assume the item is in the list.
        '''
        idx = 0
        ptr = self.head
        while ptr:
            if ptr.get_data() == item:
                return idx
            ptr = ptr.get_next()
            idx += 1

    def pop(self, pos=None):
        '''
        pop() removes and returns the last item in the list. It needs nothing
        and returns an item. Assume the list has at least one item
        '''
        ret_data = None
        ptr = self.head
        prev_ptr = None
        if pos == None:
            if not ptr:
                return
            elif not ptr.get_next():
                ret_data = ptr.get_data()
                self.head = None
            else:
                while ptr.get_next():
                    prev_ptr = ptr
                    ptr = ptr.get_next()
                ret_data = ptr.get_data()
                prev_ptr.set_next(None)
        else:            
            '''
            pop(pos) removes and returns the item at position pos. It needs the
            position and returns the item. Assume the item is in the list
            '''
            if not ptr:
                return
            elif pos == 0 and not ptr.get_next():
                ret_data = ptr.get_data()
                self.head = None
            else:
                idx = 0
                while ptr:
                    if idx == pos:
                        if not prev_ptr:
                            ret_data = ptr.get_data()
                            self.head = ptr.get_next()
                        else:
                            ret_data = ptr.get_data()
                            prev_ptr.set_next(ptr.get_next())
                    prev_ptr = ptr
                    ptr = ptr.get_next()
                    idx += 1
                
        return ret_data

    def __str__(self):
        retstr = "List: ["
        ptr = self.head
        while ptr:
            retstr += str(ptr.get_data())
            ptr = ptr.get_next()
            if ptr:
                retstr += ", "

        retstr += "]"
        return retstr

if __name__ == "__main__":
    l = OrderedList()
    print(l)
    print("List size:", l.size())
    l.add(10)
    print(l)
    l.add(5)
    print(l)
    l.add(15)
    print(l)
    l.add(15)
    print(l)
    l.add(0)
    print(l)
    l.add(12)
    print(l)
    print("List size:", l.size())
    l.remove(12)
    print(l)
    l.remove(0)
    print(l)        
    l.remove(15)
    print(l)
    print("Search for 15:", l.search(15))
    print("Search for 5:", l.search(5))
    print("Search for 0:", l.search(0))
    print("List size:", l.size())
    print("Index of 5:", l.index(5))
    print("Index of 15:", l.index(15))
    print("Index of 15:", l.index(1))
    print(l)
    print("Pop item:", l.pop())
    print(l)
    print("Pop item:", l.pop())
    print(l)
    print("Pop item:", l.pop())
    print(l)
    print("Pop item:", l.pop())
    l.add(15)
    l.add(10)
    l.add(5)
    print(l)
    print("Pop item at pos 1:", l.pop(1))
    print(l)
    print("Pop item at pos 0:", l.pop(0))
    print(l)
    print("Pop item at pos 0:", l.pop(0))
    print(l)