# This program simulates the 'Tic-Tac-Toe' game.

import sys
import time

playing_field = ['', '', '', '', '', '', '', '', '']
O = 'O'
X = 'X'
MAX = 9
MIN = 1
player_1 = 1
player_2 = 2


# Displays the current status of the game.
def display_game(board):
    print("")
    for i in range(0, 7, 3):
        print(str(board[i]) + '  |  ' + str(board[i + 1])
              + '  |  ' + str(board[i + 2]))
        if i < 4:
            print('------------')
    print("")

# The entry point for the program.
def main(board, o, x):
    print('Tic-Tac-Toe')
    time.sleep(1)
    print('Starting game...')
    time.sleep(1)
    print('Player 1 will be playing as O; player 2 will be playing as X.')
    time.sleep(3)
    display_game(board)
    time.sleep(1)

    for i in range(9):
        if i in [0, 2, 4, 6, 8]:
            while True:
                player_1_input = input('Please enter the box number where you wish to place your \'O\' ' +
                                       'Boxes are numbered from left to right starting from the left most top box. ')
                if check_input_validity(board, player_1_input):
                    update_game(board, player_1_input, player_1)
                    display_game(board)
                    # Start checking for a player_1 win after 2 moves have been played in the game.
                    if i > 2:
                        if check_for_win(board):
                            print('Congratulations player 1! You have won the game.')
                            time.sleep(3)
                            sys.exit()
                    break
                else:
                    continue

        if i in [1, 3, 5, 7]:
            while True:
                player_2_input = input('Please enter the box number where you wish to place your \'X\' ' +
                                       'Boxes are numbered from left to right starting from the left most top box. ')
                if check_input_validity(board, player_2_input):
                    update_game(board, player_2_input, player_2)
                    display_game(board)
                    # Start checking for a player_2 win after 4 moves have been played in the game.
                    if i > 4:
                        if check_for_win(board):
                            print('Congratulations player 2! You have won the game.')
                            time.sleep(3)
                            sys.exit()
                    break
                else:
                    continue
    print('... and that\'s a draw.')

# Checks the validity of an input.
def check_input_validity(board, input):
    try:
        input = int(input)
    except ValueError:
        print('Incorrect input. Try again.')
        return False
    if input > MAX or input < MIN:
        print('Input out of bounds. Try again.')
        return False
    if board[input - 1] == O or board[input - 1] == X:
        print('Incorrect input. Try again.')
        return False
    return True


# Updates the game status
def update_game(board, input, player_no):
    if player_no == player_1:
        board[int(input) - 1] = 'O'
    else:
        board[int(input) - 1] = 'X'


# Checks for a win.
def check_for_win(board):
    for i in range(0, 7, 3):
        if board[i] == board[i + 1] and board[i + 1] == board[i + 2] and board[i + 1] != '':
            return True
    for i in range(0, 3):
        if board[i] == board[i + 3] and board[i + 3] == board[i + 6] and board[i + 3] != '':
            return True
    if board[0] == board[4] and board[4] == board[8] and board[4] != '':
        return True
    if board[2] == board[4] and board[4] == board[6] and board[4] != '':
        return True
    return False


main(playing_field, O, X)
