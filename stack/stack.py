"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
from singly_linked_list import LinkedList


class Stack:
    def __init__(self):
        self._stack = 0
        self._size = LinkedList()

    def __len__(self):
        return self._stack

    def push(self, value):
        self._size.add_to_tail(value)
        self._stack += 1

    def pop(self):
        if self.__len__() < 1:
            return
        self._stack -= 1
        return self._size.remove_tail()


if __name__ == "__main__":
    pass

# import pkgutil
# search_path = ['.'] # set to None to see all modules importable from sys.path
# all_modules = [x[1] for x in pkgutil.iter_modules(path=search_path)]
# print(all_modules)

# Ran 4 tests in 0.000s
# OK