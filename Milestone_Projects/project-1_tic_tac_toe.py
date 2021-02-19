
# Using the numpad to play tic-tac-toe

def display_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]}")

def player_input():
    playerInput = int(input("Where to place your mark? "))
    return playerInput

def place_marker(board, marker, position):
    print(type(board))
    board[position] = marker

    return board

def win_check(board, mark):
    win1 = [mark,mark,mark,'','','','','','']
    win2 = ['','','',mark,mark,mark,'','','']
    win3 = ['','','','','','',mark,mark,mark]
    win4 = ['X']


def playerTurn(turn):
    if turn == True:
        return 'X'
    else:
        return 'O'


def replay():
    pass

def ticTacToe():
    
    board = ['1','2','3','4','5','6','7','8','9']

    gameOn = True
    turn = True


    while gameOn:

        display_board(board)

        playerMark = playerTurn(turn)

        position = player_input()

        board = place_marker(board, playerMark, position)

        turn = not turn

    
ticTacToe()