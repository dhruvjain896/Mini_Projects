import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser(text, shift, direction):
  end_text = ""
  if direction == 'decode':
    shift *= -1
  for i in text:
    if i in alphabet:
      if(shift + alphabet.index(i) > 26):
        end_text += alphabet[alphabet.index(i) + shift - 26]
      elif(shift + alphabet.index(i) < 0):
        end_text += alphabet[alphabet.index(i) + shift + 26]
      else:
        end_text += alphabet[alphabet.index(i) + shift]
    else:
      end_text += i
  print(f"Here's the {direction}d result: {end_text}")

decision = "yes"
while(decision == "yes"):
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  if shift > 26:
    shift = shift % 26
  ceaser(text, shift, direction)
  decision = input("Do you want to go again? \nType 'yes' if you want to go again. Otherwise type 'no': ")
