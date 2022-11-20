from art import *


auction_over = False
bids = {}
highest_bid = 0
highest_bidder = ""
while not auction_over:
    print(logo)
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bids[name] = bid
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

    if more_bidders == "yes":
        print("Don't look up \n\n\n")
    else:
        auction_over = True
        for bidder in bids:
            if bids[bidder] > highest_bid:
                highest_bid = bids[bidder]
                highest_bidder = bidder

print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")
