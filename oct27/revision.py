# 1 - Implement an algorithm to determine if a String has all unique characters

def simpleUniqueChars(inputString):
    
    charSet = set()
    
    for char in inputString:
        if char in charSet:
            return False
        else:
            charSet.add(char)
            
    return True

def uniqueChars(inputString):
    
    bit_counter = 0
    
    for char in inputString:
        
        val = ord(char) - ord('a')
        
        if bit_counter & (1 << val) != 0:
            return False
        else:
            bit_counter |= (1 << val)
            
    return True
        
        

# 2 - Given 2 strings - check if one is a permutation of the other

def check_perm(s1, s2):
    
    if len(s1) != len(s2):
        return False
        
    return sorted(s1) == sorted(s2)
    
# Time complexity for the above solution is O(nlogn) which is for the sorting algorithm.

def check_perm(s1, s2):
    
    if len(s1) != len(s2):
        return False
    
    char_dict = {}
    
    for char in s1:
        char_dict[char] = char_dict.get(char, 0) + 1
        
    for char in s2:
        if char not in char_dict or char_dict[char] == 0:
            return False
            
        char_dict[char] -= 1
    
    return True
    
# The above solution has an O(n) time complexity.
    
 
# 3 - Write a method to replace all the spaces in a string with '%20'

def urlify(string, true_length):
    
    string = string[:true_length]
    
    return string.replace(' ', '%20')
    

def urlify_optimized(char_array, true_length):
    
    index = len(char_array)
    
    for i in range(index - 1, -1, -1):
        if char_list[i] == ' ':
            char_list[index - 3:index] = '%20'
            index -= 3
        else:
            char_list[index - 1] = char_list[i]
            index -= 1

    return ''.join(char_list)
    
    
# 4 - Palindrome permutation

def pal_perm(input_string):
    
    char_dict = {}
    
    for char in input_string.replace(" ", "").lower():
        char_dict[char] = char_dict.get(char, 0) + 1
        
        
    # Check for at most one odd count
    single_odd_found = False
    for count in char_dict.values():
        if count % 2 != 0:
            if single_odd_found:
                return False
            single_odd_found = True
                
    return True
    
# The above solution has a time complexity of O(n) and space complexity of O(k)

def pal_perm_efficient(input_string):
    
    bit_vector = 0
    
    def toggle_bit(bit_vector, index):
        mask = (1 << index)
        
        if (bit_vector & mask) != 0:
            bit_vector &= ~mask
        else:
            bit_vector |= mask
            
        return bit_vector
        
    for char in input_string.replace(" ", "").lower():
        index = ord(char) - ord('a')
        
        if 0 <= index < 26:
            bit_vector = toggle_bit(bit_vector, index)
            
    return (bit_vector == 0) or (bit_vector & (bit_vector - 1) == 0)
    
# The above solution has a time complexity of O(n) and space complexity of O(1)



# 5 - One Away problem

# I know this is NOT a sorting problem. Insert / remove / replace a character.

def one_away(s1, s2):
    
    if abs(len(s1) - len(s2)) > 1:
        return False
    
    # ensure s2 is longer
    if len(s1) > len(s2):
        s1, s2 = s2, s1
        
    index1 = 0
    index2 = 0
    found_difference = False
    
    while index1 < len(s1) and index2 < len(s2):
        if s1[index1] != s2[index2]:
            if found_difference:
                return False
            found_difference = True
            
            if len(s1) != len(s2):
                index2 += 1
                continue
                
        index1 += 1
        index2 += 1
        
    return True
    
 
 
# 6 - String Compression

def string_comp(input_string):
    
    if len(input_string == 0):
        return ""
    
    char_list = []
    count = 1
    
    for i in range(1, len(input_string)):
        if input_string[i - 1] == input_string[i]:
            count += 1
        else:
            char_list.append(input_string[i - 1])
            char_list.append(count)
            count = 1
            
    char_list.append(input_string[-1])
    char_list.append(count)
    
    compressed_string = ''.join(char_list)
    
    return compressed_string if len(compressed_string) < len(input_string) else input_string
    


# 7 - Rotate matrix

def rotate_matrix(input_matrix):
    
    row_count = len(input_matrix)
    
    for i in range(row_count):
        for j in range(i, row_count):
            input_matrix[i,j], input_matrix[j, i] = input_matrix[j,i], input_matrix[i,j]
            
            
    for row in row_count:
        input_matrix[row].reverse()
        
    return input_matrix
    
    
# 8 - Zero matrix

# going for the optimized solution

