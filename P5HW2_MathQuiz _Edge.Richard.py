#Math Quiz with options for addition and subtraction
#10-July-2021
#CTI-110 P5HW2 - Math Quiz
#Richard Edge
#

#Random Function.
import random

#Define the Main Menu.
#Use print '\t Main Menu' to create indentation
#Use print '\t ------\n' to create indentation
#Use print ("\t 1. Addition Random Numbers") to create indentation for addition
#Use print ("\t 2. Subtract Random Numbers") to create indentation for subtraction
#print ("\t 3. Exit\n") to create indentation and creates space between lines
def menu():
    print ('\t MAIN MENU')
    print ('\t -------------------')
    print ("\t 1. Addition Random Numbers")
    print ("\t 2. Subtract Random Numbers")
    print ("\t 3. Exit\n")
    
    choice = int(input("\t Please choose one of the menu options: "))
    return choice

#Define the Addition and Subtraction Functions.
def addition():
    a = random.randint (0, 1000)
    b = random.randint (0, 1000)
    right = a + b

    #Format things with newlines and tabs so that numbers go above one another
    # {a} and {b} get replaced with the value of a and b 
    print (f"\t  {a} \n\t +{b}\n\t ----\n")
    answer = int(input("\t Enter answer: "))

    #Create a loop until the user enters a right aswer
    while right != answer:
        if answer > right:
            print ("\t Sorry, guess is too high.")
        elif answer < right:
            print ("\t Sorry, guess is too low.")

        answer = int(input("\t Try again: "))
    
    #If the user has gotten here the answer must is right
    print ("\t Congratulations!!!!, your answer is correct.\n")


def subtraction():
    a = random.randint (0, 1000)
    b = random.randint (0, 1000)
    right = a - b
    #Format things with newlines and tabs so that numbers go above one another
    # {a} and {b} get replaced with the value of a and b 
    print (f"\t  {a} \n\t -{b}\n\t ----\n")
    answer = int(input("\t Enter answer: "))

    #Create a loop until the user enters the right aswer
    while right != answer:
        if answer > right:
            print ("\t Sorry, guess is too high.")
        elif answer < right:
            print ("\t Sorry, guess is too low.")
            

        answer = int(input("\t Try again: "))
    
    #If the user has gotten here the answer must be right
    print ("\t Congratulations!!!!, your answer is correct.\n")

#Define the main program
def main():

    print ("\t Welcome to Math Quiz\n")

    #Set choice to a value that makes the loop run the first time
    choice = 0

    #The loop continues until the user enters the number 3 to exit the menu 
    while choice != 3:

        #Run the menu function which will return a choice that the user has entered
        choice = menu()

        if choice == 1:
            addition()
        elif choice == 2:
            subtraction()

        #If the user enters the number 3 the loop will end and the program will exit

    #Exit message
    print ("\t Thanks for playing!")

#Run the main program
main()


