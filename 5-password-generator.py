#Password Generator Project
from random import shuffle
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

""" shuffle(letters)
shuffle(numbers)
shuffle(symbols)

password_list = []
password_list.append(letters[0:nr_letters])
password_list.append(symbols[0:nr_symbols])
password_list.append(numbers[0:nr_numbers])

password_string = ''

for sublist in password_list:
    for item in sublist:
        password_string += item

print(password_string) """

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

shuffle(letters)
shuffle(numbers)
shuffle(symbols)

password_sublists = []
password_sublists.append(letters[0:nr_letters])
password_sublists.append(symbols[0:nr_symbols])
password_sublists.append(numbers[0:nr_numbers])

password_list = []

for sublist in password_sublists:
    for item in sublist:
        password_list.append(item)

shuffle(password_list)
password_string = ''.join(password_list)

print(password_string)