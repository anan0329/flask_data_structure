class Node:
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node


class Stack:
    """Last-In-First-Out First-In-Last-Out"""
    def __init__(self):
        self.top = None

    def peek(self):
        return self.top
    
    def push(self, data):
        """Only add to the head of the stack(linked list)"""
        next_node = self.top
        new_top = Node(data, next_node)
        self.top = new_top

    def pop(self):
        if self.top is None:
            return None
        removed = self.top
        self.top = self.top.next_node
        return removed
