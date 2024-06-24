from turtle import Turtle, Screen
import random 

timmy = Turtle()
timmy.shape("classic") 
    
colors = ["red", "green", "cyan", "blue", "orange", "brown", "navy", "pink", "purple", "yellow"]
    
def draw_shape(sides): 
    angle = 360/sides
    for side in range(sides):  
        timmy.forward(100) 
        timmy.right(angle) 
    timmy.color(random.choice(colors))
        


# triangle = draw_shape(3)
# print(triangle) 

# square = draw_shape(4)
# print(square)

# pentagone = draw_shape(5)
# print(pentagone)

# hexagone = draw_shape(6)
# print(hexagone)

# heptagone = draw_shape(7)
# print(heptagone)

# octagone = draw_shape(8)
# print(octagone) 


for sides in range(3,11): #from triangle to shape of 10 sides
    print(draw_shape(sides))
    




screen = Screen()
screen.exitonclick()