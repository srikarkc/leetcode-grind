from collections import deque

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def list_of_depths_linked_list(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        head = ListNode(0)
        current = head

        for _ in range(level_size):
            node = queue.popleft()

            current.next = ListNode(node.value)
            current = current.next

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(head.next)

    return result