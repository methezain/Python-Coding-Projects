import Resources_Data

def formate_resources(resources):
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"] 
    money = resources["money"]
    
    return f"===============\nWater : {water} mg\nMilk : {milk} mg\nCoffee : {coffee} mg\nMoney : {money} $\n==============="


def resource_checker(ingredients_dict):
    for item in ingredients_dict:
        if ingredients_dict[item] > Resources_Data.resources[item]: 
            print(f"Sorry, not enough {item}, {ingredients_dict[item] - Resources_Data.resources[item]} ml more {item} is required.")
            return False 
    return True   







# main body

next_customer = True

while next_customer:
    user_choice = input("​What would you like? ( Espresso/  Latte /  Cappuccino): ").lower()
    
    if user_choice == "off":
        break 
    elif user_choice == "report":
        print(formate_resources(Resources_Data.resources))   
    else:
        drink = Resources_Data.MENU[user_choice] 

        if resource_checker(drink["ingredients"]):
            print("you can get a drink.")
            
             