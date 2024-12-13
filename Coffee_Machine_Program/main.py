from random import choice

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_making=CoffeeMaker()
machine_money=MoneyMachine()
menu=Menu()

maker_on=True

while maker_on:
    #options=menu.get_items()
    choice=input(f"What would you like? ({menu.get_items()}):").lower()
    if choice=="off":
        maker_on=False
    elif choice=="report":
        coffee_making.report()
        machine_money.report()
    else:
        drink=menu.find_drink(choice)
        if coffee_making.is_resource_sufficient(drink) and machine_money.make_payment(drink.cost):
            coffee_making.make_coffee(drink)
