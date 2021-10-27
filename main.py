import random
import os
from art import logo

def clear():
  # for mac and linux
  if os.name == 'posix':
    _ = os.system('clear')
  else:
    # for windows platfrom
    _ = os.system('cls')

def play_game():
  print(logo)

  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  attempts = 0
  if(difficulty == 'easy'):
    print("You have 10 attempts remaining to guess the number.")
    attempts = 10
  else:
    print("You have 5 attempts remaining to guess the number.")
    attempts = 5

  number = random.randint(1, 100)
  is_guess = False
  while(not is_guess):
    guess = int(input("Make a guess: "))
    if(guess > number):
      print("Too high.")
      print("Guess again.")
      attempts -= 1
      print(f"You have {attempts} attempts remaining to guess the number.")
    elif(guess < number):
      print("Too low.")
      print("Guess again.")
      attempts -= 1
      print(f"You have {attempts} attempts remaining to guess the number.")
    else:
      print(f"You got it! The answer was {number}.")
      is_guess = True
    if(attempts <= 0):
      print("You've run out of guesses, you lose.")
      break

play_game()

play_again = True
while(play_again == True):
  user_decision = input("Do you want to play the Number Guessing Game again. Type 'yes' or 'no' ")
  if(user_decision == 'yes'):
    clear()
    play_game()
  else:
    play_again = False
