class Node:
    def __init__(self, data=None, next=None):
        self._data = data
        self._next = next

    def update_data(self, data):
        self._data = data

    def set_next(self, node):
        self._next = node

    def get_data(self):
        return self._data

    def get_next(self):
        return self._next


class LinkedList:
    def __init__(self):
        self._head = None

    def add_head(self, data : object) -> None:
        new_node = Node(data)
        new_node.set_next(self._head)
        self._head = new_node
        del new_node

    def get_tail_node(self) -> Node:
        temp = self._head
        while temp is not None and temp._next is not None:
            temp = temp._next
        return temp

    def add_tail(self, data : object)-> bool:
        new_node = Node(data)
        if self._head is None:
            self._head = new_node
            return True
        tail = self.get_tail_node()
        tail.set_next(new_node)
        return True


    def remove_tail(self):
        temp = self._head
        while temp is not None:
            if temp.get_next()._next is not None:
                temp = temp.get_next()
            else:
                break
        del temp

    def print_list(self):
        temp = self._head
        while temp is not None:
            print(temp.get_data(), end=" ")
            temp = temp.get_next()


linked_list = LinkedList()
linked_list.add_tail(10)
linked_list.add_tail(26)
linked_list.add_tail(34)
linked_list.print_list()
