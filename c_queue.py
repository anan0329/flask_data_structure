class Node:
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node

class Queue:
    """First-In-First-Out"""
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """insert to queue"""
        if self.tail is None and self.head is None:
            self.tail = self.head = Node(data, None)
            return

        self.tail.next_node = Node(data, None)
        self.tail = self.tail.next_node
        return

    def dequeue(self):
        """remove from queue"""
        if self.head is None:
            return None
        removed = self.head
        self.head = self.head.next_node
        if self.head is None: # case when there is only a node in the queue
            self.tail = None
        return removed
