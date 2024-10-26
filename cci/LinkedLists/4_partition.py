# Partition a linked list around a value x

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def partition(head, x):
    left_head = ListNode(0)
    right_head = ListNode(0)

    left = left_head
    right = right_head

    current = head
    while current:
        if current.val < x:
            left.next = current
            left = left.next
        else:
            right.next = current
            right = right.next
        current = current.next

    right.next = None

    left.next = right_head.next

    return left_head.next