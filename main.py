import random
import hangman_art
import hangman_words

print(hangman_art.logo)
level = len(hangman_art.stages)
chosen_word = random.choice(hangman_words.word_list)

display = []
display.extend(('_ '*len(chosen_word)).split())

guesses = []

while('_' in display and level > 0):
  guess = input("Guess a letter: ").lower()
  if(guess in guesses):
    print("You already have chosen this letter")
    print(' '.join(display))
    print(hangman_art.stages[level-1])
    continue
  guesses.append(guess)
  count = 0
  for i in range(len(chosen_word)):
    if chosen_word[i] == guess:
        display[i] = chosen_word[i]
        count += 1
  if(count == 0):
    level -= 1
    print(f"You guessed {guess}, that's not in the word. You lose a life.")
  print(' '.join(display))
  print(hangman_art.stages[level-1])
  

if("_" not in display and level > 0):
  print("You Win")
else:
  print("You Lose")
  print(f"The word was: {chosen_word}")
