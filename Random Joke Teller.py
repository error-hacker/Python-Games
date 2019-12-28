#Random Joke Teller
import random

print("Do you want to read a joke(Y/N)")
yn=input()
while yn=='Y'or yn=='y':
    
    jn=random.randint(1,6)
    if jn==1:
        print('Did you hear about the new hi-tech broom?')
        input()
        print("It's sweeping the nation\n")
    if jn==2:
        print('What do you call someone who points out the obvious?')
        input()
        print('Someone who points out the obvious\n')
    if jn==3:
        print('Which horse runs the city?')
        input()
        print('The mare, of course\n')
    if jn==4:
        print('How do you get over a fear of elevators?')
        input()
        print('Just take some steps to avoid them!\n')
    if jn==5:
        print('Which playing cards are the best dancers?')
        input()
        print('The king and queen of clubs\n')
    if jn==6:
        print('What did one sonowman say to the other?')
        input()
        print('"Do you smell carrots"\n')
    yn=input('Do you want another (Y/N)')
print('It\'s ok I won\'t mind it!')