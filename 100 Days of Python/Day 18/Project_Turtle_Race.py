from turtle import Turtle, Screen
import random 
canvas = Screen()

canvas.setup(width=500, height=400) 
canvas.title("Project Turtle Race by Ali Zain")
user_choice = canvas.textinput(title="make a bet", prompt="Which Turtle will win (red, purple, blue, orange, green or cyan): ")


colors = ['red','purple','blue','orange','green','cyan']
y_positions = [-60, -30, 0, 30, 60, 90]
all_turtles = []
 
is_race_on = False


for tim in range(0 , 6):
    new_timmy = Turtle(shape="turtle")
    new_timmy.color(colors[tim]) 
    new_timmy.penup()
    new_timmy.goto(x=-230, y=y_positions[tim]) 
    all_turtles.append(new_timmy)
    

if user_choice:
    is_race_on = True
    
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner_color = turtle.pencolor() 
            if winner_color == user_choice:
                print("You won it.")
            else:
                print(f"You lost it. {winner_color} turtle won the race.")
        
        distance = random.randint(0,10)
        turtle.forward(distance) 

canvas.exitonclick()