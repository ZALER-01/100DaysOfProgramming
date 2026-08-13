from Day9 import logo

print(logo)
print("Hello")
print("\n" * 100)


# 1. Define the function first
def findHighestBidder(biddingDictionary):
    highest_bid = 0
    winner = ""
    for bidder in biddingDictionary:
        bid_amount = biddingDictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f'The winner is {winner} with a bid of {highest_bid}!')


bids = {}

# 2. Run the loop second
continue_bidding = True
while continue_bidding:
    name = input("What is your name? \n")
    bidAmount = int(input("How much do you bid? \n"))
    bids[name] = bidAmount

    should_continue = input('Is there any other bidder? Type "yes" or "no": \n').lower()
    if should_continue == 'no':
        continue_bidding = False
        findHighestBidder(bids)  # Now Python knows exactly what this is!
    elif should_continue == 'yes':
        print("\n" * 100)
