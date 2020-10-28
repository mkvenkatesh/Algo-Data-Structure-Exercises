'''
Unordered List ADT

A linked list can be used to implement the unordered list ADT.

The structure of an unordered list is a collection of items where each item
holds a relative position with respect to the others. Some possible unordered
list operations are given below.
• List() creates a new list that is empty. It needs no parameters and returns an
empty list.
• add(item) adds a new item to the list. It needs the item and returns nothing.
Assume the item is not already in the list.
• remove(item) removes the item from the list. It needs the item and modifies
the list. Assume the item is present in the list.
• search(item) searches for the item in the list. It needs the item and returns
a boolean value.
• is_empty() tests to see whether the list is empty. It needs no parameters and
returns a boolean value.
• size() returns the number of items in the list. It needs no parameters and
returns an integer.
• append(item) adds a new item to the end of the list making it the last item in
the collection. It needs the item and returns nothing. Assume the item is not
already in the list.
• index(item) returns the position of item in the list. It needs the item and
returns the index. Assume the item is in the list.
• insert(pos,item) adds a new item to the list at position pos. It needs the
item and returns nothing. Assume the item is not already in the list and there
are enough existing items to have position pos.
• pop() removes and returns the last item in the list. It needs nothing and
returns an item. Assume the list has at least one item.
• pop(pos) removes and returns the item at position pos. It needs the position
and returns the item. Assume the item is in the list.

'''

class Node:
    def __init__(self, data):
        self.next = None
        self.data = data
    
    def get_data(self):
        return self.data
    
    def set_data(self, data):
        self.data = data
    
    def get_next(self):
        return self.next
    
    def set_next(self, node):
        self.next = node


class List:
    def __init__(self):
        '''List() creates a new list that is empty. It needs no parameters and
            returns an empty list.'''
        self.head = None

    def add(self, item):
        '''add(item) adds a new item to the list. It needs the item and returns
            nothing. Assume the item is not already in the list.'''
        print("Add to list:", item)
        new_node = Node(item)
        new_node.set_next(self.head)
        self.head = new_node

    def remove(self, item):
        '''remove(item) removes the item from the list. It needs the item and
            modifies the list. Assume the item is present in the list.'''
        print("Remove from list:", item)
        ptr = self.head
        prev_ptr = None
        
        while ptr != None:
            if ptr.get_data() == item:
                if prev_ptr == None:
                    self.head = ptr.get_next()
                else:
                    prev_ptr.set_next(ptr.get_next())
            
            prev_ptr = ptr
            ptr = ptr.get_next()

    def search(self, item):
        '''search(item) searches for the item in the list. It needs the item and
            returns a boolean value.'''
        print("Search in list:", item)
        ptr = self.head
        while ptr != None:
            if ptr.get_data() == item:
                return True
            ptr = ptr.get_next()
        return False

    def is_empty(self):
        '''is_empty() tests to see whether the list is empty. It needs no
            parameters and returns a boolean value.'''
        if self.head == None:
            return True
        else:
            return False

    def size(self):
        '''size() returns the number of items in the list. It needs no
            parameters and returns an integer'''
        ptr = self.head
        size = 0
        while ptr != None:
            size += 1
            ptr = ptr.get_next()
        
        return size

    def append(self, item):
        '''append(item) adds a new item to the end of the list making it the
            last item in the collection. It needs the item and returns nothing.
            Assume the item is not already in the list''' 
        print("Append to list:", item)       
        ptr = self.head
        while True:
            if ptr.get_next() == None:
                ptr.set_next(Node(item))
                break
            ptr = ptr.get_next()

    def index(self, item):
        '''index(item) returns the position of item in the list. It needs the
            item and returns the index. Assume the item is in the list'''
        ptr = self.head
        index = 0
        while ptr != None:
            if ptr.get_data() == item:
                return index
            ptr = ptr.get_next()
            index += 1

    def insert(self, pos, item):
        '''insert(pos,item) adds a new item to the list at position pos. It
            needs the item and returns nothing. Assume the item is not already
            in the list and there are enough existing items to have position
            pos'''
        print("Inserting", item, "in position:", pos)
        if pos == 0:
            self.add(item)
        elif pos >= self.size():
            self.append(item)
        else:
            ptr = self.head
            prev_ptr = None
            idx = 0
            while ptr != None:
                if idx == pos:
                    new_node = Node(item)
                    new_node.set_next(ptr)
                    prev_ptr.set_next(new_node)
                    break                    
               
                idx += 1
                prev_ptr = ptr
                ptr = ptr.get_next()

    def pop(self, pos=-1):
        '''pop() removes and returns the last item in the list. It needs nothing
            and returns an item. Assume the list has at least one item'''    
        if pos == -1:
            ptr = self.head   
            prev_ptr = None
            while ptr.get_next() != None:
                prev_ptr = ptr
                ptr = ptr.next
            ret_data = ptr.data
            prev_ptr.set_next(None)
            return ret_data
        else:
            '''pop(pos) removes and returns the item at position pos. It needs the
            position and returns the item. Assume the item is in the list'''    
            idx = 0
            ptr = self.head
            prev_ptr = None            
            while ptr != None:
                if idx == pos:
                    if prev_ptr == None:
                        self.head = ptr.get_next()                
                    else:
                        prev_ptr.set_next(ptr.get_next())
                    ret_data = ptr.get_data()
                    return ret_data

                prev_ptr = ptr
                ptr = ptr.get_next()
                idx += 1

    def __str__(self):
        retstr = "List: "
        ptr = self.head
        while ptr != None:
            retstr += str(ptr.get_data()) + " "
            ptr = ptr.get_next()
        return retstr

if __name__ == "__main__":    
    l = List()
    l.add(10)
    l.add(20)
    l.add(30)
    print(l)
    l.remove(10)
    print(l)
    l.remove(30)
    print(l)
    l.remove(20)
    print(l)
    print("List is empty?", l.is_empty())
    print("List Size:", l.size())
    l.add(20)    
    l.add(30)
    l.add(40)
    print(l)
    print("Found:", l.search(40))
    print("Found:", l.search(20))
    print("Found:", l.search(90))
    print("List is empty?", l.is_empty())
    print("List Size:", l.size())
    print(l)
    l.append(10)
    print(l)
    print(f"Index of {40} is:", l.index(40))
    print(f"Index of {10} is:", l.index(10))
    print(f"Index of {30} is:", l.index(30))
    print(f"Index of {300} is:", l.index(300))
    print(l)
    l.insert(0, 50)
    print(l)
    l.insert(1, 45)
    print(l)
    l.insert(5, 15)
    print(l)
    l.insert(10, 0)
    print(l)
    print("Pop from list:", l.pop())
    print(l)
    print("Pop from list:", l.pop())
    print(l)
    print("Pop from list at pos 0:", l.pop(0))
    print(l)
    print("Pop from list at pos 4:", l.pop(4))
    print(l)
    print("Pop from list at pos 1:", l.pop(1))
    print(l)