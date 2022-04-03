from gavel import logo

print(logo)
print("Welcome to the secret auction!")
new_bidder = True
bid_dict = {}
while new_bidder:
    name = input("What is your name? ")
    bid = int(input("How much do you want to bid? $"))
    bid_dict[name] = bid
    new = input("Are there anymore bidders? Type Yes or No: ")
    if new == "no":
        new_bidder = False
highest_bid = 0
winner = ''
for bidder in bid_dict:
    amount = bid_dict[bidder]
    if amount > highest_bid:
        highest_bid = amount
        winner = bidder

print(f"The winner is {winner} with a bid of {highest_bid}")
