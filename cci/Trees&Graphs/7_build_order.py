from collections import defaultdict

class Graph:
    def __init__(self, projects, dependencies):
        self.graph = defaultdict(list)
        self.projects = projects
        self.build_graph(dependencies)
    
    def build_graph(self, dependencies):
        for prereq, proj in dependencies:
            self.graph[prereq].append(proj)
    
    def find_build_order(self):
        # Tracking states of nodes: None = unvisited, 'visiting' = in the process, 'visited' = fully processed
        visiting = set()
        visited = set()
        result = []

        def dfs(node):
            if node in visiting:  # Cycle detected
                return False
            if node in visited:  # Node has already been processed
                return True

            # Mark the node as being visited
            visiting.add(node)

            # Visit all neighbors
            for neighbor in self.graph[node]:
                if not dfs(neighbor):  # If a cycle is detected, return False
                    return False

            # Mark the node as fully processed
            visiting.remove(node)
            visited.add(node)

            # Add to build order
            result.append(node)
            return True

        # Start DFS from each node that hasn't been visited
        for project in self.projects:
            if project not in visited:
                if not dfs(project):  # Cycle detected, so no valid build order
                    return None

        # Return result in reverse order
        return result[::-1]
