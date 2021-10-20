import random

r1 = random.randint(1, 9)

chances = 0

while chances < 5:
    print('Enter a Number') 
    userGuess = int(input())
    if(userGuess == r1): 
        print('You Got It Right!')
        chances = 5
    elif(userGuess > r1):
        print('You guessed too high, Go Lower')
        chances = chances+1
    elif(userGuess < r1):
        print('You Guessed Too Low, Go Higher')
        chances = chances+1
    elif(chances == 5):
        print('The correct answer was ' + r1 + ', Try again next time')
    else:
        print('no')