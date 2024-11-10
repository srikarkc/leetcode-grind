# Given a binary search tree - print all possible arrays

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
def bst_sequences(root):
    if not root:
        return [[]]
    
    result = []
    left_seq = bst_sequences(root.left)
    right_seq = bst_sequences(root.right)

    for left in left_seq:
        for right in right_seq:
            weaved = []
            weave_lists(left, right, [root.value], weaved)
            result.extend(weaved)

    return result

def weave_lists(left, right, prefix, results):
    if not left or not right:
        results.append(prefix + left + right)
        return
    
    head_left = left[0]
    weave_lists(left[1:], right, prefix + [head_left], results)

    head_right = right[0]
    weave_lists(left, right[1:], prefix + [head_right], results)