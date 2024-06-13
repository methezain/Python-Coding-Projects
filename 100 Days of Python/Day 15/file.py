if Resources_Data.resources["water"] < 50:
            print(f"Not enough water, {Resources_Data.MENU["espresso"]["water"] - Resources_Data.resources["water"]} ml more water is required.") 
            
        elif Resources_Data.resources["coffee"] < 18:
            print(f"Not enough coffee, {Resources_Data.MENU["espresso"]["coffee"] - Resources_Data.resources["coffee"]} ml more coffee is required.") 
        elif Resources_Data.resources["money"] < 1.5:
            print(f"No enough money, {Resources_Data.MENU["espresso"]["cost"] - Resources_Data.resources["money"]}$ more money is required.")  
        
    elif user_choice == "2":
        if Resources_Data.resources["water"] < 200:
            print(f"Not enough water, {Resources_Data.MENU["espresso"]["water"] - Resources_Data.resources["water"]} ml more water is required.") 
            
        elif Resources_Data.resources["coffee"] < 24:
            print(f"Not enough coffee, {Resources_Data.MENU["espresso"]["coffee"] - Resources_Data.resources["coffee"]} ml more coffee is required.") 
            
        elif Resources_Data.resources["money"] < 2.5:
            print(f"No enough money, {Resources_Data.MENU["espresso"]["cost"] - Resources_Data.resources["money"]}$ more money is required.")
        
        elif Resources_Data.resources["milk"] < 150:
            print(f"No enoug milk, {Resources_Data.MENU["latte"]["ingredients"]["milk"] - Resources_Data.resources["milk"]} ml more milk is required.") 