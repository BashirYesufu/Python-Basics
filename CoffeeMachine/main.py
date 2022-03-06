from menu import MENU
from resources import  resources

continue_dispensing = True
while continue_dispensing:
    choice = input("What would you like? (espresso, latte or cappuccino): ")
    if choice == "off":
        continue_dispensing = False
