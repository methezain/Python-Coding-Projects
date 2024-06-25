from turtle import Turtle as t, Screen as S
import random 

canvas = S()
canvas.colormode(255)

timmy = t()
timmy.shape("classic")
timmy.speed("fastest")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    
    final_color = (r, g, b)
    return final_color

def draw_spirograph(gap_Size):
    for i in range(int(360/gap_Size)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + gap_Size)
        
        
        
draw_spirograph(5) 




canvas.exitonclick()