#! python3
# Tic tac toe
import random

# function to draw board
def drawBoard(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

# function to get letter from player
def getPlayerLetter():
    print(" X or O ? ")
    while True:
        answer = input().upper()
        print(answer, type(answer))
        if len(answer) != 1:
            print(" Choose ONE letter")
        elif answer == 'X' or answer == 'O':
            return answer
        else:
            print(" Choose X or O")


# function to decide who begins first
def firstPlayer():
    players = ['player', 'computer']
    return random.choice(players)

# function to get player move
def getplayerMove(board, letter):
    moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while True:
        move = int(input())
        if move not in moves:
            print(" Add valid move!")

        elif checkFreeSpace(board, move):
            print(checkFreeSpace(board, move))
            return move
        else:
            print("Try again!")


# check if space is free
def checkFreeSpace(board, move):
    move = int(move)
    return str(board[move]) == ' '

# function to get computer move
def getComputerMove(board, computerLetter):
    # given a board and computer letter, determine where to move & return the move
    if computerLetter == 'X':
        playerLetter = "O"
    else:
        playerLetter = "O"

# AI ALGORITHM
    # first check if can win

    for i in range(1, len(board)):
        boardCopy = getBoardCopy(board)
        if checkFreeSpace(boardCopy, i):
            boardCopy[i] = computerLetter
            if isWinner(boardCopy, computerLetter):
                return i

    # else check if we should block the player
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if checkFreeSpace(boardCopy, i):
            boardCopy[i] = playerLetter
            if isWinner(boardCopy, playerLetter):
                return i
    # go to the center if its free
    if checkFreeSpace(board, 5):
        return 5
    # go to a corner if they are free
    move = validMoves(board, [1, 3, 7, 9])
    if move is not None:
        return move
    # move to the sides
    return validMoves(board,[2, 4, 6, 8])

# returns a copy of the board
def getBoardCopy(board):
    boardCp = list(board)
    return boardCp

# return a valid move or none if not valid move
def validMoves(board, moves):
    possibleMoves = list()
    for i in moves:
        if checkFreeSpace(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

# function to start game
def startGame(board):
    print("*" * 10 + " TIC-TAC-TOE " + "*" * 10)
    drawBoard(board)

# function to ask to play again
def playAgain():
    print(" Do you want to play again ? (yes or no)")
    return input().lower().startswith('y')

# function to check if game over
def gameOver(board):
    playerLetter = getPlayerLetter()
    if playerLetter == "X":
        computerLetter = "O"
    else:
        computerLetter = "X"
    if isWinner(board, playerLetter):
        print("Player has won the game!")
        return True
    elif isWinner(board, computerLetter):
        print("Computer has won the game!")
        return True

    return False

# function to check if it's tie
def isTie(board):
    for i in board:
        if i != " ":
            return False
    if gameOver(board):
        return False
    return True

# function to check if player won
def isWinner(board, letter):
#returns True is player won
    return ( board[7] == letter and board[8] == letter and board[9] == letter #top
             or (board[4] == letter and board[5] == letter and board[6] == letter) #middle
             or (board[1] == letter and board[2] == letter and board[3] == letter) #bottom
             or (board[4] == letter and board[1] == letter and board[7] == letter) #down left
             or (board[8] == letter and board[5] == letter and board[2] == letter) #down middle
             or (board[9] == letter and board[3] == letter and board[6] == letter) #down right
             or (board[7] == letter and board[5] == letter and board[3] == letter) #diagonal
             or (board[9] == letter and board[5] == letter and board[1] == letter)) #diagonal

# main function that plays the game
def play():
    board = [' '] *10
    startGame(board)
    gameDone = False

    print(" Choose your letter.")
    playerLetter = getPlayerLetter()

    if playerLetter == "X":
        computerLetter = "O"
    else:
        computerLetter = "X"
    print(playerLetter, computerLetter)
    turn = firstPlayer()
    print(turn + " goes first.")


    while not gameDone:
            if turn == "player":
                drawBoard(board)
                print(" Give your move. (1-9)")
                move = getplayerMove(board, playerLetter)
                board[move] = playerLetter
                if isWinner(board, playerLetter):
                    drawBoard(board)
                    print('You have won the game!')
                    gameDone = True
                    break
                else:
                    if isTie(board):
                        print('It is a Tie!')
                        gameDone = True
                        break
                    else:
                        turn = 'computer'
            else:
                # computer's turn
                move = getComputerMove(board, computerLetter)
                board[move] = computerLetter
                if isWinner(board, computerLetter):
                    drawBoard(board)
                    print(" Computer has won the game!")
                    gameDone = True
                    break
                else:
                    if isTie(board):
                        print('It is a Tie!')
                        gameDone = True
                        break
                    else:
                        turn = "player"




drawBoard(" 123456789")
play()
while playAgain():
    play()
# board=[" "]*10
# letter='X'
# move = getComputerMove(board,letter)
# print(move)
