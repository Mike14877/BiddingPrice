# BiddingPrice
from art import logo

print(logo)
bid = {}
def find_highest_bidder(bidding_record):
    higher_bidder = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        winner = bidder
        if bid_amount > higher_bidder:
            higher_bidder = bid_amount
    print(f"The winner is {winner} with bid of $ {higher_bidder}")

keep_bidding = False
while not keep_bidding:
    name = input("What is your name: ")
    bid_price = int(input("What your price ? $ "))
    other_bidder = input("Is other bidder? ")
    bid[name] = bid_price
    if other_bidder == "no":
        keep_bidding = True
        find_highest_bidder(bid) # back to find_highest_bidder function
    # else:
    #     clear()
