

class Menu():
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

class MenuItem():
    dummyvar = 0
# 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
def order_drink():
    selection = input("What would you like?\n1 - Espresso\n2 - Latte\n3 - Cappuccino)"
                      "\nUse 1, 2, or 3 for the selection: ")
    # Turn off the Coffee Machine by entering “off” to the prompt.
    if selection == 'off':
        turn_off()
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
