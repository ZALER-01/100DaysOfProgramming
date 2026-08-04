print("Welcome to Rollercoaster!")

name = input("What is your name? ")
height = int(input("How tall are you? "))

bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")

    age = int(input("How old are you? "))

    if age <= 12:
        bill = 5
        print("Child ticket is $5")
    elif age <= 18:
        bill = 7
        print("Youth ticket is $7")
    elif 45 <= age <= 55:
        print(f'Have a free ride on us')
        bill = 0
        print("Youth ticket is $0")
    else:
        bill = 12
        print("Adult ticket is $12")

    wants_photo = input("Do you want a photo? Yes or No: ")

    if wants_photo.lower() == "yes":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you can't ride the rollercoaster.")