import random as rnd

print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

print(f"welcome to rock paper scissors game ")
print(f" 1 for rock\n 2 for paper\n 3 for scissors")

user_choice = int(input(f"Enter your choice:  1  2 or 3: "))

# Check for valid input range
if user_choice < 1 or user_choice > 3:
  print("You typed an invalid number. You lose!")
else:
  computer_choice = rnd.randint(1, 3)
  print(f"Computer chose {computer_choice}")

  # Game logic
  if user_choice == computer_choice:
    print("It's a draw!")
  elif (
      (user_choice == 1 and computer_choice == 3)
      or (user_choice == 2 and computer_choice == 1)
      or (user_choice == 3 and computer_choice == 2)
  ):
    print("You win!")
  else:
    print("You Lose")




