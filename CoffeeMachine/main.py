from menu import MENU
from resources import resources

profit_made = 0
continue_dispensing = True

def check_resources(drink_ingredients):
    for item in drink_ingredients:
        if drink_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
    return True


while continue_dispensing:
    choice = input("What would you like? (espresso, latte or cappuccino): ")
    if choice == "off":
        continue_dispensing = False
    elif choice == "report":
        print(f"{resources['water']}ml of water")
        print(f"{resources['milk']}ml of milk")
        print(f"{resources['coffee']}g of coffee")
        print(f"${profit_made} profit made.")
    else:
        coffee_type = MENU(choice)
        if check_resources(coffee_type):

