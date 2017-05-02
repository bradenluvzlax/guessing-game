print ("welcome to the guessing game, You have five tries to guess the right number from 1-100")
import random
y = random.randint(1,100) 
tries = 0
while tries < 5:
    x = int(input("Guess a whole number 1-100: "))
    if x < 1 or x > 100:
        print ("Hey! that is not even between 1 and 100!")
        tries = tries + 1
    elif x == y:
        print ("nice guess!!! YOU WIN")
        break
    elif x < y:
        print ("Too low!")
        tries = tries + 1
        if tries >= 4:
            print (5 - tries, "guess left")
        else:
            print (5 - tries, "guesses left")
    elif x > y:
        print ("Too high!")
        tries = tries + 1
        if tries >= 4:
            print (5 - tries, "guess left")
        else:
            print (5 - tries, "guesses left")
if tries > 5:
    print ("You Lose!")

        
    
    


    
