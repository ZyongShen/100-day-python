from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


if __name__ == "__main__":
    coffee_maker = CoffeeMaker()
    menu = Menu()
    money_machine = MoneyMachine()
    coffee_machine_on = True

    while (coffee_machine_on):
        coffee_options = menu.get_items()
        customer_question = f"What would you like? ({coffee_options}): "
        customers_choice = input(customer_question)
        if (customers_choice == "off"):
            coffee_machine_on = False
        else:
            if (customers_choice == "report"):
                print(coffee_maker.report())
            else:
                menu_item = menu.find_drink(customers_choice)
                if (menu_item):
                    # True if enough resources, False and prints if not enough resources
                    resource_sufficient = coffee_maker.is_resource_sufficient(menu_item)

                    # process coins if enough
                    if (resource_sufficient):
                        customer_payment = money_machine.make_payment(menu_item.cost)

                        if (customer_payment):
                            coffee_maker.make_coffee(menu_item)
                        

                