import Data  # This loads resources and MENU from Data.py

def Machine_On():
    On = True
    identity = input("Customer/Vendor? :").lower()

    if identity == "vendor":
        print("Welcome Vendor")
        for i in Data.resources:
            Data.resources[i] += int(input(f"How much {i} did you add? "))
        print("Thanks for refilling me!")
        print(Data.resources)
        Data.save_resources()  # ✅ Persist the update
        return

    if identity == "customer":
        print("Welcome !")
        while On:
            choice = input("What would you like? (espresso/latte/cappuccino): ").strip().lower()
            if choice == "off":
                print("Machine Turned Off")
                break

            if choice not in Data.MENU:
                print("Invalid choice. Please select from espresso, latte, or cappuccino.")
                continue

            # Check resource sufficiency
            for i in Data.MENU[choice]["ingredients"]:
                if Data.resources.get(i, 0) < Data.MENU[choice]["ingredients"][i]:
                    print("Not Enough Resources.")
                    print(Data.resources)
                    break
            else:
                # Take money
                quarters = 0.25 * int(input("How many quarters?: "))
                dimes = 0.10 * int(input("How many dimes?: "))
                nickles = 0.05 * int(input("How many nickles?: "))
                pennies = 0.01 * int(input("How many pennies?: "))
                money = quarters + dimes + nickles + pennies

                if money < Data.MENU[choice]["cost"]:
                    print("Sorry that's not enough money. Money refunded.")
                else:
                    change = round(money - Data.MENU[choice]["cost"], 2)
                    print(f"Here is ${change} in change.")
                    print(f"Enjoy Your {choice} !")
                    for i in Data.MENU[choice]["ingredients"]:
                        Data.resources[i] -= Data.MENU[choice]["ingredients"][i]
                    print(Data.resources)
                    Data.save_resources()  # ✅ Persist after purchase

Machine_On()

