def gameloop():
    print ("welcome to the guessing game, guess the randomly generated number in the range of 1-100 within 5 tries, and you win!")
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
            tries = tries + 1
            if tries == 5:
                print ("You lose!")
                print ("The number was", y)
                z = input("Play again?Y/N: ")
                if z == "Y":
                    replay()
                elif z == "N":
                    print ("Thanks for playing!")
                break
            print ("Too low!")
            if tries == 4:
                print (5 - tries, "guess left")
            else:
                print (5-tries, "guesses left")
        elif x > y:
            tries = tries + 1
            if tries == 5:
                print ("You Lose!")
                print ("The number was", y)
                replay()
            print ("Too high!")
            if tries == 4:
                print (5 - tries, "guess left")
            else:
                print (5-tries, "guesses left")
def replay():
    gameloop()
gameloop()
        
    
    


    
