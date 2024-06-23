# PROGRAM REQUIREMENTS 
## 1- Print Report 
## 2- Check Resource Sufficient 
## 3- process the coins 
## 4- check transaction successful 
## 5- Make Coffee 


from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine 

menu = Menu()
coffee = CoffeeMaker() 
profit = MoneyMachine() 



is_on = True

avalaible_options = menu.get_items()

while is_on:
    
    choice = input(f"What would you like? ({avalaible_options}) : ").lower()
    
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee.report()
        profit.report()
    else: 
        drink = menu.find_drink(choice) 
        if coffee.is_resource_sufficient(drink) and profit.make_payment(drink.cost): 
            coffee.make_coffee(drink )  
    
    