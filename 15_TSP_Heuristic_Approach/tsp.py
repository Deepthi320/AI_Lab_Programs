def tsp_nearest_neighbor(dist_matrix, start=0):

    n = len(dist_matrix)
    unvisited = set(range(n))  # Set of unvisited cities
    unvisited.remove(start)    # Start city is initially visited
    path = [start]             # Initialize path with the start city
    current_city = start
    total_cost = 0

    # Build the path
    while unvisited:
        # Find the nearest unvisited city
        next_city = min(unvisited, key=lambda city: dist_matrix[current_city][city])
        total_cost += dist_matrix[current_city][next_city]
        path.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    # Return to the start city to complete the tour
    total_cost += dist_matrix[current_city][start]
    path.append(start)

    return path, total_cost


# Example usage with a distance matrix
dist_matrix = [
    [0, 29, 20, 21],
    [29, 0, 15, 17],
    [20, 15, 0, 28],
    [21, 17, 28, 0]
]

start_city = 0
path, total_cost = tsp_nearest_neighbor(dist_matrix, start=start_city)

print("Approximate TSP Path:", path)
print("Total Distance:", total_cost)
