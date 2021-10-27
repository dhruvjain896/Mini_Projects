import random
import os
from art import logo

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)

def calculate_score(arr):
  if len(arr) == 2 and sum(arr) == 21:
    return 0
  if 11 in arr and sum(arr) > 21:
    arr[arr.index(11)] = 1
  return sum(arr)

def compare(user_score, computer_score):
  if(user_score == computer_score):
    return "Draw 🙃"
  elif(computer_score == 0):
    return "Lose, opponent has Blackjack 😱"
  elif(user_score == 0):
    return "Win with a Blackjack 😎"
  elif(user_score > 21):
    return "You went over. You lose 😭"
  elif(computer_score > 21):
    return "Opponent went over. You win 😁"
  else:
    if(user_score > computer_score):
      return "You win 😄"
    else:
      return "You lose 😤"

def clear():
  # for mac and linux
  if os.name == 'posix':
    _ = os.system('clear')
  else:
    # for windows platfrom
    _ = os.system('cls')

def play_game():
  print(logo)
  user_cards = []
  computer_cards = []
  for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  is_game_over = False
  while(not is_game_over):
    computer = calculate_score(computer_cards)
    user = calculate_score(user_cards)
    print(f"Your cards: {user_cards}, current score: {user}")
    print(f"Computer's first card: {computer_cards[0]}")
    if(computer == 0 or user == 0 or user > 21):
      is_game_over = True
    else:
      dec = input("Do you want to draw another card. Type 'yes' or 'no'\n")
      if dec == "yes":
        user_cards.append(deal_card())
      else:
        is_game_over = True

  while(computer < 17 and computer != 0):
    computer_cards.append(deal_card())
    computer = calculate_score(computer_cards)

  print(f"Your final hand: {user_cards}, final score: {user}")
  print(f"Computer's final hand: {computer_cards}, final score: {computer}")
  print(compare(user, computer))

while input("Do you want to play a game of Blackjack? Type 'yes' or 'no': ") == 'yes':
  clear()
  play_game()
