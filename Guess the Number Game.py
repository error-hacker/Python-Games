#Guess the Number Game
import random
no=random.randint(1, 15)
guessno=0
print("Hello There! \nWhat's your Name?")
name=input()
print(name,",I am thinking of a number between 1 and 15 in my processor.\nTake a guess!")
for guessno in range(5):
    guess=int(input())
    if guessno==0:
        if guess<no:
            print('Oh! Your guess is low\nTry again (4 tries left)')
        if guess>no:
            print('Oh! Your guess is high\nTry again (4 tries left)')
    if guessno==1:
        if guess<no:
            print('Opps! Your guess is low\nTry again (3 tries left)')
        if guess>no:
            print('Oops! Your guess is high\nTry again (3 tries left)')
    if guessno==2:
        if guess<no:
            print('Opps! Wrong Again \nYour guess is low (2 tries left)')
        if guess>no:
            print('Oops! Wrong Again \nYour guess is high (2 tries left)')
    if guessno==3:
        if guess<no:
            print('Your guess is low.\nThink harder (1 try left)')
        if guess>no:
            print('Your guess is high.\nThink harder (1 try left)')
    if guessno==4:
        if guess<no:
            print('Your guess is low.\nSorry all tries over\nThe number I was thinking of was',no)
        if guess>no:
            print('Your guess is high.\nSorry all tries over\nThe number I was thinking of was',no)
    if guess==no:
        print('Good Job,',name,',You guessed the number in ',guessno+1,'guesses!')
        break