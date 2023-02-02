from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

turn_off_machine = False
while not turn_off_machine:
    coffee_machine = CoffeeMaker()
    get_item = Menu()
    get_item.get_items()
    customer_choice = input(f"What would you like? {get_item.get_items()}: ")

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
            if payment.make_payment(customer_choice[x]['cost']) == False:
                exit()
        payment.report()
        coffee_machine.make_coffee(customer_choice)
        coffee_machine.report()
        payment.report()
        print(f"Here is your {list(customer_choice.keys())[0]}. Enjoy!")

    turn_off_machine = True
