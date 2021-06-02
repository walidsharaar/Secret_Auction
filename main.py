#import library

import os

from  asciis import welcome_massege
print(welcome_massege)

print("Welcome to the secret auction program.")



#todo clear the terminal

def clear():
    os.system('cls')
#todo create function to find highest bidder

def find_bidder():
    highest_amount=0

    #{"a":123}
    for bidder in bidding:
        highest_amount= bidding[bidder]
        if highest_amount > highest_amount:
            highest_amount = bid_amount



#todo create a empty dictory.

bids={}
bidding_closed=False



#todo while loop to get user input

while not bidding_closed:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    bids[name]= bid
    close_the_bid = input("Do you want to close the bed? Type 'Y' for yes and 'N' for no").lower()
    if close_the_bid =="no":
        bidding_closed=True
    elif close_the_bid=="yes":
        bidding_closed=False
        clear()
    else:
        close_the_bid=True






clear()


