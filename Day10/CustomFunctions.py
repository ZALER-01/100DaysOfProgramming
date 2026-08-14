def show_calculator():
    calc = """
  _____________________

 |  _________________  |
 | | [5318008]       | |
 | |_________________| |
 |  ___ ___ ___   ___  |
 | | 7 | 8 | 9 | | + | |
 | |___|___|___| |___| |
 | | 4 | 5 | 6 | | - | |
 | |___|___|___| |___| |
 | | 1 | 2 | 3 | | x | |
 | |___|___|___| |___| |
 | | . | 0 | = | | / | |
 | |___|___|___| |___| |
 |_____________________|
    """
    print(calc)

show_calculator()

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide any inputs."

    f_name = f_name.title()
    l_name = l_name.title()

    return f"{f_name} {l_name}"


# Test
print(format_name("riTuraj", "chOUDHARY"))

def function1(text):
    return text +text

def function2(text):
    return text.title()

def add (n1 , n2):
    return n1 +n2
def sub (n1 , n2):
    return n1 - n2
def mul (n1 , n2):
    return n1 * n2
def div (n1 , n2):
    return n1 / n2
