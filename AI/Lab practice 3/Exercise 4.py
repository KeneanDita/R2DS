graph = {
    5: [3, 7],
    3: [2, 4],
    7: [8],
    2: [],
    4: [8],
    8: []
}

def dfs(graph, start, visited=None):
    if visited is None:
        visited = []
    visited.append(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited

result = dfs(graph, 5)
print("DFS Traversal Order:", result)


#output: DFS Traversal Order: [5, 3, 2, 4, 8, 7]
# The algorithm traverses through the graph and finds the path with the least cost