from binary_search_tree import BinarySearchTree
from queue import SimpleQueue

def bfs(self):
    if self.root:
        visited_node = []

        bfs_queue = SimpleQueue()
        bfs_queue.put(self.root)

        while not bfs_queue.empty():
            current_node = bfs_queue.get()
            visited_node.append(current_node.data)

            if current_node.left_child:
                bfs_queue.put(current_node.left_child)

            if current_node.right_child:
                bfs_queue.put(current_node.right_child)
    
    return visited_node

BinarySearchTree.bfs = bfs

bst = BinarySearchTree()

bst.insert(47)
bst.insert(48)
bst.insert(49)
bst.insert(42)
bst.insert(45)
bst.insert(46)

print(bst.bfs()) # [47, 42, 48, 45, 49, 46]
