import random as rnd
from Characters import letters, numbers, symbols

print("Welcome to the Password Generator!")

NumberOfLetters = int(input("How many letters would you like? "))
NumberOfNumbers = int(input("How many numbers would you like? "))
NumberOfSymbols = int(input("How many symbols would you like? "))

password_list = []

for _ in range(NumberOfLetters):
    password_list.append(rnd.choice(letters))

for _ in range(NumberOfNumbers):
    password_list.append(rnd.choice(numbers))

for _ in range(NumberOfSymbols):
    password_list.append(rnd.choice(symbols))

rnd.shuffle(password_list)

password = ""

for character in password_list:
    password += character

print(f"Your password is: {password}")