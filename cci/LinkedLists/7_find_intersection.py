# Find intersection of 2 Linked Lists

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None

def findLength(head):
    length = 0
    while current:
        length += 1
        current = current.next
    return length

def find_intersection(headA, headB):

    lenA, lenB = findLength(headA), findLength(headB)

    while lenA > lenB:
        headA = headA.next
        lenA -= 1
    while lenB > lenA:
        headB = headB.next
        lenB -= 1

    while headA and headB:
        if headA == headB:
            return headA
        headA = headA.next
        headB = headB.next

    return None