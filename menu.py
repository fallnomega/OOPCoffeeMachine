class Menu():
    # 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    def order_drink(self):
        selection = input("What would you like?\n1 - Espresso\n2 - Latte\n3 - Cappuccino)"
                          "\nUse 1, 2, or 3 for the selection: ")
        # Turn off the Coffee Machine by entering “off” to the prompt.
        if selection == 'off':
            self.turn_off()
        # Print report.
        elif selection == 'report':
            print_report()
        elif int(selection) > 3:
            print("\n\nWrong selection, try again\n\n")
            exit()
        else:

            return selection

    def turn_off():
        print("\n\nTurning off the machine. Good bye!\n\n")
        exit()
        return


class MenuItem():
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
