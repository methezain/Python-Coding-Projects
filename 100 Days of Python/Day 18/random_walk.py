from turtle import Turtle, Screen
import random 

canvas = Screen()
canvas.colormode(255)


timmy = Turtle()
timmy.shape("classic") 
timmy.width(7)
timmy.speed(6)

directions = [0, 90, 180, 270]
#colors = ["red", "green", "cyan", "indigo", "orange", "brown", "navy", "blue violet", "purple", "dark slate gray"]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    final_color = (r, g, b)
    return final_color

 
for step in range(200):
    timmy.color(random_color())
    timmy.forward(30) 
    timmy.setheading(random.choice(directions))
    
    


canvas.exitonclick()