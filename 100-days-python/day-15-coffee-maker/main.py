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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0
on = True

def sufficient_check(order):
    ingredients = MENU[order]["ingredients"]
    insufficients = []
    is_sufficient = True
    for key in ingredients.keys():
        if (int(resources[key]) < int(ingredients[key])):
            insufficients.append(key)
    if (len(insufficients) > 0):
        is_sufficient = False
    return (is_sufficient, insufficients)

def make_coffee(order):
    ingredients = MENU[order]["ingredients"]
    for key in ingredients.keys():
        resources[key] -= ingredients[key]
    print(f"Here is your {order}. Enjoy!")


def make_order(order):
    # resource check
    # if not enough, return not sufficient
    # else make coffee order
    sufficiency = sufficient_check(order)
    # send a message if not sufficient
    if (not sufficiency[0]):
        # ingrdeints sufficiency check
        print (f"Sorry there is not enough {sufficiency[1]}")
    else:
        item = MENU[order]
        money_given = 0
        # if the sufficiency check passed then get the coins
        print("Please insert coins.")
        quarters = int(input("How many quarters?:"))
        dimes = int(input("How many dimes?:"))
        nickles = int(input("How many nickles?:"))
        pennies = int(input("How many pennies?:"))
        money_given = 0.25*quarters + 0.1*dimes + 0.05*nickles + 0.01*pennies
        # check if less than cost
        # check if more than cost, offer change
        # if enough, add as profit
        # money check
        if (money_given < item["cost"]):
            print("Sorry that's not enough money. Money refunded.")
            money_given = 0
        elif (money_given > item["cost"]):
            change = round(money_given - item["cost"], 2)
            print(f"Here is ${change} dollars in change.")
        else:
            global profit # tells the program to use the global version while changing values
            profit += item["cost"] # add profit
            make_coffee(order)

        


if __name__ == "__main__":
    while (on):
        coffee_order = input("What would you like? (espresso/latte/cappuccino) ")
        if (coffee_order == "off"):
            on = False
        elif (coffee_order == "report"):
            print(
                f'Water: {resources["water"]}ml \n'
                f'Milk: {resources["milk"]}ml \n'
                f'Coffee: {resources["coffee"]}g \n'
                f'Money: ${profit}'
            )
        else:
            make_order(coffee_order)

