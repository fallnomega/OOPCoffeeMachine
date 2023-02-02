
class MoneyMachine():
#     - report()
# Prints the current profit
# e.g.
# Money: $0
#
    def make_payment(self, cost):
        print(f"make_payment cost: {cost}")

        # drink_name = list(MENU)[int(drink_selection) - 1]
        # print(f"Please insert coins to pay for your {drink_name}.\n"
        #       f"The total cost is: ${MENU[drink_name]['cost']} ")
        #
        # inserted_quarters = int(input("How many quarters to insert?") or 0)
        # inserted_dimes = int(input("How many dimes to insert?") or 0)
        # inserted_nickles = int(input("How many nickles to insert?") or 0)
        # inserted_pennies = int(input("How many pennies to insert?") or 0)
        # total_inserted = round(
        #     (inserted_quarters * QUARTERS) + (inserted_dimes * DIMES) + (inserted_nickles * NICKLES) + (
        #             inserted_pennies * PENNIES), 2)
        # print(f"Total inserted is: ${round(total_inserted, 2)}")
        # # Check transaction successful?
        # if check_transaction_successful(total_inserted, drink_name) is False:
        #     print("Sorry that's not enough money. Money refunded.")
        #     exit()
        # else:
        #     if float(MENU[drink_name]['cost']) < total_inserted:
        #         print(f"{total_inserted} - {float(MENU[drink_name]['cost'])}")
        #         change = total_inserted - float(MENU[drink_name]['cost'])
        #         resources['money'] += MENU[drink_name]['cost']
        #         print(f"Here is ${change} dollars in change")
        #
        #     else:
        #         resources['money'] += MENU[drink_name]['cost']
        # return

        return 0
# Parameter cost: (float) The cost of the drink.
# Returns True when payment is accepted, or False if insufficient.
# e.g. False
# 5. Process coins.
# a. If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.
# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

    dummyvar = 0

