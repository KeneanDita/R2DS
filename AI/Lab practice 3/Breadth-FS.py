def bfs(graph, start):
    visited = []  # List to keep track of visited nodes.
    queue = []    # Initialize a queue
    visited.append(start)
    queue.append(start)
    while queue:
        s = queue.pop(0)  # Dequeue a vertex from the front
        print(s, end=" ")  # Print the current node
        for neighbor in graph[s]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

graph_bfs = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

bfs(graph_bfs, 'A')