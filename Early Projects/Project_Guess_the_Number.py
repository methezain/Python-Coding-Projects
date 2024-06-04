# include error handling in inputs in this program.
import random 
from art import number_guesser_logo


def Guess_Number():
    print(number_guesser_logo)
    
    random_number = random.randint(1,100)  
     
    
    user_choice = input("\n\nChoose difficulty level. \n\nEasy\nHard.\n\n").lower()
    if user_choice == "easy":
        count = 10
    elif user_choice == "hard":
        count = 5 
    else: 
        print("Invalid Choice, Defaulting to Hard Mode.\n")
        count = 5
    while(True):
        user_input = int(input(f"You have {count} tries left.\nEnter a digit (1 - 100):  "))
        count -= 1         
        
        if count == 0 and user_input != random_number: 
            print(f"\n----------------------------------------------\n----------------------------------------------\nYou failed to guess the number. The answer was {random_number}.\n----------------------------------------------\n----------------------------------------------") 
            break
        elif user_input > random_number:
            print("Too High.\n") 
            pass  
        elif user_input < random_number:
            print("Too Low.\n")
            pass 
        elif user_input == random_number:
            print("\n----------------------------------------------\n----------------------------------------------\nCongratulations, You guessed the Right digit.\n----------------------------------------------\n----------------------------------------------")    
            break           
        
        
Guess_Number() 