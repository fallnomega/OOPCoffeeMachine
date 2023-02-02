from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

turn_off_machine = False
while not turn_off_machine:
    coffee_machine = CoffeeMaker()
    get_item = Menu()
    get_item.get_items()
    # customer_choice = input(f"What would you like? {get_item.get_items()}: ")
    customer_choice = 'latte'

    if customer_choice == 'off':
        print("\nShutting down. Goodbye!\n")
        exit()
    elif customer_choice == 'report':
        coffee_machine.report()
    elif get_item.find_drink(customer_choice) == None:
        print("\n\nWrong selection, try again\n\n")
        exit()
    else:
        customer_choice = get_item.find_drink(customer_choice)
        if coffee_machine.is_resource_sufficient(customer_choice) == 0:
            continue
        payment = MoneyMachine()
        for x in customer_choice:
            payment.make_payment(customer_choice[x]['cost'])
        payment.report()
        coffee_machine.make_coffee(customer_choice)
        coffee_machine.report()
    turn_off_machine = True

# 7. Make Coffee.
# a. If the transaction is successful and there are enough resources to make the drink the user
# selected, then the ingredients to make the drink should be deducted from the coffee
# machine resources.
# E.g. report before purchasing latte:
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0
# Report after purchasing latte:
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If latte
# was their choice of drink.


# test info on drink ordered
# testing_get_drink_order = Menu.find_drink('espresso')
# print(testing_get_drink_order)
# testing_get_drink_order = Menu.find_drink('latte')
# print(testing_get_drink_order)
# testing_get_drink_order = Menu.find_drink('cappuccino')
# print(testing_get_drink_order)

# test print coffee maker report on its resource levels

# print_report()
# # Check resources sufficient?
# resource_check = check_resources_availability(drink_choice)
# if resource_check == 0:
#     continue
# process_coins(drink_choice)
# make_coffee(drink_choice)
# print_report()
# print(f"Here is your {list(MENU)[int(drink_choice) - 1]}. Enjoy!")
# turn_off()
