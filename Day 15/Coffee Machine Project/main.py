
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}

refill_amount = {
    "water": 150,
    "milk": 100,
    "coffee": 50,
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0

runCoffeeMachine = True
while runCoffeeMachine:
    print("")
    print(f"Water: {resources["water"]}ml | Milk: {resources["milk"]}ml | Coffee: {resources["coffee"]}ml | "
          f"Money: ${"%.2f" % money}")
    new_drink = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if new_drink == "off":
        runCoffeeMachine = False
    elif new_drink == "refill":
        refill_resource = input("Which resource to be refilled? (water/milk/coffee): ").lower()
        if refill_resource == "coffee" or refill_resource == "water" or refill_resource == "milk":
            if money >= 1:
                money -= 1
                resources[refill_resource] += refill_amount[refill_resource]
                print(f"You lost $1, but got {refill_amount[refill_resource]}ml of {refill_resource} refilled!")
            else:
                print("I am sorry, but that requires $1. Please come back later.")
        else:
            print("I am sorry, but that resource does not exist. Please try again later.")

    elif new_drink == "espresso" or new_drink == "latte" or new_drink == "cappuccino":
        resources_sufficient = True
        for resource in resources:
            if resources[resource] < MENU[new_drink]["ingredients"][resource]:
                resources_sufficient = False
                print(f"I am sorry, but I don't have enough {resource}!")
        if resources_sufficient:
            quarters = int(input("How many Quarters: "))
            dimes = int(input("How many Dimes: "))
            nickels = int(input("How many Nickels: "))
            pennies = int(input("How many Pennies: "))
            money_spent = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickels) + (0.01 * pennies)
            if money_spent >= MENU[new_drink]["cost"]:
                for resource in resources:
                    resources[resource] -= MENU[new_drink]["ingredients"][resource]
                money_leftover = money_spent - MENU[new_drink]["cost"]
                money += MENU[new_drink]["cost"]
                print(f"You got ${"%.2f" % money_leftover} back! Enjoy your {new_drink}!")
            else:
                print(f"I am sorry, but ${"%.2f" % money_spent} will not cover it. "
                      f"The {new_drink} requires ${"%.2f" % MENU[new_drink]["cost"]}!")
    else:
        print("That drink does not exist!")
print(f"We made ${"%.2f" % money}! Yay!")
