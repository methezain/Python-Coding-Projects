# dynamic colors flower using turtle

from turtle import Turtle, Screen 

timmy = Turtle()
timmy.speed(10)

for i in range(3):
    for colour in ["red","blue","cyan","purple","black","orange"]:
        timmy.color(colour) 
        timmy.circle(100)
        timmy.left(20) 
        
myScreen = Screen()
myScreen.exitonclick() 
        