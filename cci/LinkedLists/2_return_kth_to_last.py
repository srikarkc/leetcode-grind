# 2 pointer technique

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def findKthToLast(head, k):
    first = head
    second = head

    for _ in range(k):
        if not first:
            return None # If k is largers than the length of the list
        first = first.next

    while first:
        first = first.next
        second = second.next
    
    return second