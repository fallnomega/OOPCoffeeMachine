from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine










turn_off_machine = False
while turn_off_machine != True:
    drink_choice = order_drink()
    print_report()
    # Check resources sufficient?
    resource_check = check_resources_availability(drink_choice)
    if resource_check == 0:
        continue
    process_coins(drink_choice)
    make_coffee(drink_choice)
    print_report()
    print(f"Here is your {list(MENU)[int(drink_choice) - 1]}. Enjoy!")
    turn_off()
