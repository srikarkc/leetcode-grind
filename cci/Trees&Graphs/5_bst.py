# Check if a binary tree is a binary search tree

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_valid_bst(root):
    def validate(node, min_val, max_val):
        if not node:
            return True

        if not (min_val < node.value < max_val):
            return False

        return (validate(node.left, min_val, node.value) and
                validate(node.right, node.value, max_val))

    return validate(root, float('-inf'), float('inf'))
