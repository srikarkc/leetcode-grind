# Given a linked list, check if it's a palindrome

def is_palindrome(head):
    if not head or head.next:
        return True
    
    # First, find the middle of the list
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    second_half_start = reverse_list(slow)

    first_half, second_half = head, second_half_start
    palindrome = True
    while palindrome and second_half:
        if first_half.val != second_half.val:
            palindrome = False
        first_half = first_half.next
        second_half = second_half.next

    reverse_list(second_half_start)

    return palindrome

def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev