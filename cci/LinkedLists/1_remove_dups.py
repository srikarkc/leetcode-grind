# Remove duplicates from an unsorted linked list

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeDuplicates(head):
    if not head:
        return head
    
    current = head
    prev = None
    seen_values = set()

    while current:
        if current.val in seen_values:
            prev.next = current.next
        else:
            seen_values.add(current.val)
            prev = current
        current = current.next

    return head

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


# Removing without extra space

def removeDuplicatesWithoutExtraSpace(head):
    current = head

    while current:
        runner = current
        while runner.next:
            if runner.next.val == current.val:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next

    return head