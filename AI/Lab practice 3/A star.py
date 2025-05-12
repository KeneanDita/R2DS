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
            return path[::-1]
        for neighbor, weight in graph[current_node].items():
            tentative_g_score = g_scores[current_node] + weight
            if tentative_g_score < g_scores[neighbor]:
                g_scores[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristics[neighbor]
                heapq.heappush(open_list, (f_score, neighbor))
                parents[neighbor] = current_node
    return None

graph_astar = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 2, 'E': 5},
    'C': {'F': 3},
    'D': {'G': 2},
    'E': {'G': 1},
    'F': {'G': 6},
    'G': {}
}
heuristics = {
    'A': 7,
    'B': 6,
    'C': 5,
    'D': 4,
    'E': 3,
    'F': 2,
    'G': 0
}

print("\nA* Path:", a_star(graph_astar, 'A', 'G', heuristics))

#The algorithm traverses through the graph and finds the path with the least cost
#which is through A* Path: ['A', 'B', 'D', 'G']