# Linked Lists

## Basics

```python
class Node:
    def __init__(self, data):
        self.data = data
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
```

### Main Problems to Solve

Easy:

1. Reverse a Linked List
2. Detect Cycle in a Linked List
3. Find the Middle of a Linked List

Medium:

1. Remove N-th Node From End of List
2. Merge Two Sorted Linked Lists
3. Add Two Numbers (where each number is represented by a linked list)

Hard:

1. Reverse Nodes in k-Group
2. Copy List with Random Pointer
3. Merge k Sorted Lists

---

### Problem 3 - Delete middle node


