# Stacks and Queues

## Stacks

### Introduction to Stacks

A stack is a data structure that follows Last In, First Out (LIFO).

1. push() - add an item to the top of the stack
2. pop() - removes the item from the top of the stack
3. peek() / top() - get the element from the top of the stack
4. isEmpty - check if the stack is empty

```python
stack = []
stack.append(1)
stack.append(2)
stack.pop()
top_item = stack[-1] if stack else None
```

## Queues

### Introduction to Queues

First In, First Out - similar to a movie theatre.

1. Enqueue - adds an item to the end of the queue
2. Dequeue - removes an item from the front of the queue
3. Peek/Front - views the front item without removing it
4. isEmpty - check if queue is empty

Useful for BFS (Breadth first search) in graphs.

```python
from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
queue.popleft()
front_item = queue[0] if queue else None

```
