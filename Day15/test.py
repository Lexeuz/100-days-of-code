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
user_choice = "cappuccino"
money = 0
drink = MENU[user_choice]

for ingredient in drink["ingredients"]:
    print(ingredient)
    resources[ingredient] -= drink["ingredients"][ingredient]
money = drink["cost"]
print(
    f"These are the resources: \n- Water: {resources['water']}\n- Milk: {resources['milk']}\n- Coffee: {resources['coffee']}\n- Money: ${money}"
)
