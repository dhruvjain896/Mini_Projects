import pandas

nato = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in nato.iterrows()}

word = input("Enter a word: ").upper()

list_of_words = [nato_dict[letter] for letter in word]

print(list_of_words)
