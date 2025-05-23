import heapq

def aStar(graph, heuristic, start, goal):
    open_heap = [(heuristic[start], 0, start, [start])]  # (f, g, current, path)
    visited = {}

    while open_heap:
        f, g_current, node, path = heapq.heappop(open_heap)

        if node == goal:
            return path, g_current

        if node in visited and visited[node] <= g_current:
            continue
        visited[node] = g_current

        for neighbor, cost in graph[node].items():
            g = g_current + cost
            h = heuristic[neighbor]
            heapq.heappush(open_heap, (g + h, g, neighbor, path + [neighbor]))

    return None, float('inf')



# Input Graph and Heuristic
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5, 'E': 12},
    'C': {'A': 4, 'B': 2, 'D': 2},
    'D': {'B': 5, 'C': 2, 'E': 3},
    'E': {'D': 3}
}

heuristic = {
    'A': 7, 'B': 6, 'C': 2, 'D': 1, 'E': 0
}

# Run the function
path, cost = aStar(graph, heuristic, 'A', 'E')
print("Path:", path)
print("Total cost:", cost)
