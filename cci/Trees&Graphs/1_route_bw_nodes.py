# Route between nodes

# represent the graph as an adjacency list

# bfs solution

from collections import deque

def route_between_nodes(graph, start, end):
    if start == end:
        return True
    
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node == end:
            return True
        
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)

    return False

# dfs solution

def dfs(graph, start, end, visited=set()):
    if start == end:
        return True
    
    visited.add(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            if dfs(graph, neighbor, end, visited):
                return True
    return False