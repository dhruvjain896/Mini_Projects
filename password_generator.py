import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = 5
nr_symbols = 2
nr_numbers = 3


def split(word):
    return [char for char in word]


def generate_password():
    password = ""
    for i in range(0, nr_letters):
        password += letters[random.randint(0, len(letters) - 1)]

    for i in range(0, nr_symbols):
        password += symbols[random.randint(0, len(symbols) - 1)]

    for i in range(0, nr_numbers):
        password += numbers[random.randint(0, len(numbers) - 1)]

    password_len = len(password)

    hard_password = ""
    password = split(password)

    for i in range(0, password_len):
        char_index = random.randint(0, len(password) - 1)
        char = password.pop(char_index)
        hard_password += char
    return hard_password

