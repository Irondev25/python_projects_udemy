# global variable
board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]


# games board
def print_board():
    print(board[0][0] + ' ' + board[0][1] + ' ' + board[0][2])
    print(board[1][0] + ' ' + board[1][1] + ' ' + board[1][2])
    print(board[2][0] + ' ' + board[2][1] + ' ' + board[2][2])


# function for user input
def user_input_x(turn):
    x = 0
    print("Its %s turn:" % turn)
    x = int(input("input x co-ordinate:"))
    return x


def user_input_y(turn):
    y = 0
    y = int(input("input y co-ordinate:"))
    return y


# game algorithm


def game_check():
    if board[0][0] == board[0][1] == board[0][2] != '_':
        print(board[0][0] + " Won")
        return 'won'
    elif board[1][0] == board[1][1] == board[1][2] != '_':
        print(board[1][0] + " won")
        return 'won'
    elif board[2][0] == board[2][1] == board[2][2] != '_':
        print(board[2][0] + " won")
        return 'won'
    elif board[0][0] == board[1][0] == board[2][0] != '_':
        print(board[0][0] + " won")
        return 'won'
    elif board[0][1] == board[1][1] == board[2][1] != '_':
        print(board[0][1] + " won")
        return 'won'
    elif board[0][2] == board[1][2] == board[2][2] != '_':
        print(board[0][2] + " won")
        return 'won'
    elif board[0][0] == board[1][1] == board[2][2] != '_':
        print(board[0][0] + " won")
        return 'won'
    elif board[0][2] == board[1][1] == board[2][0] != '_':
        print(board[0][2] + " won")
        return 'won'
    else:
        if no_of_blank_space() != 0:
            return
        else:
            print("The math was draw!!!")


def no_of_blank_space():
    space = 0
    for row in board:
        for ele in row:
            if ele == '_':
                space += 1
    return space


# the main console
def play_ttt():
    turn = 0
    x = 0
    y = 0
    print("Welcome To TicTacToe")
    print("Player 1 in O \nPlayer 2 is X")
    print_board()
    while no_of_blank_space() != 0:
        x = user_input_x(turn)
        y = user_input_y(turn)
        if turn == 0:
            board[x][y] = 'O'
            turn = 1
        else:
            board[x][y] = 'X'
            turn = 0
        if game_check() == 'won':
            print('\n')
            print_board()
            break
        print('\n')
        print_board()
        print('\n')

option = 'y'
while option == 'y':
    play_ttt()
    print('\n')
    option = input("Want to play again(y/n)")
