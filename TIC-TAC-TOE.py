import random

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check if a player has won
def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(row[col] == player for row in board):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2-i] == player for i in range(3)):
        return True

    return False

# Function to check if the board is full
def is_board_full(board):
    return all(board[i][j] != "-" for i in range(3) for j in range(3))

# Minimax function with Alpha-Beta Pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    if check_winner(board, "X"):
        return -1
    if check_winner(board, "O"):
        return 1
    if is_board_full(board):
        return 0

    if is_maximizing:
        max_eval = float("-inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == "-":
                    board[i][j] = "O"
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = "-"
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == "-":
                    board[i][j] = "X"
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = "-"
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Function for the AI's move
def get_ai_move(board):
    best_move = None
    best_eval = float("-inf")
    for i in range(3):
        for j in range(3):
            if board[i][j] == "-":
                board[i][j] = "O"
                eval = minimax(board, 0, False, float("-inf"), float("inf"))
                board[i][j] = "-"
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    return best_move

# Function to start the game
def play_game():
    board = [["-" for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe AI!")

    while not check_winner(board, "X") and not check_winner(board, "O") and not is_board_full(board):
        print_board(board)
        x, y = map(int, input("Enter your move (row and column): ").split())
        while board[x][y] != "-":
            print("Invalid 
            move! Try again.")
            x, y = map(int, input("Enter your move (row and column): ").split())
        board[x][y] = "X"

        if not check_winner(board, "X") and not is_board_full(board):
            ai_move = get_ai_move(board)
            board[ai_move[0]][ai_move[1]] = "O"

    print_board(board)
    if check_winner(board, "X"):
        print("Congratulations! You won!")
    elif check_winner(board, "O"):
        print("AI wins! Better luck next time.")
    else:
        print("It's a draw!")

# Start the game
if __name__ == "__main__":
    play_game()
