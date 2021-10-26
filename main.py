from art import logo
import os

print(logo)
print("Welcome to the secret auction program.")
bids = {}

def clear():
  # for mac and linux
  if os.name == 'posix':
    _ = os.system('clear')
  else:
    # for windows platfrom
    _ = os.system('cls')

bidders = "yes"
while(bidders == "yes"):
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))
  bids[name] = bid
  bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  clear()

maximum = 0
max_key = ""
for i in bids:
  if bids[i] > maximum:
    maximum = bids[i]
    max_key = i
print(f"The winner is {max_key} with a bid of ${maximum}.")
