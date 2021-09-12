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

OFF_CODE = 'off'
RESTOCK_CODE = 'restock'
REPORT_CODE = 'report'

SPECIAL_CODES = [OFF_CODE, REPORT_CODE, RESTOCK_CODE]

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0
}


def print_report():
    """Print report on machine resources"""
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = resources["money"]
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money:.2f}")


def restock():
    """Restock the coffee machine"""
    resources["water"] = 300
    resources["milk"] = 200
    resources["coffee"] = 100


def generate_drink_names() -> str:
    """Generate list of drinks to output"""
    menu_formatted = [f"{x} ${MENU[x]['cost']:.2f}" for x in MENU]
    return "; ".join(menu_formatted)


def is_enough_ingredients(ingredients: dict[str, int]) -> bool:
    """Check if enough resources in the machine. Returns True or False"""
    for resource_name in ingredients:
        resource_requirements = ingredients[resource_name]
        if resource_name not in resources or resources[resource_name] < resource_requirements:
            print(f"Sorry, there is not enough {resource_name}")
            return False
    return True


def remove_ingredients(ingredients: dict[str, int]):
    for resource_name in ingredients:
        resource_requirements = ingredients[resource_name]
        resources[resource_name] -= resource_requirements


coins_value = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01,
}


def get_coins() -> float:
    money = 0.0
    for coin, value in coins_value.items():
        amount = int(input(f"How many {coin} (${value:.2f}) you insert? "))
        money += value * amount
    return money


def coffee_machine():
    """General function that completes coffee_machine functions"""
    print("Welcome, to our coffee machine!")
    while True:
        # Get drink from user
        drink_name = input(f"What would you like? ({generate_drink_names()}) ").lower()

        # Check if it's a special command
        if drink_name in SPECIAL_CODES:
            if drink_name == OFF_CODE:
                print("Turning off. Buh-bye!")
                return
            elif drink_name == RESTOCK_CODE:
                restock()
            elif drink_name == REPORT_CODE:
                print_report()
            continue

        # If something unusual, tell user
        if drink_name not in MENU:
            print("Sorry, we don't have it here, I don't think..")
            continue

        # Get ingredients and cost
        drink_ingredients = MENU[drink_name]["ingredients"]
        drink_cost = MENU[drink_name]["cost"]

        # Check if there are enough resources
        if not is_enough_ingredients(drink_ingredients):
            continue

        # Get money from user
        money = get_coins()

        print(f"You've inserted ${money}.")

        # Check if enough money
        if money < drink_cost:
            print("Sorry, that's not enough money. Money refunded.")
            continue
        elif money > drink_cost:
            print(f"Here is ${money - drink_cost:.2f} in change.")

        print("Payment successful!")

        # Add money to resources and make a drink
        resources["money"] += drink_cost
        remove_ingredients(drink_ingredients)

        # Give drink to user
        print(f"Here's your {drink_name} ☕. Enjoy!")


if __name__ == '__main__':
    coffee_machine()
