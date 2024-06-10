import Resources_Data

def formate_resources(resources):
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"] 
    
    return f"===============\nWater : {water} mg\nMilk : {milk} mg\nCoffee : {coffee} mg\n==============="


# main body

next_customer = True

while next_customer:
    user_choice = input("​What would you like? (espresso/latte/cappuccino): ").lower()
    
    if user_choice == "off":
        break 
    if user_choice == "report":
        print(formate_resources(Resources_Data.resources))   
        
        
        