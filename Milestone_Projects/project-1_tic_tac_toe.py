import os
# Using the numpad to play tic-tac-toe

def display_board(board):
    print(f"   |   |  ")
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print(f"---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print(f"---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print(f"   |   |  ")

def clearTerminal():
    os.system('clear')

def player_input(mark):
    print("\n")
    playerInput = int(input(f"Player {mark}, make your mark: "))
    return playerInput

def place_marker(board, marker, position):
    board[position-1] = marker

    return board

def win_check(board, mark):
   
    return ((board[0] == mark and board[1] == mark and board[2] == mark) or # Horiz top
           (board[3] == mark and board[4] == mark and board[5] == mark) or # Horiz middle
           (board[6] == mark and board[7] == mark and board[8] == mark) or # Horiz bottom
           (board[0] == mark and board[3] == mark and board[6] == mark) or # Vert left
           (board[1] == mark and board[4] == mark and board[7] == mark) or # Vert mid
           (board[2] == mark and board[5] == mark and board[8] == mark) or # Vert right
           (board[0] == mark and board[4] == mark and board[8] == mark) or # Diag LtoR
           (board[2] == mark and board[4] == mark and board[6] == mark)) # Diag RtoL
           



def playerTurn(turn):
    if turn == True:
        return 'X'
    else:
        return 'O'


def replay():
    print("\n")
    playMore = input("Would you like to play again? ")

    if playMore.lower() == "y":
        return True
    else:
        return False

def resetBoard():
    return ['1','2','3','4','5','6','7','8','9']

def ticTacToe():
    
    board = ['1','2','3','4','5','6','7','8','9']

    gameOn = True
    turn = True
    win = False
    moves = 0


    while gameOn:

        clearTerminal()

        display_board(board)

        playerMark = playerTurn(turn)

        position = player_input(playerMark)

        board = place_marker(board, playerMark, position)

        win = win_check(board, playerMark)
        if win:
            print("\n")
            print(f"PLAYER {playerMark} WINS!")
            gameOn = replay()
            if gameOn:
                board = resetBoard()
                moves = 0
        elif moves == 8:
            print("\n")
            print("IT'S A TIE!")
            gameOn = replay()
            if gameOn:
                board = resetBoard();
                moves = 0
        else:
            moves += 1
            turn = not turn
    clearTerminal()

    
ticTacToe()