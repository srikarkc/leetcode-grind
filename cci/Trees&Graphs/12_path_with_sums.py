# Given a binary tree - design an algorithm to count the number of paths that sum to a given value

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def path_sum(root, target_sum):
    def dfs(node, current_sum, prefix_sums):
        if not node:
            return 0

        current_sum += node.value

        path_count =  prefix_sums.get(current_sum - target_sum, 0)

        prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1

        path_count += dfs(node.left, current_sum, prefix_sums)
        path_count += dfs(node.right, current_sum, prefix_sums)

        prefix_sums[current_sum] -= 1
        if prefix_sums[current_sum] == 0:
            del prefix_sums[current_sum]

        return path_count
    
    prefix_sums = {0: 1}
    dfs(root, 0, prefix_sums)