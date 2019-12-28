# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 03:08:22 2019

@author: Sahilsarthak
"""

import random

NO_DIGITS = 3
MAX_GUESS = 10

def getSecretNumber():
    num= list(range(10))
    random.shuffle(num)
    
    secNum = ''
    for i in range(NO_DIGITS):
        secNum += str(num[i])
        
    return secNum

def getClues(guess, secNum):
    
    if guess == secNum:
        return ('You got it! It\'s %s'%(secNum))
        
    clues=[]
    for i in range(NO_DIGITS):
        if guess[i]==secNum[i]:
            clues.append('Fermi')
        elif guess[i] in secNum:
            clues.append('Pico')
            
    if clues == []:
        return ('Bagels')
        
    clues.sort()
    return(' '.join(clues))

def getGuess(guessCount):
    guess=''
    while True:
        print('Guess #%s :\t'%(guessCount))
        guess=input()
        a=0
        for i in guess:
            if i not in '0 1 2 3 4 5 6 7 8 9'.split():
                a=1
        if len(guess)==NO_DIGITS and a!=1:
            break
    return guess

print('I am thinking of a %s-digit number. Try to guess what it is.' %(NO_DIGITS))
print('The clues I give are...')
print('When I say:    That means:')
print('  Bagels        None of the digits is correct.')
print('  Pico          One digit is correct but in the wrong position.')
print('  Fermi         One digit is correct and in the right position.')


while True:
    
    secNum = getSecretNumber()
    
    print('I have thought of a number. You have %s gusses to get it' %(MAX_GUESS))
    
    guessCount = 1
    while guessCount <= MAX_GUESS:
        guess=getGuess(guessCount)
        
        print(getClues(guess, secNum))
        
        guessCount +=1
        if guess == secNum:
            break
        if guessCount > MAX_GUESS:
            print('You ran out of guesses. The answer was %s.' %(secNum))
    print('Do you want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        break