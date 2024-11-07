# Find the next node of a given node in a binary search tree

class TreeNode:
    def __init__(self, value=0, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

def find_next_node(node):

    if node.right:
        find_min(node.right)

    current = node
    while current.parent and current.parent.right == current:
        current = current.parent
    
    return current.parent

def find_min(node):
    current = node
    while current.left:
        current = current.left
    return current