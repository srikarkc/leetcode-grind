# Give two numbers represented by Linked Lists, write a function that adds the 2 numbers and returns the sum as a LinkedList

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sum_list(l1, l2):
    dummy = ListNode(0)
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        val1 = l1 if l1 else 0
        val2 = l2 if l2 else 0
        
        sum = val1 + val2 + carry

        carry = sum // 10
        new_digit = sum % 10

        # Create a new node for the result and move the pointer
        current.next = ListNode(new_digit)
        current = current.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy.next