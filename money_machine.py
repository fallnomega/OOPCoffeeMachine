
class MoneyMachine():
    QUARTERS = .25
    DIMES = .10
    NICKLES = .05
    PENNIES = .01





# Process coins.
def process_coins(drink_selection):
    drink_name = list(MENU)[int(drink_selection) - 1]
    print(f"Please insert coins to pay for your {drink_name}.\n"
          f"The total cost is: ${MENU[drink_name]['cost']} ")

    inserted_quarters = int(input("How many quarters to insert?") or 0)
    inserted_dimes = int(input("How many dimes to insert?") or 0)
    inserted_nickles = int(input("How many nickles to insert?") or 0)
    inserted_pennies = int(input("How many pennies to insert?") or 0)
    total_inserted = round((inserted_quarters * QUARTERS) + (inserted_dimes * DIMES) + (inserted_nickles * NICKLES) + (
            inserted_pennies * PENNIES), 2)
    print(f"Total inserted is: ${round(total_inserted, 2)}")
    # Check transaction successful?
    if check_transaction_successful(total_inserted, drink_name) is False:
        print("Sorry that's not enough money. Money refunded.")
        exit()
    else:
        if float(MENU[drink_name]['cost']) < total_inserted:
            print(f"{total_inserted} - {float(MENU[drink_name]['cost'])}")
            change = total_inserted - float(MENU[drink_name]['cost'])
            resources['money'] += MENU[drink_name]['cost']
            print(f"Here is ${change} dollars in change")

        else:
            resources['money'] += MENU[drink_name]['cost']
    return


def check_transaction_successful(inserted_money, drink_name):
    if int(MENU[drink_name]['cost']) > inserted_money:
        return False
    else:
        return True

