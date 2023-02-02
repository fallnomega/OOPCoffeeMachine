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
        print(customer_choice.items())
        for x in customer_choice:
            payment.make_payment(customer_choice[x]['cost'])
    turn_off_machine = True







# 5. Process coins.
# a. If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.
# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
# 6. Check transaction successful?
# a. Check that the user has inserted enough money to purchase the drink they selected. E.g
# Latte cost $2.50, but they only inserted $0.52 then after counting the coins the program
# should say “Sorry that's not enough money. Money refunded.”.
# b. But if the user has inserted enough money, then the cost of the drink gets added to the
# machine as the profit and this will be reflected the next time “report” is triggered. E.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# c. If the user has inserted too much money, the machine should offer change.
# E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
# places.
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