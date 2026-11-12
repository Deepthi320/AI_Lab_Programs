class Node:
    def __init__(self, name, heuristic=0, is_and=False):
        self.name = name
        self.heuristic = heuristic
        self.children = []
        self.is_and = is_and
        self.optimal_path = []

    def add_child(self, child, cost=1):
        self.children.append((child, cost))


def ao_star(node):
    if not node.children:
        print(f"{node.name} is a leaf node with heuristic {node.heuristic}.")
        return node.heuristic

    print(f"Evaluating node {node.name} with initial heuristic {node.heuristic}.")

    costs = []
    paths = []

    for child_group in node.children:
        total_cost = 0
        group_path = []

        for child, cost in child_group:
            child_cost = cost + ao_star(child)
            total_cost += child_cost
            group_path.append((child.name, child_cost))

        costs.append(total_cost)
        paths.append(group_path)

    best_index = costs.index(min(costs))
    best_cost = costs[best_index]

    node.optimal_path = paths[best_index]

    print(f"Best cost for {node.name} is updated to {best_cost}. Optimal path: {node.optimal_path}")

    node.heuristic = best_cost
    return best_cost


# Create nodes based on the example
A = Node("A")
B = Node("B")
C = Node("C", is_and=True)
D = Node("D", is_and=True)
E = Node("E", heuristic=7)
F = Node("F", heuristic=9)
G = Node("G", heuristic=3)
H = Node("H", heuristic=0)
I = Node("I", heuristic=0)
J = Node("J", heuristic=0)

# Define connections (child groups)
A.children = [
    [(B, 1)],
    [(C, 1), (D, 1)]
]

B.children = [
    [(E, 1)],
    [(F, 1)]
]

C.children = [
    [(G, 1)],
    [(H, 1), (I, 1)]
]

D.children = [
    [(J, 1)]
]

# Run AO* algorithm on the root node
print("Starting AO* algorithm...\n")
optimal_cost = ao_star(A)


# Function to print the optimal path
def print_optimal_path(node, current_path=None):
    if current_path is None:
        current_path = []

    current_path.append(node.name)

    for child_name, _ in node.optimal_path:
        child_node = next(
            n for n in [A, B, C, D, E, F, G, H, I, J]
            if n.name == child_name
        )
        print_optimal_path(child_node, current_path)

    return current_path


optimal_path = print_optimal_path(A, [])

print(f"\nOptimal Cost for A: {optimal_cost}")
print(f"Optimal Path: {' -> '.join(optimal_path)}")
