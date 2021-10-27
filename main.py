import random
import os
import art
from game_data import data

def clear():
  # for mac and linux
  if os.name == 'posix':
    _ = os.system('clear')
  else:
    # for windows platfrom
    _ = os.system('cls')

high_score = 0
def play_game():
  global high_score
  is_right = True
  B = random.choice(data)
  print(art.logo)
  score = 0
  while(is_right == True):
    A = B
    B = random.choice(data)
    while (A == B):
      B = random.choice(data)
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
    print(art.vs)
    print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}")
    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    if (A['follower_count'] > B['follower_count']):
      answer = 'a'
    else:
      answer = 'b'
    if (user_guess == answer):
      score += 1
      clear()
      print(art.logo)
      print(f"You're right! Current score: {score}.")
    else:
      clear()
      print(art.logo)
      print(f"Sorry, that's wrong. Final score: {score}")
      if score > high_score:
        high_score = score
      print(f"High Score: {high_score}")
      is_right = False
play_again = "yes"
while(play_again == "yes"):
  play_game()
  play_again = input("Do you want to play again? Type 'yes' or 'no': ")
  clear()
