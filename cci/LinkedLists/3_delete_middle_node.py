# Remove the middle node given only access to that node

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteMiddle(node):

    if node is None or node.next is None:
        return
    
    node.val = node.next.val
    node.next = node.next.next