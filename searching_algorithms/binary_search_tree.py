class TreeNode:

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left_child = left
        self.right_child = right

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def search(self, search_value):
        current_node = self.root

        while current_node:
            if current_node.data == search_value:
                return True
            elif current_node.data < search_value:
                current_node = current_node.right_child
            else:
                current_node = current_node.left_child
        return False
    
    def insert(self, data):
        new_node = TreeNode(data)

        if self.root is None:
            self.root = new_node
            return
        else:
            current_node = self.root

            while True:
                if data < current_node.data:
                    if current_node.left_child is None:
                        current_node.left_child = new_node
                        return
                    else:
                        current_node = current_node.left_child
                else:
                    if current_node.right_child is None:
                        current_node.right_child = new_node
                        return
                    else:
                        current_node = current_node.right_child

    def find_min(self):
        if self.root is None:
            return None
        else:
            current_node = self.root

            while current_node.left_child:
                current_node = current_node.left_child
            return current_node.data

def numbered_bst():
    bst = BinarySearchTree()

    bst.insert(47)
    bst.insert(48)
    bst.insert(49)

    return bst

bst = numbered_bst()

print(bst.root.data)                         # 47
print(bst.root.left_child)                   # None
print(bst.root.right_child.data)             # 48
print(bst.root.right_child.right_child.data) # 49

print(bst.search(46)) # False
print(bst.search(47)) # True

print(bst.find_min()) # 47

bst.insert(44)
print(bst.find_min()) # 44
