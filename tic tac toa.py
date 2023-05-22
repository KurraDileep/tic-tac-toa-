import random

board = [' '] * 9

def print_board():
    for i in range(0, 9, 3):
        print(' | '.join(board[i:i+3]))

def check_win(player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for combination in winning_combinations:
        if all(board[i] == player for i in combination):
            return True
    return False

def get_computer_move():
    empty_squares = [i for i, val in enumerate(board) if val == ' ']
    return random.choice(empty_squares)

print("Let's play tic-tac-toe!")
print_board()

while True:
    player_move = int(input("Enter your move (0-8): "))
    if board[player_move] != ' ':
        print("Invalid move! Try again.")
        continue
    board[player_move] = 'X'
    print_board()
    if check_win('X'):
        print("Congratulations, you win!")
        break
    if ' ' not in board:
        print("It's a tie!")
        break
    print("Computer is making a move...")
    computer_move = get_computer_move()
    board[computer_move] = 'O'
    print_board()
    if check_win('O'):
        print("Sorry, you lose!")
        break
