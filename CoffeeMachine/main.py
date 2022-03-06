from menu import MENU
from resources import resources

profit_made = 0
continue_dispensing = True


def check_resources(drink_ingredients):
    """"Returns if the ingredients left can make the selected drink type"""
    for item in drink_ingredients:
        if drink_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
    return True


def process_coins():
    """Returns the total calculated coins"""
    print("Please insert coins")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_transaction_successful(coins_received, drink_cost):
    """Returns if the payment is accepted ar money received is insufficient"""
    if coins_received >= drink_cost:
        change = round(coins_received - drink_cost, 2)
        global profit_made
        profit_made += drink_cost
        if not change == 0.00:
            print(f"Here is your change ${change}")
        return True
    else:
        print(f"Sorry, insufficient payment. Money refunded.")
        return False


def make_coffee(drink, ingredients):
    """This makes the required drink"""
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink} ☕️")


while continue_dispensing:
    choice = input("What would you like? (espresso, latte or cappuccino): ").lower()
    if choice == "off":
        continue_dispensing = False
    elif choice == "report":
        print(f"{resources['water']}ml of water")
        print(f"{resources['milk']}ml of milk")
        print(f"{resources['coffee']}g of coffee")
        print(f"${profit_made} profit made.")
    else:
        coffee_type = MENU[choice]
        if check_resources(coffee_type['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, coffee_type['cost']):
                make_coffee(choice, coffee_type['ingredients'])

