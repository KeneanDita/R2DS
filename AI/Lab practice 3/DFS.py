def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")
    for next_node in graph[start] - visited:
        dfs(graph, next_node, visited)
    return visited

graph_dfs = {
    '0': set(['1', '2']),
    '1': set(['0', '3', '4']),
    '2': set(['0']),
    '3': set(['1']),
    '4': set(['2', '3'])
}

dfs(graph_dfs, '0')