def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    if n2 == 0:
        return "Cannot divide by zero"
    return n1 / n2


Operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

should_accumulate = True

while should_accumulate:

    number1 = float(input("What is your first number? "))

    print("Available operations:")
    for symbol in Operations:
        print(symbol)

    operation_symbol = input("Pick an operation: ")

    if operation_symbol not in Operations:
        print("❌ Enter a correct choice (+, -, *, /)")
        continue

    number2 = float(input("What is your second number? "))

    answer = number1, number2

    print(f"{number1} {operation_symbol} {number2} = {answer}")

    choice = input(
        "Type 'y' to perform another calculation or 'n' to exit: "
    ).lower()

    if choice == "n":
        should_accumulate = False
        print("Calculator closed.")