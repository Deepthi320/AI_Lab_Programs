import heapq

graph = {
    'S': [('B', 4), ('C', 3)],
    'B': [('F', 5), ('E', 12)],
    'C': [('D', 7), ('E', 10)],
    'D': [('E', 2)],
    'E': [('G', 5)],
    'F': [('G', 16)],
    'G': []  # Goal node has no neighbors
}

def a_star_all_paths(graph, start, goal, heuristics):
    def reconstruct_path(came_from, current):
        path = []
        while current in came_from:
            path.append(current)
            current = came_from[current]
        path.append(start)
        return path[::-1]

    open_set = []
    heapq.heappush(open_set, (0, start, [], 0))
    all_paths = []

    while open_set:
        current_f_cost, current, path_so_far, g_cost = heapq.heappop(open_set)
        path_so_far = path_so_far + [current]

        # If goal is reached, add the path and its cost
        if current == goal:
            all_paths.append((path_so_far, g_cost))
            continue

        for neighbor, weight in graph[current]:
            tentative_g_cost = g_cost + weight
            f_cost = tentative_g_cost + heuristics.get(neighbor, float('inf'))
            heapq.heappush(open_set, (f_cost, neighbor, path_so_far, tentative_g_cost))

    return all_paths


# Heuristics (estimated cost to goal for each node)
heuristics = {
    'S': 14,
    'B': 12,
    'C': 11,
    'D': 6,
    'E': 4,
    'F': 11,
    'G': 0  # Goal node has heuristic 0
}

# Example usage
start = 'S'
goal = 'G'

all_paths = a_star_all_paths(graph, start, goal, heuristics)

if all_paths:
    print("All paths with their costs:")
    for path, cost in all_paths:
        print(f"Path: {' -> '.join(path)}, Cost: {cost}")

    # Find the optimal path
    optimal_path, optimal_cost = min(all_paths, key=lambda x: x[1])

    print("\nOptimal Path:")
    print(f"Path: {' -> '.join(optimal_path)}, Cost: {optimal_cost}")
else:
    print("No path found.")
