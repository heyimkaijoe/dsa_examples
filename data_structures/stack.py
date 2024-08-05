from node import Node

class Stack:

    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)

        if self.top:
            new_node.next = self.top
        self.top = new_node
    
    def pop(self):
        if self.top is None:
            return None
        else:
            popped_node = self.top

            self.top = popped_node.next
            popped_node.next = None
            return popped_node.data
    
    def peek(self):
        if self.top:
            return self.top.data
        else:
            return None
