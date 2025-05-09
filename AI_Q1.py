from collections import deque

# Define the graph using an adjacency list
graph = {
    'A': ['B', 'G'],
    'B': ['C', 'D', 'E'],
    'C': [],
    'D': [],
    'E': ['F'],
    'F': [],
    'G': ['H'],
    'H': ['I'],
    'I': [],
}

def bfs(graph, start_node):
    visited = set()            # Set to keep track of visited nodes
    queue = deque([start_node])  # Initialize a queue with the starting node

    while queue:
        current_node = queue.popleft()
        if current_node not in visited:
            print(current_node, end=' ')
            visited.add(current_node)
            # Enqueue all unvisited neighbors
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Execute BFS starting from node 'A'
bfs(graph, 'A')
