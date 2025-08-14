# Function to print the current board
def print_board(board):
    print("\nCurrent Board:")
    for row in board:
        # Print each row with separators
        print(" | ".join(row))
        print("-" * 5)
    print()

# Function to check if a player has won
def check_winner(board, player):
    # Check all rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True

    # Check all columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True

    # Check both diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    # If no win condition is met
    return False

# Function to check if the board is full (no empty cells)
def is_full(board):
    for row in board:
        for cell in row:
            if cell != 'X' and cell != 'O':
                return False
    return True

# Main function to run the game
def main():
    # Create a 3x3 board with numbers 1 to 9
    board = [['1', '2', '3'],
             ['4', '5', '6'],
             ['7', '8', '9']]

    # Player X starts first
    current_player = 'X'

    print("Welcome to Tic-Tac-Toe!")
    print("Players take turns choosing a cell number (1–9).")

    # Game loop
    while True:
        # Show the board
        print_board(board)

        # Ask the current player for their move
        move = input(f"Player {current_player}, enter your move (1–9): ")

        # Check if the input is a number
        if not move.isdigit():
            print("Please enter a number between 1 and 9.")
            continue

        # Convert input to an integer
        move = int(move)

        # Check if the number is within the valid range
        if move < 1 or move > 9:
            print("Invalid cell number. Choose between 1 and 9.")
            continue

        # Calculate row and column from the move
        row = (move - 1) // 3
        col = (move - 1) % 3

        # Check if the chosen cell is already taken
        if board[row][col] == 'X' or board[row][col] == 'O':
            print("That cell is already taken. Try a different one.")
            continue

        # Place the player's symbol on the board
        board[row][col] = current_player

        # Check if the current player has won
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins! 🎉")
            break

        # Check if the board is full (draw)
        if is_full(board):
            print_board(board)
            print("It's a draw! 🤝")
            break

        # Switch to the other player
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'

# Run the game
if __name__ == "__main__":
    main()