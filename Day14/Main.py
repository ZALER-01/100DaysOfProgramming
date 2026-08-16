from art import logo
import random
from gameData import data

print(logo)


def format_data(account):
    """Take account data and return printable format"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"


def check_answer(user_guess, a_followers, b_followers):
    """Return True if user is correct, otherwise False"""

    if a_followers > b_followers:
        return user_guess == "A"
    else:
        return user_guess == "B"


# Pick two random accounts
account_a = random.choice(data)
account_b = random.choice(data)

# Make sure A and B are different
while account_a == account_b:
    account_b = random.choice(data)

print(f"Compare A: {format_data(account_a)}")
print("VS")
print(f"Against B: {format_data(account_b)}")

# Ask user for guess
guess = input("Who has more followers? Type 'A' or 'B': ").upper()

# Get follower counts
a_followers_count = account_a["followers_count"]
b_followers_count = account_b["followers_count"]

# Check answer
is_correct = check_answer(
    guess,
    a_followers_count,
    b_followers_count
)

# Display result
if is_correct:
    print("✅ You are right!")
else:
    print("❌ Sorry, that's wrong.")

print(f"\n{name:=^30}")
print(f"A followers: {a_followers_count}")
print(f"B followers: {b_followers_count}")