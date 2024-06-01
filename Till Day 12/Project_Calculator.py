import math
import sys
from art import calculator_logo


def add(n , m):
    return n + m

def subtract(n , m):
    return n - m

def multiplication(n , m):
    return n * m

def division(n , m):
    return n / m

def power(n , m):
    return n ** m

def square_root(n , m):
    return math.sqrt(n , m)  


operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiplication,
    "/" : division,
    "**" : power
}

def calculator():
    print(calculator_logo) 
    
    while(True):
        num1 = float(input("Enter the first number: "))

        for key in operations:
            print(key)  
        
        user_oper = input("Which operation to perform: ") 
        calculation_function = operations[user_oper]

        num2 = float(input("Enter the second number: ")) 

        answer = calculation_function(num1, num2)
        print(f"{num1} {user_oper} {num2} = {answer}") 
        
        should_continue = input("Type 'y' to continue, and 'n' to exit:  ").lower()
        
        if should_continue == "n":
            print("Exited Successfully.\n\n")
            break
        
calculator() 

   