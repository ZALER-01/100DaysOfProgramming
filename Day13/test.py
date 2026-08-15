from random import randint

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