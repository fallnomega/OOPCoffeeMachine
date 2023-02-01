class CoffeeMaker():
    resources = {
        "water": 500,
        "milk": 200,
        "coffee": 100,
        "money": 100
    }

    # Prints a report of all resources.
    def report(self):
        print(f"\n\nReport on resource levels:\n"
              f"Water: {self.resources['water']}m\n"
              f"Milk: {self.resources['milk']}ml\n"
              f"Coffee: {self.resources['coffee']}g\n"
              f"Money: ${self.resources['money']}\n"
              f"Profit: ${self.resources['money'] - 100}\n\n")
        return

# - is_resource_sufficient(drink)
# Parameter drink: (MenuItem) The MenuItem object to make.
# Returns True when the drink order can be made, False if ingredients are insufficient.
# e.g. True
#
#
# - make_coffee(order)
# Parameter order: (MenuItem) The MenuItem object to make.
# Deducts the required ingredients from the resources

