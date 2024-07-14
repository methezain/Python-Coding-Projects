## Basic event listening program


from turtle import Turtle, Screen

tim = Turtle()
canvas = Screen()

def forward_move():
    tim.forward(20)
    
    
canvas.listen()
canvas.onkey(key = "space", fun = forward_move)
canvas.exitonclick()  