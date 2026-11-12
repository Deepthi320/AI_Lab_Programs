def water_jug_bfs_tree(jug1_capacity, jug2_capacity, target):
    jug_list = [(0, 0)]   # only state, not path
    visited = set()
    tree_path = []        # to store BFS tree order

    while jug_list:
        jug1, jug2 = jug_list.pop(0)  # If pop(0) -> queue -> BFS; if pop() -> stack -> DFS

        # Record state in BFS tree order
        tree_path.append((jug1, jug2))

        # Stop when target is found
        if jug1 == target or jug2 == target:
            print("BFS Tree Traversal Path:")
            for state in tree_path:
                print(f"Jug1: {state[0]}, Jug2: {state[1]}")
            return

        # Skip visited states
        if (jug1, jug2) in visited:
            continue
        visited.add((jug1, jug2))

        # All possible moves
        possible_moves = [
            (jug1_capacity, jug2),  # Fill jug1
            (jug1, jug2_capacity),  # Fill jug2
            (0, jug2),              # Empty jug1
            (jug1, 0),              # Empty jug2
            (max(0, jug1 - (jug2_capacity - jug2)), min(jug2_capacity, jug2 + jug1)),  # Pour jug1 → jug2
            (min(jug1_capacity, jug1 + jug2), max(0, jug2 - (jug1_capacity - jug1)))   # Pour jug2 → jug1
        ]

        for new_jug1, new_jug2 in possible_moves:
            if (new_jug1, new_jug2) not in visited:
                jug_list.append((new_jug1, new_jug2))


# Example
jug1_capacity = 4
jug2_capacity = 3
target = 2

water_jug_bfs_tree(jug1_capacity, jug2_capacity, target)
