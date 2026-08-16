#TODO :2 Check Resources sufficient to make drink


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_suffucient(order_ingridients):
    for item in order_ingridients:
        order_ingrideient[item] >= resources[item]
        

is_on  = True
while True:
    choice = input(f"What do you like ?(Espresso / Latte / Cappuccino): ").lower()
    if choice == "Off":
        is_on = False
    elif choice == report:
        print (f'water: {resources["water"]}')
        print (f'milk: {resources["milk"]}')
        print (f'coffee: {resources["coffee"]}')
        print(f'Money: ${resources["cost"]}')

    else:
        ingredients = MENU[choice]["ingredients"]

