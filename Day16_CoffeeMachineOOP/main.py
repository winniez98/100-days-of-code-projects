from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# object naming tends to be lower and snake case of class name
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

machine_on = True

while machine_on:
    # TODO: 1. Get user's input
    options = menu.get_items()
    choice = input(f"What would you like? {options}: ")

    # TODO: 2. Turn machine off when "off" entered
    if choice == "off":
        machine_on = False
    # TODO: 3. Print report
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        item = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(item):
            # TODO: 5. Process coins and check that transaction is successful
            if money_machine.make_payment(item.cost):
                # TODO: 6. Make coffee
                coffee_maker.make_coffee(item)
