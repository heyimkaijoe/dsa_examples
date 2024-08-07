class TreeNode:

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left_child = left
        self.right_child = right

# Build a binary tree
node1 = TreeNode('B')
node2 = TreeNode('C')
node3 = TreeNode('A', node1, node2)
print(node3.left_child.data)  # B
print(node3.right_child.data) # C
