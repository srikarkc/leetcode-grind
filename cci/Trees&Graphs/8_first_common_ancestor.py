# common ancestor

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def find_common_ancestor(root, p, q):
    if not root or root == p or root == q:
        return root
    
    left = find_common_ancestor(root.left, p, q)
    right = find_common_ancestor(root.right, p, q)

    if left and right:
        return root
    
    return left if left else right