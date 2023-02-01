class Menu():
    # Returns all the names of the available menu items as a concatenated string.
    # e.g. “latte/espresso/cappuccino”
    def get_items(self):
        items = MenuItem()
        items = '|'
        for x in MenuItem.MENU:
            items += ' ' + x + ' |'
        return items

    # Searches the menu for a particular drink by name. Returns a MenuItem object if it exists,
    # otherwise returns None.
    def find_drink(order_name):
        drink_selected = {}
        for x in MenuItem.MENU:
            if x == order_name:
                drink_selected[x] = MenuItem.MENU[x]
                return drink_selected
        return None


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
