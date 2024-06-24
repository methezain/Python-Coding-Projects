from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("classic")
timmy.fillcolor("blue")

# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)

for directions in range(4):
    timmy.forward(100)
    timmy.left(90)
        
screen = Screen()
screen.exitonclick() 