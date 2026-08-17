from Day16.Docs.coffee_maker import CoffeeMaker
from Day16.Docs.menu import Menu
from Day16.Docs.money_machine import MoneyMachine

# Create objects
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")

    if choice == "off":
        is_on = False

    elif choice == "report":
        coffee_maker.report()
        money_machine.report()

    else:
        drink = menu.find_drink(choice)

        # Check resources sufficient
        if drink and coffee_maker.is_resource_sufficient(drink):

            # Process payment and make coffee
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)