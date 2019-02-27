
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
        if self.head:
            old_head = self.head
            old_head.insert_before(value)

            self.head = self.head.prev
        else:
            self.head = ListNode(value)
            self.tail = self.head

    def remove_from_head(self):
        if self.head:
            if self.head == self.tail:
                head = self.head
                self.head = None
                self.tail = None
                return head.value
            else:
                old_head = self.head
                self.head = old_head.next
                old_head.delete()
                return old_head.value
        else:
            return None

    def add_to_tail(self, value):
        if self.tail:
            self.tail.insert_after(value)
            self.tail = self.tail.next

        else:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node

    def remove_from_tail(self):
        if self.tail:

            old_tail = self.tail
            if self.tail == self.head:
                self.tail = None
                self.head = None
                return old_tail.value
            else:
                self.tail = old_tail.prev
                old_tail.delete()
            return old_tail.value
        else:
            return None

    def move_to_front(self, node):
        node.delete()
        self.add_to_head(node.value)

    def move_to_end(self, node):
        node.delete()
        self.add_to_tail(node.value)

    def delete(self, node):
        if not self.head and not self.tail:
            return None
        if self.head == self.tail:
            self.head = None
            self.tail = None
        if self.head == node:
            self.head = node.next
            node.delete()
        if self.tail == node:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()

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
