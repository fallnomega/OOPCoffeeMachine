class CoffeeMaker():
    dummyvar = 0


resources = {
    "water": 500,
    "milk": 200,
    "coffee": 100,
    "money": 100
}




def print_report():
    print(f"\n\nReport on resource levels:\n"
          f"Water: {resources['water']}m\n"
          f"Milk: {resources['milk']}ml\n"
          f"Coffee: {resources['coffee']}g\n"
          f"Money: ${resources['money']}\n"
          f"Profit: ${resources['money'] - 100}\n\n")
    return



def check_resources_availability(drink_to_check):
    # espresso check
    if drink_to_check == '1':
        print("Checking espresso resources.")
        if int(resources['water']) < int(MENU['espresso']['ingredients']['water']):
            print("Sorry there is not enough water.")
            return 0
        elif int(resources['coffee']) < int(MENU['espresso']['ingredients']['coffee']):
            print("Sorry there is not enough coffee beans.")
            return 0
        else:
            return 1

    # latte check
    if drink_to_check == '2':
        print("Checking latte resources.")
        if int(resources['water']) < int(MENU['latte']['ingredients']['water']):
            print("Sorry there is not enough water.")
            return 0
        elif int(resources['milk']) < int(MENU['latte']['ingredients']['milk']):
            print("Sorry there is not enough milk.")
            return 0
        elif int(resources['coffee']) < int(MENU['latte']['ingredients']['coffee']):
            print("Sorry there is not enough coffee beans.")
            return 0
        else:
            return 1

    # Cappuccino check
    if drink_to_check == '3':
        print("Checking cappuccino resources.")
        if int(resources['water']) < int(MENU['cappuccino']['ingredients']['water']):
            print("Sorry there is not enough water.")
            return 0
        elif int(resources['milk']) < int(MENU['cappuccino']['ingredients']['milk']):
            print("Sorry there is not enough milk.")
            return 0
        elif int(resources['coffee']) < int(MENU['cappuccino']['ingredients']['coffee']):
            print("Sorry there is not enough coffee beans.")
            return 0
        else:
            return 1
    return


# Make Coffee.
def make_coffee(drink_to_be_made):
    if int(drink_to_be_made) == 1:
        resources['water'] -= MENU['espresso']['ingredients']['water']
        resources['coffee'] -= MENU['espresso']['ingredients']['coffee']
        return
    if int(drink_to_be_made) == 2:
        resources['water'] -= MENU['latte']['ingredients']['water']
        resources['coffee'] -= MENU['latte']['ingredients']['coffee']
        resources['milk'] -= MENU['latte']['ingredients']['milk']
        return
    else:
        resources['water'] -= MENU['cappuccino']['ingredients']['water']
        resources['coffee'] -= MENU['cappuccino']['ingredients']['coffee']
        resources['milk'] -= MENU['cappuccino']['ingredients']['milk']
        return
    return
