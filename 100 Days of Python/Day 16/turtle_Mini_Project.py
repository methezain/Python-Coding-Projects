# basic flower using turtle

from turtle import Turtle , Screen

timmy = Turtle()  

for colour in ["purple", "orange", "red", "black", "cyan", "navy"]:
    timmy.color(colour)
    timmy.circle(75)
    timmy.left(60)

myScreen = Screen()
myScreen.exitonclick()