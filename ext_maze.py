import heapq

def solve_maze(maze, start, end):
    rows = len(maze)
    cols = len(maze[0])

    def is_valid(row, col):
        return 0 <= row < rows and 0 <= col < cols and maze[row][col] == 0

    def heuristic(row, col):
        return abs(row - end[0]) + abs(col - end[1])

    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    cost_so_far = {start: 0}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == end:
            break

        row, col = current
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = row + dr, col + dc
            if is_valid(new_row, new_col):
                new_cost = cost_so_far[current] + 1
                neighbor = (new_row, new_col)
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    priority = new_cost + heuristic(new_row, new_col)
                    heapq.heappush(open_set, (priority, neighbor))
                    came_from[neighbor] = current

    if end not in came_from:
        return None

    path = []
    current = end
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path

# Example usage:
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
start = (0, 0)
end = (4, 4)

path = solve_maze(maze, start, end)

if path:
    print("Path found:")
    for row, col in path:
        print(f"({row}, {col})")
else:
    print("No path found.")
