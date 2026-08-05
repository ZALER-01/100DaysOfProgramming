import random as rnd
import Characters as Chars

from Characters import letters , numbers , symbols


# print(Chars.numbers)
# print(Chars.symbols)
# print(Chars.letters)

# print(numbers)
# print(symbols)
# print(letters)

password = ""

for _ in range(5):
    password += rnd.choice(letters)
for _ in range(2):
    password += rnd.choice(numbers)
for _ in range(2):
    password += rnd.choice(symbols)

print(f"Your password is: {password}")

