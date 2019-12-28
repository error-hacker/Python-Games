# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 00:42:21 2019

@author: Sahilsarthak
"""

import random

hangmanPics=['''
 +---+
 |
 |
 |
===''', '''
 +---+
 |   O
 |
 |
===''', '''
 +---+
 |   O
 |   |
 |
===''', '''
 +---+
 |   O
 |   |\\
 |
===''', '''
 +---+
 |   O
 |  /|\\
 |
===''', '''
 +---+
 |   O
 |  /|\\
 |    \\
===''', '''
 +---+
 |   O
 |  /|\\
 |  / \\
===''','''
 +---+
 |  [O
 |  /|\\
 |  / \\
===''','''
 +---+
 |  [O]
 |  /|\\
 |  / \\
 ===''']

words = {'Colors':'red orange yellow green blue indigo violet white black brown'.split(),
'Shapes':'square triangle rectangle circle ellipse rhombus trapezoid chevron pentagon hexagon septagon octagon'.split(),
'Fruits':'apple orange lemon lime pear watermelon grape grapefruit cherry banana cantaloupe mango strawberry tomato'.split(),
'Animals':'bat bear beaver cat cougar crab deer dog donkey duck eagle fish frog goat leech lion lizard monkey moose mouse otter owl panda python rabbit rat shark sheep skunk squid tiger turkey turtle weasel whale wolf wombat zebra'.split()}


def getRandomWord(wordDict):
    wordKey = random.choice(list(wordDict.keys()))
    
    wordIndex=random.randint(0,len(wordDict[wordKey])-1)
    
    return [wordDict[wordKey][wordIndex],wordKey]

def selectDifficulty():
    difficulty="a"
    while difficulty !='E' and difficulty !='M' and difficulty !='H' :
        print('Enter difficulty: E - Easy, M - Medium, H - Hard')
        difficulty= input().upper()
    if difficulty == 'M' :
        del hangmanPics[8]
        del hangmanPics[7]
    if difficulty == 'H' :
        del hangmanPics[8]
        del hangmanPics[7]
        del hangmanPics[5]
        del hangmanPics[3]
    return


def displayBoard(missedLetters, correctLetters, secretWord):
    print(hangmanPics[len(missedLetters)])
    print()
    
    print ('Missed letters :', end=' ')
    for letter in missedLetters:
        print (letter,end=' ')
    print()
    
    blanks='_'*len(secretWord)
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks=blanks[:i]+secretWord[i]+blanks[i+1:]
    
    for letter in blanks:
        print(letter, end=' ')
    print()
    
def getGuess(alreadyGuessed):
    
    while True:
        print("Guess a letter")
        guess=input()
        guess= guess.lower()
        
        if len(guess)!=1:
            print('Please enter a single digit.')
        elif guess in alreadyGuessed:
            print ('This letter is already guessed. Choose another')
        elif guess not in 'qwertyuiopasdfghjklzxcvbnm' :
            print('Please enter an alphabet')
        else:
            return guess
        
def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

print('H A N G M A N')
selectDifficulty()
missedLetters=''
correctLetters=''
secretWord, secretSet = getRandomWord(words)
gameIsDone=False

while True:
    print("The secret word is in the set : " + secretSet)
    displayBoard(missedLetters, correctLetters, secretWord)
    
    guess=getGuess(missedLetters + correctLetters)
    
    if guess in secretWord:
        correctLetters=correctLetters+guess
        
        foundAllLetters=True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters=False
        if foundAllLetters:
            print('Congrats, you have won. The secret word is "'+ secretWord+'"')
            gameIsDone=True
            
    else:
        missedLetters=missedLetters+guess
        if len(missedLetters)==len(hangmanPics)-1:
            displayBoard(missedLetters,correctLetters, secretWord)
            print('You have ran out of guesses after '+str(len(missedLetters))+' missed guesses and '+str(len(correctLetters))+' correct guesses and the secret word was "'+ secretWord+'"')
            gameIsDone=True
    
    if gameIsDone:
        if playAgain():
            selectDifficulty()
            missedLetters=''
            correctLetters=''
            secretWord, secretSet = getRandomWord(words)
            gameIsDone=False
        else:
            break