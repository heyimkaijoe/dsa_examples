from binary_search_tree import BinarySearchTree

# 3 ways: in-order, pre-order and post-order
# in-order
def in_order(self, current_node):
    if current_node:
        self.in_order(current_node.left_child)
        print(current_node.data)
        self.in_order(current_node.right_child)

# pre-order
def pre_order(self, current_node):
    if current_node:
        print(current_node.data)
        self.pre_order(current_node.left_child)
        self.pre_order(current_node.right_child)

# post-order
def post_order(self, current_node):
    if current_node:
        self.post_order(current_node.left_child)
        self.post_order(current_node.right_child)
        print(current_node.data)

BinarySearchTree.in_order = in_order
BinarySearchTree.pre_order = pre_order
BinarySearchTree.post_order = post_order

bst = BinarySearchTree()

bst.insert(20)
bst.insert(13)
bst.insert(28)
bst.insert(15)
bst.insert(22)
bst.insert(29)
bst.insert(12)

bst.in_order(bst.root)   # print order: 12->13->15->20->22->28->29
bst.pre_order(bst.root)  # print order: 20->13->12->15->28->22->29
bst.post_order(bst.root) # print order: 12->15->13->22->29->28->20
