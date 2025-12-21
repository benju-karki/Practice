
#simple dice game to play in loop until user wants to quit
# ask a question : play the game (yes/no)
#if yes then roll the dice and guess the number
#if no then thankyou message and terminate the game
#if choose invalid option then show invalid option message

import random

while True:
    Choice = input("Do you want to play the Dice Roll Game? (yes/no): ").lower()
    if Choice == "yes":
        d1= random.randint(1, 6)
        d2= random.randint(1, 6)
        print(f" Dice rolled: {d1} and {d2}")
    elif Choice == "no":
        print( "Thank you for playing the Dice Roll Game. Goodbye!")
        break
    else:
        print("Invalid option.")