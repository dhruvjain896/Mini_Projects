coffee_types = {'espresso': [{'Water': 50, 'Coffee': 18}, {'Price': 1.50}],
                'latte': [{'Water': 200, 'Coffee': 24, 'Milk': 150}, {'Price': 2.50}],
                'cappuccino': [{'Water': 250, 'Coffee': 24, 'Milk': 100}, {'Price': 3.00}]}

coffee_machine = {'Water': [300, 'ml'], 'Coffee': [100, 'g'], 'Milk': [200, 'ml'], 'Money': ['$', 0.00]}
coins = {'penny': 0.01, 'dime': 0.10, 'nickel': 0.05, 'quarter': 0.25}


def report():
    for item in coffee_machine:
        print(f"{item}: {coffee_machine[item][0]}{coffee_machine[item][1]}")


def check_resources(variant):
    for ingredients in coffee_types[variant][0]:
        if coffee_machine[ingredients][0] >= coffee_types[variant][0][ingredients]:
            pass
        else:
            return ingredients
    return 'true'


def deduct_resources(variant):
    for ingredients in coffee_types[variant][0]:
        coffee_machine[ingredients][0] -= coffee_types[variant][0][ingredients]


def insert_coins(variant):
    coffee_price = coffee_types[variant][1]['Price']

    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickels = int(input("how many nickels?: "))
    pennies = int(input("how many pennies?: "))

    money = 0.0
    quarters *= coins['quarter']
    dimes *= coins['dime']
    nickels *= coins['nickel']
    pennies *= coins['penny']
    money += quarters + dimes + nickels + pennies
    return round(money - coffee_price, 2)


choice = "on"

while choice != "off":
    choice = input(
        f"What would you like? (espresso ${coffee_types['espresso'][1]['Price']} / latte ${coffee_types['latte'][1]['Price']} / cappuccino ${coffee_types['cappuccino'][1]['Price']}): ")
    if choice == 'off':
        break
    if choice == "report":
        report()
    else:
        var_of_check_resources = check_resources(choice)
        if var_of_check_resources == 'true':
            print("Please insert coins.")
            change = insert_coins(choice)
            if change >= 0:
                print(f"Here is your ${change} in change.")
                coffee_machine['Money'][1] += coffee_types[choice][1]['Price']
            else:
                print("Sorry that's not enough money. Money refunded.")
            deduct_resources(choice)
            print(f"Here is your {choice} ☕. Enjoy!.")
        else:
            print(f"Sorry there is not enough {var_of_check_resources}.")
