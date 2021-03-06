"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:                                                            #<<<
    def __init__(self, value, prev=None, next=None):
        self._value = value
        self._prev = prev
        self._next = next

    @property
    def value(self):
        return self._value
    @property
    def prev(self):
        return self._prev
    @property
    def next(self):
        return self._next

    @value.setter
    def value(self, x):
        self._value = x
    @prev.setter
    def prev(self, x):
        self._prev = x
    @next.setter
    def next(self, x):
        self._next = x

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self._next
        self._next = ListNode(value, self, current_next)
        if current_next:
            current_next._prev = self._next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self._prev
        self._prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev._next = self._prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self._prev:
            self._prev._next = self._next
        if self._next:
            self._next._prev = self._prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class doubleLinkedList:                                                    #<<<
    def __init__(self, node=None):
        self._head = node
        self._tail = node
        self._length = 1 if node is not None else 0

    def __len__(self):
        return self._length
    
    @property
    def head(self):
        return self._head
    @property
    def tail(self):
        return self._tail
    @property
    def length(self):
        return self._length

    @head.setter
    def head(self, x):
        self._head = x
    @tail.setter
    def tail(self, x):
        self._tail = x
    @length.setter
    def length(self, x):
        self._length = x

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        new_node = ListNode(value)
        self._length += 1
        if not self._head and not self._tail:
            self._head = new_node
            self._tail = new_node
        else:
            new_node._next = self._head
            self._head._prev = new_node
            self._head = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        value = self._head._value
        self.delete(self._head)
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        new_node = ListNode(value)
        self._length += 1
        if not self._head and not self._tail:
            self._head = new_node
            self._tail = new_node
        else:
            new_node._prev = self._tail
            self._tail._next = new_node
            self._tail = new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        value = self._tail._value
        self.delete(self._tail)
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        if node is self._head:
            return
        value = node._value
        self.delete(node)
        self.add_to_head(value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if node is self._tail:
            return
        value = node._value
        self.delete(node)
        self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        self._length -= 1

        if self._head is self._tail:
            self._head = None
            self._tail = None
        elif node is self._head:
            self._head = node._next
            node.delete()
        elif node is self._tail:
            self._tail = node._prev
            node.delete()
        else:
            node.delete()

    """Returns the highest value currently in the list"""
    def get_max(self):
        # Loop through all nodes, looking for biggest value
        if not self._head:
            return None
        max_value = self._head._value
        current = self._head
        while current:
            if current._value > max_value:
                max_value = current._value
            current = current._next

        return max_value


if __name__ == "__main__": #>>> <PASS>
    pass