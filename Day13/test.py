from random import randint, random
import math


def my_function():
    for i in range(1,20):
        if i ==20:
            print("You got it!")
my_function()


def my_function1():
    for i in range(1,21):
        if i ==20:
            print("You got it!")
my_function1()

dice_images = ['1','2','3','4','5','6']
dice_num = randint(0,5)
print(dice_images[dice_num])

year = int(input(f'What is your year of birth'))
if 1980 < year < 1994:
    print(f'you are a mellenial')
elif year >1994 :
    print(f'you are a genz')

word_per_page = 0

try:
    pages = int(input("No of words per page: "))

    total_words = pages * word_per_page

    print(f"pages = {pages}")
    print(f"word_per_page = {word_per_page}")
    print(f"total_words = {total_words}")

except ValueError:
    print("Please enter a valid integer.")

def mutate (a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(0,1)
        new_item = maths.add(new_item , item)
    b_list.append(new_item)
    print(b_list)

