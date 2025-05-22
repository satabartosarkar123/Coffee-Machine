import json

try:
    with open("resources.json") as f:
        resources = json.load(f)
except FileNotFoundError:
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100
    }

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0
    }
}

def save_resources():
    with open("resources.json", "w") as f:
        json.dump(resources, f)


resource_sufficiency = True
