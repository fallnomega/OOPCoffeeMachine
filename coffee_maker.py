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

    # Returns True when the drink order can be made, False if ingredients are insufficient.
    # e.g. True
    def is_resource_sufficient(self, drink):
        # print (drink['espresso'])
        # print(drink.keys())
        # print(list(drink.keys())[0])
        # print(type(drink))
        # espresso check
        if list(drink.keys())[0] == 'espresso':
            print("Checking espresso resources.")
            if int(self.resources['water']) < int(drink['espresso']['ingredients']['water']):
                print("Sorry there is not enough water.")
                return 0
            elif int(self.resources['coffee']) < int(drink['espresso']['ingredients']['coffee']):
                print("Sorry there is not enough coffee beans.")
                return 0
            else:
                print("Resources are available for the Espresso, proceeding")
                return 1

        # latte check
        if list(drink.keys())[0] == 'latte':
            print("Checking latte resources.")
            if int(self.resources['water']) < int(drink['latte']['ingredients']['water']):
                print("Sorry there is not enough water.")
                return 0
            elif int(self.resources['milk']) < int(drink['latte']['ingredients']['milk']):
                print("Sorry there is not enough milk.")
                return 0
            elif int(self.resources['coffee']) < int(drink['latte']['ingredients']['coffee']):
                print("Sorry there is not enough coffee beans.")
                return 0
            else:
                print("Resources are available for the Latte, proceeding")
                return 1

        # Cappuccino check
        if list(drink.keys())[0] == 'cappuccino':
            print("Checking cappuccino resources.")
            if int(self.resources['water']) < int(drink['cappuccino']['ingredients']['water']):
                print("Sorry there is not enough water.")
                return 0
            elif int(self.resources['milk']) < int(drink['cappuccino']['ingredients']['milk']):
                print("Sorry there is not enough milk.")
                return 0
            elif int(self.resources['coffee']) < int(drink['cappuccino']['ingredients']['coffee']):
                print("Sorry there is not enough coffee beans.")
                return 0
            else:
                print("Resources are available for the Cappuccino, proceeding")
                return 1
        return

    # Parameter order: (MenuItem) The MenuItem object to make.
    # Deducts the required ingredients from the resources
    def make_coffee(self, order):

        if list(order.keys())[0] == 'espresso':
            self.resources['water'] -= order['espresso']['ingredients']['water']
            self.resources['coffee'] -= order['espresso']['ingredients']['coffee']
            return
        if list(order.keys())[0] == 'latte':
            self.resources['water'] -= order['latte']['ingredients']['water']
            self.resources['coffee'] -= order['latte']['ingredients']['coffee']
            self.resources['milk'] -= order['latte']['ingredients']['milk']
            return
        else:
            self.resources['water'] -= order['cappuccino']['ingredients']['water']
            self.resources['coffee'] -= order['cappuccino']['ingredients']['coffee']
            self.resources['milk'] -= order['cappuccino']['ingredients']['milk']
            return
