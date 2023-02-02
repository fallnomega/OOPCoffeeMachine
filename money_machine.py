class MoneyMachine():
    QUARTERS = .25
    DIMES = .10
    NICKLES = .05
    PENNIES = .01
    MONEY = 0

    # Prints the current profit
    def report(self):
        print(f"Profit so far: ${self.MONEY}\n\n")

    # Returns True when payment is accepted, or False if insufficient.
    # e.g. False
    def make_payment(self, cost):
        print(f"Please insert coins to pay for your drink. The total cost is: ${cost} ")

        inserted_quarters = int(input("\n\nHow many quarters to insert?") or 0)
        inserted_dimes = int(input("How many dimes to insert?") or 0)
        inserted_nickles = int(input("How many nickles to insert?") or 0)
        inserted_pennies = int(input("How many pennies to insert?") or 0)
        print("\n\n")
        total_inserted = round(
            (inserted_quarters * self.QUARTERS) + (inserted_dimes * self.DIMES) + (inserted_nickles * self.NICKLES) + (
                    inserted_pennies * self.PENNIES), 2)
        print(f"Total inserted is: ${round(total_inserted, 2)}")
        # Check transaction successful?
        if total_inserted < cost:
            print("Sorry that's not enough money. Money refunded.")
            return False
        else:
            if cost < total_inserted:
                change = total_inserted - float(cost)
                print(f"Here is ${round(change, 2)} dollars in change")
                self.MONEY += cost
                return True
            else:
                self.MONEY += cost
                return True
