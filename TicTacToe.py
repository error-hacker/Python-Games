# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 02:22:51 2019

@author: Sahilsarthak
"""

import random

def drawBoard(board):
    
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])
    
def inputPlayerLetter():
    
    letter=''
    
    while not(letter== 'X' or letter== 'O'):
        print ('Do you want to be X or O')
        letter= input().upper()
    
    if letter== 'X' :
        return['X','O']
    else:
        return['O','X']

def whoGoesFirst():
    
    first=random.randint(0,1)
    if first==0:
        return 'computer'
    else:
        return 'player'
    
def makeMove(board,letter,move):
    board[move]=letter
    
def isWinner(bo, le) :
    return ((bo[7]==le and bo[8]==le and bo[9]==le) or
            (bo[4]==le and bo[5]==le and bo[6]==le) or
            (bo[1]==le and bo[2]==le and bo[3]==le) or
            (bo[1]==le and bo[4]==le and bo[7]==le) or
            (bo[2]==le and bo[5]==le and bo[8]==le) or
            (bo[3]==le and bo[6]==le and bo[9]==le) or
            (bo[1]==le and bo[5]==le and bo[9]==le) or
            (bo[7]==le and bo[5]==le and bo[3]==le))
    
def getBoardCopy(board):
    copyBoard=[]
    for i in board:
        copyBoard.append(i)
    return copyBoard

def isSpaceFree(board, move):
    return board[move] == ' '

def getPlayerMove(board):
    move=' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print ('What\'s your move? (1-9)')
        move=input()
    return int(move)

def chooseMoveFromList(board, moveList):
    
    possibleMoves=[]
    for i in moveList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
            
    if len(possibleMoves) !=0:
        return random.choice(possibleMoves)
    else:
        return None
    
def getComputerMove(board, computerLetter):
    if computerLetter == 'X' :
        playerLetter = 'O'
    else:
        playerLetter = 'X'
        
    for i in range(1,10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i

    for i in range(1,10):
        boardCopy= getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i
        
    move = chooseMoveFromList(board,[1,3,7,9])
    if move!=None:
        return move
    
    if isSpaceFree(board, 5):
        return 5
    
    return chooseMoveFromList(board,[2,4,6,8])

def isBoardFull(board):
    for i in range(1,10):
        if isSpaceFree(board, i):
            return False
    
    return True

print('Welcome to Tic-Tac-Toe')

while True:
    
    board = [' ']*10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True
    
    while gameIsPlaying:
        if turn=='player' :
            drawBoard(board)
            move = getPlayerMove(board)
            makeMove(board,playerLetter, move)
            
            if isWinner(board, playerLetter):
                drawBoard(board)
                print('Congratulations! You have beaten me.')
                break
            elif isBoardFull(board):
                drawBoard(board)
                print('The game is a tie!')
                break
            else:
                turn='computer'
        
        else:
            
            move = getComputerMove(board, computerLetter)
            makeMove(board, computerLetter, move)
            if isWinner(board, computerLetter):
                drawBoard(board)
                print('Sorry! You lost the game.')
                break
            elif isBoardFull(board):
                drawBoard(board)
                print('The game is a tie!')
                break
            else:
                turn='player'
                
    print('Do you want to play again? (Y or N)')
    if not input().lower().startswith('y'):
        break            