import Resources_Data

def formate_resources(resources):
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"] 
    money = resources["money"]
    
    return f"===============\nWater : {water} mg\nMilk : {milk} mg\nCoffee : {coffee} mg\nMoney : {money} $\n==============="


# main body

next_customer = True

while next_customer:
    user_choice = input("​What would you like? (1- Espresso/ 2- Latte / 3- Cappuccino): ")
    
    if user_choice == "off":
        break 
    if user_choice == "report":
        print(formate_resources(Resources_Data.resources))   
    if user_choice == "1":
        if Resources_Data.resources["water"] < 50:
            print(f"Not enough water, {Resources_Data.MENU["espresso"]["water"]} - {Resources_Data.resources["water"]} ml more water is required.") 
            
        elif Resources_Data.resources["coffee"] < 18:
            print(f"Not enough coffee, {Resources_Data.MENU["espresso"]["coffee"]} - {Resources_Data.resources["coffee"]} ml more coffee is required.") 
        elif Resources_Data.resources["money"] < 1.5:
            print(f"No enough money, {Resources_Data.MENU["espresso"]["cost"]} - {Resources_Data.resources["money"]}$ more money is required.")  
        
        