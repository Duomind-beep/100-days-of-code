import art

print(art.logo)

def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}")



bids = {}
restart = True
while restart is True:
    name = input("Please type your name? \n")
    price = int(input("How much would you like to bid? \n$"))

    bids[name] = price

    new_bid = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
    if new_bid == "yes":
        restart = True
        print("\n" * 100)
    else:
        restart = False
        find_highest_bidder(bids)




# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


