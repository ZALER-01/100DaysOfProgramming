print("Welcome to the Tip Calculator!")

bill = float(input("What was the total bill? ₹"))

tip = int(input("How much tip would you like to give? 10, 12 or 15? "))

while tip not in [10, 12, 15]:
    print("Please enter only 10, 12 or 15.")
    tip = int(input("How much tip would you like to give? "))

people = int(input("How many people to split the bill? "))

total_bill = bill + (bill * tip / 100)
amount_per_person = total_bill / people

print(f"Each person should pay: ₹{amount_per_person:.2f}")