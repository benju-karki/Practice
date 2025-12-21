print("Program started")

import random
import matplotlib.pyplot as plt

def guessing_game():
    """
    Simulates one guessing game.
    Returns the number of attempts needed to guess the correct number.
    """
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        guess = random.randint(1, 100)  # simulated guessing (agent)
        attempts += 1

        if guess == number_to_guess:
            return attempts


def run_experiments(total_games=50):
    """
    Runs multiple games and logs the number of attempts for each game.
    """
    attempts_data = []

    for game in range(1, total_games + 1):
        attempts = guessing_game()
        attempts_data.append(attempts)
        print(f"Game {game}: {attempts} attempts")

    return attempts_data


def visualize_results(attempts_data):
    """
    Visualizes the performance of the guessing strategy.
    """
    plt.plot(attempts_data)
    plt.xlabel("Game Number")
    plt.ylabel("Number of Attempts")
    plt.title("Guessing Game Performance Over Multiple Games")
    plt.show()


# ------------------ MAIN PROGRAM ------------------

games = 50
attempts_data = run_experiments(games)
visualize_results(attempts_data)
