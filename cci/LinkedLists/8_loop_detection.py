# Given a circular linked list, return node at the beginning of the loop

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def circular_linked_list(head):
    if not head or head.next:
        return None

    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return slow
        
    return None