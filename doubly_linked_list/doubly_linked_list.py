
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
        if self.head is None:
            self.head = ListNode(value)
            self.tail = ListNode(value)
        else:
            new_head = ListNode(value)
            new_head.next = self.head
            new_head.prev = new_head
            self.head = new_head

    def remove_from_head(self):
        if self.head == None:
            return self.head.value
        else:
            removed_head = self.head
            self.head = self.head.next
            return removed_head.value

    def add_to_tail(self, value):
        new_tail = ListNode(value)
        new_tail.prev = self.tail
        self.tail.next = new_tail
        self.tail = new_tail

    def remove_from_tail(self):
        old_tail = self.tail
        new_tail = self.tail.prev
        new_tail.next = None
        self.tail = new_tail
        return old_tail.value

    def move_to_front(self, node):
        node.delete()
        self.add_to_head(node.value)

    def move_to_end(self, node):
        node.delete()
        self.add_to_tail(node.value)

    def delete(self, node):
        pass

    def get_max(self):
        pass
