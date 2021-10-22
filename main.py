import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
comp_choice = random.randint(0, 2)
ascii_list = [rock, paper, scissors]
print(ascii_list[user_choice])
print("Computer Chose: ")
print(ascii_list[comp_choice])

if(user_choice == 0 and comp_choice == 1):
  print("You Lose")
elif(user_choice == 1 and comp_choice == 2):
  print("You Lose")
elif(user_choice == 2 and comp_choice == 0):
  print("You Lose")
else:
  if(user_choice == comp_choice):
    print("Draw")
  else:
    print("You Win")
