# Create a binary search tree with minimal height

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def minimal_tree(sorted_array):
    return create_minimal_bst(sorted_array, 0, len(sorted_array) - 1)

def create_minimal_bst(arr, start, end):

    if start > end:
        return None
    
    mid = (start + end) // 2
    node = TreeNode(arr[mid])

    node.left = create_minimal_bst(arr, start, mid - 1)
    node.right = create_minimal_bst(arr, start + 1, end)

    return node
