import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Check if someone has won
def check_winner(board, player):
    # Rows, columns, diagonals
    win_cond = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]
    return [player, player, player] in win_cond

# Get available moves
def get_available_moves(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]

# Simple strategy: random move
def random_strategy(board):
    return random.choice(get_available_moves(board))

# Slightly smarter strategy: win or block if possible
def smart_strategy(board, player, opponent):
    # Try to win
    for r, c in get_available_moves(board):
        board[r][c] = player
        if check_winner(board, player):
            board[r][c] = " "
            return (r, c)
        board[r][c] = " "

    # Try to block opponent
    for r, c in get_available_moves(board):
        board[r][c] = opponent
        if check_winner(board, opponent):
            board[r][c] = " "
            return (r, c)
        board[r][c] = " "

    # Otherwise random
    return random_strategy(board)

# Play the game
def play_game(strategy_X, strategy_O):
    board = [[" "]*3 for _ in range(3)]
    current_player = "X"

    for turn in range(9):
        print_board(board)

        if current_player == "X":
            r, c = strategy_X(board)
        else:
            r, c = strategy_O(board)

        board[r][c] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            return

        current_player = "O" if current_player == "X" else "X"

    print_board(board)
    print("It's a draw!")

# Example: Random vs Smart strategy
play_game(random_strategy, lambda b: smart_strategy(b, "O", "X"))
