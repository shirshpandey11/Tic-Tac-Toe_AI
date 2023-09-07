import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def minimax(board, depth, is_maximizing):
    scores = {"X": 1,"O": -1,"draw": 0}
    if check_winner(board, "X"):
        return scores["X"]
    if check_winner(board, "O"):
        return scores["O"]
    empty_cells = get_empty_cells(board)
    if not empty_cells:
        return scores["draw"]
    if is_maximizing:
        max_score = float("-inf")
        for i, j in empty_cells:
            board[i][j] = "X"
            score = minimax(board, depth + 1, False)
            board[i][j] = " "
            max_score = max(max_score, score)
        return max_score
    else:
        min_score = float("inf")
        for i, j in empty_cells:
            board[i][j] = "O"
            score = minimax(board, depth + 1, True)
            board[i][j] = " "
            min_score = min(min_score, score)
        return min_score

def get_best_move(board):
    best_score = float("-inf")
    best_move = None
    for i, j in get_empty_cells(board):
        board[i][j] = "X"
        score = minimax(board, 0, False)
        board[i][j] = " "
        if score > best_score:
            best_score = score
            best_move = (i, j)
    return best_move

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Tic Tac Toe - You are O and the AI is X")
    print_board(board)

    while True:
        player_row = int(input("Enter row (0, 1, or 2): "))
        player_col = int(input("Enter column (0, 1, or 2): "))
        if board[player_row][player_col] == " ":
            board[player_row][player_col] = "O"
            print_board(board)
            if check_winner(board, "O"):
                print("You win!")
                break
            elif not get_empty_cells(board):
                print("It's a draw!")
                break
            ai_row, ai_col = get_best_move(board)
            board[ai_row][ai_col] = "X"
            print("AI's move:")
            print_board(board)
            if check_winner(board, "X"):
                print("AI wins!")
                break
            elif not get_empty_cells(board):
                print("It's a draw!")
                break
        else:
            print("Cell already occupied. Try again.")
if __name__ == "__main__":
    main()