def set_zero_optimized(matrix):
    
    if not matrix or not matrix[0]:
        return
        
    M, N = len(matrix), len(matrix[0])
    
    first_row_has_zero = any(matrix[0][j] == 0 for j in range(N))
    first_col_has_zero = any(matrix[i][0] == 0 for i in range(M))
    
    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0
                
    # zero rows based on markers
    for i in range(1, M):
        if matrix[i][0] == 0:
            for j in range(N):
                matrix[i][j] = 0
                
    for j in range(1, N):
        if matrix[0][j] == 0:
            for i in range(M):
                matrix[i][j] = 0
                
    if first_row_has_zero:
        for j in range(N):
            matrix[0][j] = 0
            
    if first_col_has_zero:
        for i in range(M):
            matrix[i][0] = 0
            
           
           

# 9 - String rotation

def string_rotation(s1, s2):
    
    if len(s1) != len(s2):
        return False
    
    return s2 in s1+s1
    
    
 
 '''
 
 Linked Lists
 
 '''
 
 # General Linked List
 
 class Node:
     def __init__(self, data):
         self.val = data
         self.next = None
         
class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        
    def print_list(self):
        current = self.head
        while current:
            print(current.head + "->")
            current = current.next
        print("None")
        
# The shorter form used in most questions

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
# Print the linked list

def print_list(head):
    current = head
    while current:
        print(current.val, end="->")
        current = current.next
    print("None")
    
# Find the length of the linked list

def get_length(head):
    length = 0 
    current = head
    while current:
        length += 1
        current = current.next
    return length
    
# Insert a node at the beginning of a linked list

def insert_node(head, value):
    new_node = ListNode(value)
    new_node.next = head
    return new_node
   
# Insert a node at the end of a linked list

def insert_node_end(head, value):
    new_node = ListNode(value)
    if not head:
        return new_node
    current = head
    while current:
        current = current.next
    current.next = new_node
    
# Delete a node by value

def delete_node(head, value):
    if not head:
        return None
    if head.val == value:
        return head.next # remove the head
        
    current = head
    while current.next and current.next.val != value:
        current = current.next
    if current.next:
        current.next = current.next.next
        
    return head

# Reverse a linked list

def reverse(head):
    current = head
    prev = None
    
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
        
    return head
    
# Find a node by value
def find_node(head, value):
    current = head
    while current:
        if current.val = value:
            return current
        current.next
    return None
    
# Detect a cycle in the linked list

# use 2 pointers (slow & fast) - if there's a cycle, they will meet

def has_cycle(head):
    
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
    
# Find the middle of the linked list

def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
    
# Merge 2 sorted linked lists

def merge_two_sorted_lists(l1, l2):
    dummy = ListNode()
    current = dummy
    
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    
    current.next = l1 if l1 else l2 if l2
    return dummy.next
    
    
    
# 2.1 - remove dups from a linked list

def remove_dups(head):
    if not head:
        return None
        
    current = head
    val_set = set()
    val_set.add(current.val)
    
    while current and current.next:
        if current.next.val in val_set:
            current.next = current.next.next
         else:
             val_set.add(current.next.val)
        current = current.next
        
    return head
    
# same problem without a temporary buffer - no set()

def remove_dups_without_buffer(head):
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

# the solution without a buffer has O(n^2) time complexity


# 2.2 - Return kth to last element of a single linked list

def return_k_last_element(head, k):
    
    first = second = head
    
    for _ in range(k):
        if not first:
            return None
        first = first.next
        
    while first:
        first = first.next
        second = second.next
        
    return second
    
    
# 2.3 - delete middle node given the node itself

def delete_middle_node(node):
    
    node.val = node.next.val
    node.next = node.next.next
    
    return True
    

# 2.4 - write code to partition a linked list around x

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
    
    
    
# 2.5 - sum lists

def sum_lists(l1, l2):
    
    dummy = ListNode(0)
    current = dummy
    carry = 0
    
    while l1 or l2 or carry:
        val1 = l1 if l1 else 0
        val2 = l2 if l2 else 0
        sum = val1 + val2 + carry
        
        carry = sum % 10
        new_digit = sum // 10
        
        current.next = ListNode(new_digit)
        current = current.next
    
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    
    return dummy.next
    
# 2.6 - Implement a function to check if a linkedlist is a palindrome

def check_pal_ll(head):
    
    fast, slow = head, head
    
    # first middle of the list
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
    
# 2.7 - Intersection of 2 linked lists

# if 2 linked lists intersect, they will have the same last node from the intersection point onward

def get_length(head):
    length = 0
    while head:
        length += 1
        head = head.next
    return length
    
def find_intersection(headA, headB):
    
    lenA, lenB = get_length(headA), get_length(headB)
    
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
    
    
# 2.8 - Check for loop in a linked list

def check_loop(head):
    
    if not head or not head.next:
        return None
    
    slow, fast = head, head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return slow
            
    return None