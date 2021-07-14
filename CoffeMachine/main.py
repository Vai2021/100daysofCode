# TODO :1. Prompt user by asking What would you like? (espresso/latte/cappuccino):

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

def calculate_coins():
    """returns total calculated from the coins inserted"""
    print("Please insert coins")
    total = int(input("How many penny?")) * 0.01
    total += int(input("How many Dime?")) * 0.1
    total += int(input("How many Nickel?")) * 0.05
    total += int(input("How many Quarter?")) * 0.25

    return total


def is_resource_sufficient(order_ingredients):
    """return true when order can be made otherwise return false for insufficient ingredients"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def is_transcation_sucessful(money_received, drink_cost):
    """return True if payment is accepted otherwise return false"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost,2)
        print(f"Here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry,That is not enough money.Money refunded")
        return False


def make_coffee(drink_name,order_ingredients):
    """deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}☕️..Enjoy")



profit = 0
is_on = True
while is_on:

    user_input = input("What would you like to order?(espresso/latte/cappuccino):")
    #print(user_input)
    if user_input == 'off':
        is_on = False
    elif user_input == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}ml")
        print(f"Money:${profit}")
    else:
        drink = MENU[user_input]
        if is_resource_sufficient(drink["ingredients"]):
            payment = calculate_coins()
            if is_transcation_sucessful(payment,drink["cost"]):
                make_coffee(user_input,drink["ingredients"])

# TODO: 2.Turn off coffee machine using off


# TODO: 3.When user enter report print report


# TODO: 4.check for resources

# TODO: 5.process coins

# TODO: 6.check for successful transaction


# TODO: 7 .MAke coffee
