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
money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resource_ess(menu, resources_left):
    if (resources_left["water"] - menu["water"]) < 0:
        print("There isn't enough water")
        return False
    if(resources_left["coffee"] - menu["coffee"]) < 0:
        print("There isn't enough coffee")
        return False
    else:
        return True


def check_resource(menu, resources_left):
    if (resources_left["water"] - menu["water"]) < 0:
        print("There isn't enough water")
        return False
    if (resources_left["milk"] - menu["milk"]) < 0:
        print("There isn't enough milk")
        return False
    if(resources_left["coffee"] - menu["coffee"]) < 0:
        print("There isn't enough coffee")
        return False
    else:
        return True


def update_resource(coffee, drink_choice, resources_machine, profit):
    if drink_choice != "espresso":
        resources_machine["water"] = resources_machine["water"] - coffee[choice]["ingredients"]["water"]
        resources_machine["milk"] = resources_machine["milk"] - coffee[choice]["ingredients"]["milk"]
        resources_machine["coffee"] = resources_machine["coffee"] - coffee[choice]["ingredients"]["coffee"]
    else:
        resources_machine["water"] = resources_machine["water"] - coffee[choice]["ingredients"]["water"]
        resources_machine["coffee"] = resources_machine["coffee"] - coffee[choice]["ingredients"]["coffee"]

    profit += coffee[choice]["cost"]
    return profit


def sum_coins(coffee, choice_drink, resources_left, profit):
    quarters = int(input("How many quarters?"))
    dimes = int(input("How many dimes?"))
    nickles = int(input("How many nickles?"))
    pennies = int(input("How many pennies?"))

    value = quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01
    change_left = value - coffee[choice_drink]["cost"]

    if change_left < 0:
        print("Sorry that's not enough money. Money refunded.")
    else:
        profit = update_resource(coffee,choice_drink, resources_left, profit)
    return round(change_left, 2), profit


resource = False
while True:
    choice = input("What would you like? (espresso/latte/cappuccino):")

    if choice == "espresso":
        resource = check_resource_ess(MENU["espresso"]["ingredients"], resources)
    if choice == "latte":
        resource = check_resource(MENU["latte"]["ingredients"], resources)
    if choice == "cappuccino":
        resource = check_resource(MENU["cappuccino"]["ingredients"], resources)
    if choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    if resource is True and (choice == "espresso" or choice == "latte" or choice == "cappuccino"):
        print("Please insert coins.")
        change, money = sum_coins(MENU, choice, resources, money)
        print(f"Need ${-change} more")

    if choice == "off":
        break