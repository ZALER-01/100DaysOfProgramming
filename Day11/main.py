import random as rnd
from Day11.cards import *

# Return a random card from deck
def deal_card():
    return rnd.choice(cards)


def calculate_score(cards):
    # Blackjack
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    # Convert Ace from 11 to 1 if needed
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


print(deal_card())

user_cards = []
computer_cards = []

# Deal initial cards
for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

userScore = calculate_score(user_cards)
computerScore = calculate_score(computer_cards)

print(f"Your cards: {user_cards}, current score: {userScore}")
print(f"Computer's first card: {computer_cards[0]}")
