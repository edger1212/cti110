#Create a game where user enters random number between 1 - 100
#8 July 2021
#CTI-110 P5HW1 - Random Number
#Richard Edge


#Use import random function
import random


def rand_call(guess):
    #Compare users number against the generated random 1 - 100 number
    if x == guess:
        print("Congratulations!!!")
    elif x > guess:
        print("Too low, try again")
    elif x < guess:
        print("Too high, try again")

#Input a range between numbers 1 - 100
#Then generate a random number between 1 - 100
#Use print 'Main Menu\n'(\n creates a space to the next line)
#Use print '------\n'(\n creates a space to the next line)
#Use print \t for Play game (\t creates an indentation)
#Use print \t for Exit\n (\t creates an indentation)
#Use print \n to create a space to next line
x = random.randint(1, 100)
print('MAIN MENU\n')
print('----------------\n')
print("\t 1) Play Game")
print("\t 2) Exit\n")
print("\n")

loop = True
counter = 0
while loop == True:
    #Have user enter a number between 1 -100
    guess = int(input("Enter a number between 1 and 100 "))

    counter = counter + 1
    rand_call(guess)

    if x == guess:
        print(f"Good job.   It took {counter} tries.")
        counter=0
        play_again = int(input("Would you like to play again? (1 - yes, 2 - no) "))
        #If user chooses 1 - yes, generate another random number again
        #If user chooses 2 - no, game ends
        x = random.randint(1, 100)
        if play_again == 1:
            loop = True
        else:
            loop = False




