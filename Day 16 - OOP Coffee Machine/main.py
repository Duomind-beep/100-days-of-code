from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_menu = Menu()
my_coffeemaker = CoffeeMaker()
my_moneymachine = MoneyMachine()

still_on = True
while still_on is True:
    options = my_menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        still_on = False
    elif choice == "report":
        my_coffeemaker.report()
        my_moneymachine.report()
    else:
        drink = my_menu.find_drink(choice)
        is_sufficient = my_coffeemaker.is_resource_sufficient(drink)
        if is_sufficient:
            print(f"That would be ${drink.cost}")
            if my_moneymachine.make_payment(drink.cost):
                my_coffeemaker.make_coffee(drink)



