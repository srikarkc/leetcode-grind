# Trees and Graphs - ch. 4

## Introduction

1. Binary Tree - Each node has *UP TO* 2 children.

2. Binary Search Tree - A binary tree that follows a particular sorting order

Inequality must be true for all of node's descendents, not just its immediate children.

---
---

## 1. Trees
A **tree** is a hierarchical data structure consisting of nodes connected by edges, with the following properties:

- **Acyclic**: There are no cycles in a tree; it’s a connected graph with exactly one path between any two nodes.
- **Rooted Structure**: Trees typically have a **root** node, from which all other nodes branch.
- **Parent-Child Relationship**: Each node has a **parent** (except the root) and **children** (nodes it directly points to).
- **Leaf Nodes**: Nodes with no children are called **leaves**.
- **Depth and Height**:
  - **Depth**: The number of edges from the root to a node.
  - **Height**: The maximum depth of any node in the tree.

### Types of Trees
1. **Binary Tree**: Each node has at most two children, often referred to as **left** and **right**.
   - **Binary Search Tree (BST)**: A binary tree where the left child is smaller than the parent, and the right child is larger, facilitating fast search operations.
2. **Balanced Tree**: A tree in which the heights of left and right subtrees differ by at most one.
   - **AVL Tree** and **Red-Black Tree** are common types of balanced binary trees.
3. **Binary Heap**: A binary tree often used to implement priority queues. It is complete (all levels are filled except possibly the last one), and follows the heap property (max-heap or min-heap).
4. **Trie**: A tree used for storing a dynamic set of strings, where each node represents a character. Used commonly in word search and autocomplete applications.

### Common Tree Operations
- **Insertion and Deletion**: Adding or removing nodes while maintaining the tree properties.
- **Traversal**: Visiting nodes in a specific order:
  - **Inorder** (left, root, right): Common for BSTs; yields sorted order.
  - **Preorder** (root, left, right): Useful for copying the tree.
  - **Postorder** (left, right, root): Useful for deleting nodes.
  - **Level Order**: Visit nodes level by level; uses a queue for breadth-first traversal.

### Example of Tree Operations in Python (Binary Tree Traversal)

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=" ")
        inorder_traversal(root.right)

# Example Usage
root = Node(1)
root.left = Node(2)
root.right = Node(3)
inorder_traversal(root)  # Output: 2 1 3
```

---

## 2. Graphs
A **graph** is a more general data structure than a tree and consists of nodes (vertices) connected by edges. Unlike trees, graphs can contain **cycles** and are not hierarchical by default.

### Key Characteristics
- **Directed vs. Undirected**:
  - **Directed Graph (Digraph)**: Each edge has a direction, indicating a one-way relationship (e.g., the web or Twitter followers).
  - **Undirected Graph**: Edges have no direction, meaning relationships are two-way (e.g., Facebook friends).
- **Weighted vs. Unweighted**:
  - **Weighted Graph**: Edges have weights or costs associated with them (e.g., road networks with distances).
  - **Unweighted Graph**: Edges have no weight, representing only the connections.
- **Cycles and Acyclic Graphs**:
  - **Cyclic Graph**: Contains at least one cycle.
  - **Acyclic Graph**: Contains no cycles; **Directed Acyclic Graphs (DAGs)** are particularly useful in applications like task scheduling.

### Graph Representation
1. **Adjacency Matrix**: A 2D array where each cell `(i, j)` represents an edge between nodes `i` and `j`.
   - Pros: Quick lookups for edges; useful for dense graphs.
   - Cons: Requires O(V^2) space, where V is the number of vertices.
2. **Adjacency List**: A list where each element represents a node, and contains a list of all adjacent nodes.
   - Pros: More memory-efficient for sparse graphs; easier to iterate neighbors.
   - Cons: Slower lookups for specific edges.

### Graph Traversal
1. **Depth-First Search (DFS)**: Explores as far down one path as possible before backtracking. Implemented using recursion or a stack.
2. **Breadth-First Search (BFS)**: Explores all neighbors at the present depth before moving on to nodes at the next depth level. Implemented using a queue.

### Example of Graph Representation and Traversal

```python
# Graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# BFS Traversal
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            queue.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)

bfs(graph, 'A')  # Output: A B C D E F
```

### Common Applications
- **Trees**:
  - **Binary Search Trees** for efficient searching and sorting.
  - **Heaps** for implementing priority queues.
  - **Tries** for fast prefix-based search (e.g., autocomplete).
- **Graphs**:
  - **Social Networks** where people or accounts are nodes and relationships are edges.
  - **Road Networks** with cities as nodes and roads with distances as edges.
  - **Dependency Resolution** in package managers or task scheduling with DAGs.

---

### Differences between Trees and Graphs

| Feature          | Tree                                                | Graph                                            |
|------------------|-----------------------------------------------------|--------------------------------------------------|
| Structure        | Hierarchical, acyclic                               | General, can be cyclic                           |
| Connectivity     | Exactly one path between any two nodes              | Multiple paths may exist between nodes           |
| Root Node        | Has a root node (often)                             | No root node required                            |
| Leaf Nodes       | Has leaf nodes                                      | Not necessarily                                  |
| Use Cases        | Hierarchical data (e.g., file systems, family tree) | Complex networks (e.g., social networks, maps)   |

### Summary
- **Trees** are specialized types of graphs with hierarchical structures and no cycles. They’re used in scenarios needing ordered, searchable, or hierarchical data.
- **Graphs** are versatile, representing a wide range of relationships with or without direction, weights, or cycles. They’re suited for more complex and interconnected data structures.

