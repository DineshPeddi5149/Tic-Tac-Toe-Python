def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print("\n")

def check_winner(board, player):
    # Rows, columns, diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]): return True
        if all([board[j][i] == player for j in range(3)]): return True
    if all([board[i][i] == player for i in range(3)]): return True
    if all([board[i][2 - i] == player for i in range(3)]): return True
    return False

def is_full(board):
    return all(cell in ['X', 'O'] for row in board for cell in row)

def main():
    board = [['1','2','3'], ['4','5','6'], ['7','8','9']]
    current_player = 'X'

    while True:
        print_board(board)
        move = input(f"Player {current_player}, choose a cell (1-9): ")

        if not move.isdigit() or int(move) < 1 or int(move) > 9:
            print("Invalid input. Try again.")
            continue

        row = (int(move) - 1) // 3
        col = (int(move) - 1) % 3

        if board[row][col] in ['X', 'O']:
            print("Cell already taken. Try again.")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()