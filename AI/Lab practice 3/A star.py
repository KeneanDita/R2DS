import heapq

def a_star(graph, start, goal, heuristics):
    open_list = []
    heapq.heappush(open_list, (0, start))
    g_scores = {node: float('inf') for node in graph}
    g_scores[start] = 0
    parents = {start: None}

    while open_list:
        current_cost, current_node = heapq.heappop(open_list)
        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = parents[current_node]
            return path[::-1]  # Return reversed path
        for neighbor, weight in graph[current_node].items():
            tentative_g_score = g_scores[current_node] + weight
            if tentative_g_score < g_scores[neighbor]:
                g_scores[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristics[neighbor]
                heapq.heappush(open_list, (f_score, neighbor))
                parents[neighbor] = current_node
    return None

# Sample graph and heuristic values for A*
graph_astar = {
    'S': {'A': 1, 'B': 4},
    'A': {'C': 2, 'D': 5},
    'B': {'D': 1},
    'C': {'G': 3},
    'D': {'G': 2},
    'G': {}
}
heuristics = {
    'S': 7,
    'A': 6,
    'B': 5,
    'C': 4,
    'D': 3,
    'G': 0
}

print("\nA* Path:", a_star(graph_astar, 'S', 'G', heuristics))

#output = A* Path: ['S', 'A', 'C', 'G']
# The output of the A* algorithm is the path from start to goal node.