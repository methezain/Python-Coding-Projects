# basic square using turtle

from turtle import Turtle, Screen

myTurtle = Turtle()
myTurtle.color("red")
myTurtle.shape("turtle")

myTurtle.backward(100)

for i in range(0,4):
    myTurtle.forward(200)
    myTurtle.left(90)
    
myCanvas = Screen()
myCanvas.exitonclick() 