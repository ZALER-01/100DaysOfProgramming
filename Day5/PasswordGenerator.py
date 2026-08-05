import random as rnd

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
           'n','o','p','q','r','s','t','u','v','w','x','y','z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = ['!','@','#','$','%','^','&','*','(',')']

print("Welcome to Password Generator!")

numberOfLetters = int(input("How many letters would you like? "))
numberOfSymbols = int(input("How many symbols would you like? "))
numberOfNumbers = int(input("How many numbers would you like? "))

password = ""

for char in range(numberOfLetters):
    password += rnd.choice(letters)

for char in range(numberOfSymbols):
    password += rnd.choice(symbols)

for char in range(numberOfNumbers):
    password += rnd.choice(numbers)

print(f"Your password is: {password}")