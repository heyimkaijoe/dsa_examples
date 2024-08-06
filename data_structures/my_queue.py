# Approach 1
from node import Node

class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
    
    def enqueue(self, data):
        new_node = Node(data)

        if self.head:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node
    
    def dequeue(self):
        if self.head:
            current_node = self.head

            self.head = current_node.next
            current_node.next = None

            if self.head is None:
                self.tail = None

# Approach 2
import queue

queue = queue.SimpleQueue()

queue.put('apple')
queue.put('pen')
print(queue.qsize()) # 2

print(queue.get())   # apple
print(queue.get())   # pen
print(queue.empty()) # True
