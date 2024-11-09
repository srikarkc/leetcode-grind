# Check subtree

class TreeNode:
    def __init__(self, value, left, right):
        self.value = 0
        self.left = None
        self.right = None

# Preorder traversal with string matching

def serialize_tree(root):
    if not root:
        return "X"
    return f"{root.value},{serialize_tree(root.left)},{serialize_tree(root.right)}"

def check_subtree(T1, T2):
    T1_str = serialize_tree(T1)
    T2_str = serialize_tree(T2)

    return T2_str in T1_str

# Recursive tree comparison

def are_identical(root1, root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    if root1.value != root2.value:
        return False
    
    return are_identical(root1.left, root2.left) and are_identical(root1.right, root2.right)

def check_subtree_recursive(T1, T2):
    if not T1:
        return False
    if are_identical(T1, T2):
        return True
    
    return check_subtree_recursive(T1.left, T2) or check_subtree_recursive(T1.right, T2)