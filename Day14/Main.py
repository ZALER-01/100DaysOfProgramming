from art import logo
import random
from gameData import data


def format_data(account):
    """Format account data into printable string"""
    name = account["name"]
    description = account["description"]
    country = account["country"]

    return f"{name}, a {description}, from {country}"


def check_answer(user_guess, a_followers, b_followers):
    """Return True if user guessed correctly"""

    if a_followers > b_followers:
        return user_guess == "A"
    else:
        return user_guess == "B"


score = 0
game_should_continue = True

account_a = random.choice(data)

while game_should_continue:

    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(logo)

    print(f"Compare A: {format_data(account_a)}")
    print("vs")
    print(f"Against B: {format_data(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    a_followers_count = account_a["followers_count"]
    b_followers_count = account_b["followers_count"]

    is_correct = check_answer(
        guess,
        a_followers_count,
        b_followers_count
    )

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")

        # B becomes A for next round
        account_a = account_b

    else:
        game_should_continue = False
        print(
            f"Sorry, that's wrong. Final score: {score}"
        )

        print(
            f"A had {a_followers_count} million followers."
        )

        print(
            f"B had {b_followers_count} million followers."
        )
