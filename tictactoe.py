board = [" " for _ in range(9)]

# Display the Tic Tac Toe board
def print_board():
    for row in range(3):
        print("|".join(board[row*3:(row+1)*3]))
        if row < 2:
            print("-----")

# Check if the game has a winner
def check_winner(player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    return any(all(board[i] == player for i in combo) for combo in winning_combinations)

# AI move: Picks the first empty spot
def ai_move():
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            break

# Player's move
def player_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] == " ":
                board[move] = "X"
                break
            else:
                print("That spot is taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Enter a number between 1 and 9.")

# Main game loop
def main():
    print("Welcome to Tic Tac Toe!")
    print("You are X, AI is O")
    print_board()

    while True:
        # Player's turn
        player_move()
        print_board()
        if check_winner("X"):
            print("Congratulations, you win!")
            break
        if " " not in board:
            print("It's a draw!")
            break

        # AI's turn
        ai_move()
        print("AI's move:")
        print_board()
        if check_winner("O"):
            print("AI wins!")
            break
        if " " not in board:
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()