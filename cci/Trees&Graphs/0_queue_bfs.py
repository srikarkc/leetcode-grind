from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            print(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    