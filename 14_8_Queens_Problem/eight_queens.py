def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]."""

    # Check column for conflicts
    for i in range(row):
        if board[i] == col:
            return False

    # Check left diagonal for conflicts
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i] == j:
            return False

    # Check right diagonal for conflicts
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, len(board))):
        if board[i] == j:
            return False

    return True


def solve_n_queens(board, row):
    """Recursively solve the N-Queens problem."""

    if row == len(board):
        return [board[:]]

    solutions = []

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row] = col
            solutions.extend(solve_n_queens(board, row + 1))
            board[row] = -1

    return solutions


def print_solution(solution):
    """Display the chessboard with queens placed."""

    for row in solution:
        print(" ".join("Q" if i == row else "." for i in range(len(solution))))
    print("\n")


# Initialize board and solve the problem
n = 8
board = [-1] * n
solutions = solve_n_queens(board, 0)

print(f"Found {len(solutions)} solutions for the 8-Queens problem.\n")

# Print one solution for demonstration
if solutions:
    print("One of the solutions:")
    print_solution(solutions[0])
