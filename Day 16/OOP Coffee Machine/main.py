from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

myMenu = Menu()
myCoffeeMaker = CoffeeMaker()
myMoneyMachine = MoneyMachine()

runCoffeeMachine = True
while runCoffeeMachine:
    new_command = input(f"What would you like? {myMenu.get_items()}: ").lower()
    if new_command == "off":
        runCoffeeMachine = False
    elif new_command == "report":
        myCoffeeMaker.report()
        myMoneyMachine.report()
    elif myMenu.find_drink(new_command) is not None:
        new_drink = myMenu.find_drink(new_command)
        if myCoffeeMaker.is_resource_sufficient(new_drink):
            if myMoneyMachine.make_payment(new_drink.cost):
                myCoffeeMaker.make_coffee(new_drink)
