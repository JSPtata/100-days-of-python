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

machineIsOn=True
money=0

def latteDrink(resources,money):
        if resources["water"]<200:
            print("Sorry there is not enough water.")
            return money
        elif resources["milk"]<150:
            print("Sorry there is not enough milk.")
            return money
        elif resources["coffee"]<24:
            print("Sorry there is not enough coffee.")
            return money

        print("Please insert coins.\n")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))

        total=0.25*quarters+0.1*dimes+0.05*nickles+0.01*pennies
        cost=MENU["latte"]["cost"]

        if total < cost:
            print("Sorry that's not enough money.Money refunded.")
            return money
        else:
            change=round(total-cost,2)
            print(f"Here is ${change} in change.\n")
            print("Here is your latte.Enjoy!\n")

            resources['water']-=200
            resources['milk']-=150
            resources['coffee']-=24
            return money+cost

def espressooDrink(resources,money):
    if resources['water']<50:
        print("Sorry there is not enough water\n")
        return money
    elif resources['coffee']<18:
        print("Sorry there is not enough coffee\n")
        return money

    print("Please insert coins.\n")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    total = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
    cost = MENU["espresso"]["cost"]

    if total < cost:
        print("Sorry that's not enough money.Money refunded.")
        return money
    else:
        change = round(total - cost, 2)
        print(f"Here is ${change} in change.")
        print("Here is your Espresoo.Enjoy!")

        resources['water'] -= 50
        resources['coffee'] -= 18
        return money + cost

def cappuccinoDrink(resources,money):
    if resources['water']<250:
        print("Sorry there is not enough water")
        return money
    elif resources['coffee']<24:
        print("Sorry there is not enough coffee")
        return money
    elif resources['milk']<100:
        print("Sorry there is not enough milk")
        return money

    print("Please insert coins.\n")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    total = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
    cost = MENU[("cappuccino")]["cost"]

    if total < cost:
        print("Sorry that's not enough money.Money refunded.")
        return money
    else:
        change = round(total - cost, 2)
        print(f"Here is ${change} in change.")
        print("Here is your Espresoo.Enjoy!")

        resources['water'] -= 250
        resources['coffee'] -= 24
        resources['milk']-=100
        return money + cost

while machineIsOn:
    choice=input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice=='report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    elif choice=='latte':
        money=latteDrink(resources,money)
    elif choice=='espresso':
        money=espressooDrink(resources,money)
    elif choice=='cappuccino':
        money=cappuccinoDrink(resources,money)
    elif choice=='off':
        machineIsOn=False
    else:
        print("Invalid choice.")







