
"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node

    def add_to_head(self, value):
        new_head = ListNode(value)
        new_head.next = self.head
        if self.head is not None:
            self.head.prev = new_head
        self.head = new_head

    def remove_from_head(self):
        if self.head is None:
            return None
        if not self.head.next:
            old_head = self.head
            self.head = None
            self.tail = None
            self.head.delete()
            return old_head.value
        else:
            removed_head = self.head
            self.head.delete()
            # self.head = self.head.next
            return removed_head.value

    def add_to_tail(self, value):
        new_tail = ListNode(value)
        if self.head is None:
            self.head = new_tail
        else:
            new_tail.prev = self.tail
            if self.tail is not None:
                self.tail.next = new_tail
            self.tail = new_tail

    def remove_from_tail(self):
        if self.tail is None:
            return None
        if not self.tail.prev:
            old_tail = self.tail
            self.head = None
            self.tail = None
            self.tail.delete()
            return old_tail.value
        else:
            old_tail = self.tail
            self.tail.delete()
            new_tail = self.tail.prev
            # new_tail.next = None
            self.tail = new_tail
            return old_tail.value

    def move_to_front(self, node):
        node.delete()
        self.add_to_head(node.value)

    def move_to_end(self, node):
        node.delete()
        self.add_to_tail(node.value)

    def delete(self, node):
        print(f'head: {self.head} node: {node}')
        if node.next is None and node.prev is not None:
            print('it tail')
            node.prev.next = None
            self.tail = node.prev
            node.delete()
            return node.value
        if node.prev is None and node.next is not None:
            print('it head')
            node.next.prev = None
            self.head = node.next
            node.delete()
            return node.value
        if node.prev is None and node.next is None:
            print('it both')
            self.head = None
            self.tail = None
            node.delete()
            return node.value
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.delete()
            # if node == self.head:
            #     print('it head')
            #     self.head = node.next
            # if node == self.tail:
            #     print('it tail')
            #     self.tail = node.prev
        return node.value

    def get_max(self):
        max_value = int()
        current_node = self.head
        while True:
            if current_node is None:
                return None
            if current_node.value > max_value:
                max_value = current_node.value
            if current_node.next is None:
                return max_value
            else:
                current_node = current_node.next
