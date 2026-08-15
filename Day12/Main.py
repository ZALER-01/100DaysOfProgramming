import random as rnd


def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty == "easy":
        return 10
    else:
        return 5


def check_answer(guess, answer, attempts):
    if guess > answer:
        print("Too high.")
        return attempts - 1

    elif guess < answer:
        print("Too low.")
        return attempts - 1

    else:
        print(f"You got it! The answer was {answer}.")
        return attempts


def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    answer = rnd.randint(1, 100)

    attempts = set_difficulty()

    guess = 0

    while guess != answer and attempts > 0:

        print(f"You have {attempts} attempts remaining to guess the number.")

        guess = int(input("Make a guess: "))

        attempts = check_answer(guess, answer, attempts)

        if guess != answer and attempts > 0:
            print("Guess again.\n")

    if attempts == 0:
        print("You've run out of guesses, you lose.")
        print(f"The correct number was {answer}.")


game()