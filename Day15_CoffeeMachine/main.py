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


# TODO: 4. Check if resources are sufficient when the user chooses a drink
def check_resources(ingredients):
    """Returns True if there are enough ingredients to make the drink.
     If not enough ingredients, return false."""
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print("Sorry, there aren't enough ingredients")
            return False
        return True


# TODO: 5. Process coins
def process_coins():
    """Returns total amount of coins input by customer. """
    print("Please input coins.")
    quarters = int(input("Number of quarters: "))
    dimes = int(input("Number of dimes: "))
    nickels = int(input("Number of nickels: "))
    pennies = int(input("Number of pennies: "))
    total = (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)
    print(f"You paid ${total:.2f}.")
    return total


# TODO: 6. Check transaction successful
def check_transaction(amount, drink_cost):
    """Returns change and True if customer enters enough money.
    Returns False if not enough"""
    if amount >= drink_cost:
        change = amount - drink_cost
        # add to money
        global money
        money += drink_cost
        print(f"You get ${change:.2f} in change.")
        return True
    else:
        print("Not enough money. Money refunded.")
        return False


# TODO: 7. Make Coffee -> take away resources from resources
def make_coffee(drink_ordered, order_ingredients):
    """Deduct the resources for the drink."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_ordered}. Enjoy!")


money = 0
machine_on = True

while machine_on:
    # TODO: 1. Prompt user by asking what would you like?
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    # TODO: 2. Turn off coffee machine by entering "off" to the prompt
    if choice == "off":
        machine_on = False

    # TODO: 3. Print Report of coffee machine resources
    elif choice == "report":
        print(f"Water: {resources['water']}mL")
        print(f"Milk: {resources['milk']}mL")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")

    else:
        drink = MENU[choice]
        # check resources
        if check_resources(drink["ingredients"]):
            # process coins
            total_amount = process_coins()
            if check_transaction(total_amount, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

