from menu import MENU
from resources import resources

profit_made = 0
continue_dispensing = True

while continue_dispensing:
    choice = input("What would you like? (espresso, latte or cappuccino): ")
    if choice == "off":
        continue_dispensing = False
    elif choice == "report":
        print(f"{resources['water']}ml of water")
        print(f"{resources['milk']}ml of milk")
        print(f"{resources['coffee']}g of coffee")
        print(f"${profit_made} profit made.")
