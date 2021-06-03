class Node:

    # default constructor
    def __init__(self, data, next=None, prev=None):
        self._data = data
        self._prev = prev
        self._next = next


class LinkedList:

    def __init__(self):
        self._head = Node(None)
        self._tail = Node(None)
        self._size = 0

    def add_first(self, element):
        if self._size == 0:
            self._head = Node(element)
        elif self._size == 1:
            self._tail = self._head
            self._head = Node(element, self._tail)
            self._tail._prev = self._head
        else:
            new_node = Node(element, self._head)
            self._head._prev = new_node
            self._head = new_node
        self._size += 1

    def add(self, element, index=None):
        if (index != None):
            self._insert_at(element, index)
        else:
            if self._size == 0:
                self._head = Node(element, self._tail)
            elif self._size == 1:
                self._tail = Node(element, None, self._head)
                self._head._next = self._tail
            else:
                new_node = Node(element, None, self._tail)
                self._tail._next = new_node
                self._tail = new_node
            self._size += 1

    def add_all(self, collection):
        for item in collection:
            self.add(item)

    def get_size(self):
        return self._size

    def _insert_at(self, element, index):
        if index > self._size or index < 0:
            raise Exception("Index out of bounds")
        if index == 0:
            return self.add_first(element)
        if index == self._size:
            return self.add(element)

        temp = self._head
        temp_index = 0
        new_node = Node(element)

        while temp != None:
            if index == temp_index:
                new_node._prev = temp._prev
                new_node._next = temp
                if temp._prev:
                    temp._prev._next = new_node
                temp._prev = new_node
            temp_index += 1
            temp = temp._next

        self._size += 1

    def remove_last(self):
        element = None
        if self._size == 0:
            raise Exception("No items to Remove")
        elif self._size == 1 and self._head._data != None:
            element = self._head._data
            self.clear()
        else:
            if self._tail._prev and self._tail._data != None:
                element = self._tail._data
                self._tail = self._tail._prev
                self._tail._next = None
            self._size -= 1

        return element

    def remove_first(self):
        element = None
        if self._head._data == None:
            raise Exception("No items to Remove")
        elif self._size == 1 and self._head._data != None:
            element = self._head._data
            self.clear()
        else:
            element = self._head._data
            if self._head._next:
                self._head = self._head._next
                self._head._prev = None
            self._size -= 1
        return element

    def remove(self, index=None):
        if index != None:
            if index > self._size or index < 0:
                raise Exception("Index out of Bounds")
            if index == 0:
                return self.remove_first()
            if index == self._size:
                return self.remove_last()

            temp = self._head
            temp_index = 0
            element = Node(None)

            while temp != None:
                if index == temp_index:
                    if temp._prev and temp._next:
                        element = temp
                        temp._prev._next = element._next
                        temp._next.prev = element._prev
                        break
                temp_index += 1
                temp = temp._next

            self._size -= 1
            return element._data
        else:
            return self.remove_last()

    def contains(self, element):
        temp = self._head

        while temp != None:
            if element is temp._data:
                return True
            temp = temp._next

        return False

    def get_first(self):
        if self._head._data == None:
            raise Exception("No such Element")
        return self._head._data

    def get_last(self):
        if self._tail._data == None:
            raise Exception("No such Element")
        return self._tail._data

    def index_of(self, element):
        temp = self._head
        index = 0

        while temp != None:
            if temp._data == element:
                return index
            index += 1
            temp = temp._next

        return -1

    def is_empty(self):
        return self._size == 0

    def clear(self):
        self._size = 0
        self._tail = Node(None)
        self._head = Node(None)

    def __str__(self):
        if self._size == 0:
            return "[]"
        temp = self._head
        output = "["

        while temp != None:
            if temp is self._tail:
                output += str(temp._data) + "]"
            else:
                output += str(temp._data) + " <-> "
            temp = temp._next

        return output
