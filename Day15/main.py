import os
from time import sleep
from art import logo, off

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
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0


def add_resources():
    for ingredient in resources:
        resources[ingredient] += 150


def prepare_drink(drink):
    for ingredient in drink["ingredients"]:
        resources[ingredient] -= drink["ingredients"][ingredient]


def process_money(drink):
    global money
    print("Please insert coins:")
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    pennies = float(input("How many pennies?: "))
    user_money = 0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies
    if user_money >= drink["cost"]:
        print(f"Here is ${round(user_money - drink['cost'], 2)} in change.")
        money += drink["cost"]
        return True
    else:
        print(f"Sorry that is not enough money. ${user_money} refunded")


def check_resources(drink):
    for ingredient in drink["ingredients"]:
        if drink["ingredients"][ingredient] > resources[ingredient]:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True


def report():
    print(
        f"These are the resources: \n- Water: {resources['water']}\n- Milk: {resources['milk']}\n- Coffee: {resources['coffee']}\n- Money: ${money}"
    )


def coffee_machine():
    is_on = True
    while is_on:
        os.system("cls")
        print(logo)
        user_choice = input("What would you like? (espresso / latte / cappuccino): ")
        if user_choice == "report":
            report()
        elif user_choice == "off":
            print(off)
            sleep(4)
            os.system("cls")
            is_on = False
        elif user_choice == "add":
            add_resources()
        elif (
            user_choice == "espresso"
            or user_choice == "latte"
            or user_choice == "cappuccino"
        ):
            drink = MENU[user_choice]
            if check_resources(drink) == True:
                if process_money(drink) == True:
                    prepare_drink(drink)
                    print(f"Here is your {user_choice}☕. Enjoy!")
        else:
            print("Error! Try again.")

        sleep(3)


coffee_machine()
