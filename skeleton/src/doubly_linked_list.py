from src.linked_list_node import LinkedListNode


class DoublyLinkedList:
    def __init__(self):
        self._head: LinkedListNode | None = None
        self._tail: LinkedListNode | None = None
        self._count = 0

    @property
    def is_empty(self):
        if self._count == 0:
            return True
        elif self._count >= 1:
            return False

    @property
    def count(self):
        return self._count

    @property
    def head(self):
        return self._head

    @property
    def tail(self):
        return self._tail

    def add_first(self, value):
        node = LinkedListNode(value)
        if self.is_empty:
            self._head = node
            self._tail = node
        else:
            node.next = self._head
            self._head.prev = node
            self._head = node

        self._count += 1

    def add_last(self, value):
        raise NotImplementedError()

    def insert_after(self, node, value):
        raise NotImplementedError()

    def insert_before(self, node, value):
        raise NotImplementedError()

    def remove_first(self):
        raise NotImplementedError()

    def remove_last(self):
        raise NotImplementedError()

    def find(self, value):
        raise NotImplementedError()

    def values(self):
        values_tuple = ()
        if not self.is_empty:
            current = self._head
            while current is not None:
                values_tuple += (current.value,)
                current = current.next

        return values_tuple

    def _insert_before_head(self, value):
        raise NotImplementedError()

    def _insert_after_tail(self, value):
        raise NotImplementedError()
