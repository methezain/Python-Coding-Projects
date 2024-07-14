from turtle import Turtle, Screen

tim = Turtle()
canvas = Screen()

def forward():
    tim.forward(20)
    
def backward():
    tim.backward(20)
    
def left():
    tim.left(10)
    tim.forward(20)
    
def right():
    tim.right(10)
    tim.forward(20)
    
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()    
    
    

canvas.listen()

canvas.onkey(key = "w" , fun = forward)
canvas.onkey(key = "s" , fun = backward)
canvas.onkey(key = "a" , fun = left)
canvas.onkey(key = "d" , fun = right)
canvas.onkey(key = "c" , fun = clear)

canvas.exitonclick()