import random

number_to_guess = random.randint(1, 100) 
while True:
    try:
        guess_by_user = int(input("Guess a number between 1 and 100: "))
        if guess_by_user < number_to_guess:
            print("Too low!")
        elif guess_by_user > number_to_guess:
            print("Too high!")
        else:
            print("Congratulations! You've guessed the correct number!")
            break
    except ValueError:
        print("Please enter a valid number.")

## Improved version with attempt limit and better structure
'''import random

def guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100.")
                continue

            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    if attempts == max_attempts:
        print(f"Sorry, you've used all your attempts. The number was {number_to_guess}.")'''