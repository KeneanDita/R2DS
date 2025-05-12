import heapq

graph = {
    'S': [('A', 1), ('C', 4), ('G', 12)],
    'A': [('B', 3), ('C', 1)],
    'B': [('D', 3)],
    'C': [('D', 1), ('G', 2)],
    'D': [('G', 3)],
    'G': []
}

def ucs(start, goal):
    frontier = [(0, start, [])]
    visited = set()

    while frontier:
        cost, node, path = heapq.heappop(frontier)

        if node in visited:
            continue

        visited.add(node)
        path = path + [node]

        if node == goal:
            return path, cost

        for neighbor, edge_cost in sorted(graph[node]):
            if neighbor not in visited:
                heapq.heappush(frontier, (cost + edge_cost, neighbor, path))

path, total_cost = ucs('S', 'G')
print("a)")
print("UCS Path:", path)
print("Total Cost:", total_cost)

#output: UCS Path: ['S', 'A', 'C', 'G']
# Total Cost: 4




print("""
b)
(i) Is h1 admissible?
No, because h1(S) = 5 > actual cost from S to G (4).

(ii) Is h2 admissible?
Yes, since for all nodes h2(n) ≤ actual cost to goal.

"""# h1 is not admissible because it overestimates the cost from S to G.
# h2 is admissible because it does not overestimate the cost from S to G.
)