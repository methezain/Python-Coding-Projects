colors_rgb = [
    (0, 255, 0),       # Green
    (255, 0, 0),       # Red
    (0, 0, 255),       # Blue
    (255, 255, 0),     # Yellow
    (128, 0, 128),     # Purple
    (255, 165, 0),     # Orange
    (255, 192, 203),   # Pink
    (165, 42, 42),     # Brown
    (0, 255, 255),     # Cyan
    (255, 0, 255),     # Magenta
    (0, 255, 0),       # Lime
    (128, 128, 0),     # Olive
    (0, 128, 128),     # Teal
    (0, 0, 128),       # Navy
    (128, 0, 0),       # Maroon
    (64, 224, 208),    # Turquoise
    (230, 230, 250),   # Lavender
    (245, 245, 220),   # Beige
    (189, 252, 201),   # Mint
    (255, 127, 80),    # Coral
    (255, 215, 0),     # Gold
    (192, 192, 192),   # Silver
    (205, 127, 50),    # Bronze
    (220, 20, 60),     # Crimson
    (75, 0, 130),      # Indigo
    (127, 255, 0),     # Chartreuse
    (250, 128, 114),   # Salmon
    (255, 0, 255),     # Fuchsia
    (221, 160, 221),   # Plum
    (218, 112, 214),   # Orchid
    (255, 218, 185),   # Peach
    (255, 255, 240),   # Ivory
    (160, 82, 45),     # Sienna
    (238, 130, 238),   # Violet
    (255, 191, 0),     # Amber
    (0, 127, 255),     # Azure
    (42, 82, 190),     # Cerulean
    (224, 176, 255),   # Mauve
    (195, 176, 145),   # Khaki
    (200, 162, 200),   # Lilac
    (204, 204, 255),   # Periwinkle
    (242, 133, 0),     # Tangerine
    (224, 17, 95),     # Ruby
    (80, 200, 120),    # Emerald
    (15, 82, 186),     # Sapphire
    (0, 168, 107),     # Jade
    (255, 200, 124),   # Topaz
    (168, 195, 214),   # Opal
    (115, 54, 53),     # Garnet
    (153, 102, 204),   # Amethyst
    (53, 56, 57),      # Onyx
    (184, 115, 51),    # Copper
    (181, 166, 66),    # Brass
    (242, 240, 230),   # Alabaster
    (128, 0, 32),      # Burgundy
    (150, 0, 24),      # Carmine
    (255, 0, 127),     # Rose
    (204, 119, 34),    # Ochre
    (255, 219, 88),    # Mustard
    (194, 178, 128),   # Sand
    (227, 218, 201),   # Bone
    (21, 96, 189),     # Denim
    (123, 63, 0),      # Chocolate
    (112, 128, 144),   # Slate
    (54, 69, 79),      # Charcoal
    (97, 64, 81),      # Eggplant
    (255, 247, 0),     # Lemon
    (0, 255, 127),     # Spring Green
    (255, 105, 180),   # Hot Pink
    (204, 85, 0),      # Burnt Orange
    (46, 139, 87),     # Sea Green
    (25, 25, 112),     # Midnight Blue
    (255, 64, 64)      # Coral Red
]


from turtle import Turtle as t, Screen as s
import random as r

canvas = s()
canvas.colormode(255) 

timmy = t()
timmy.penup()
timmy.hideturtle()
timmy.speed("fastest")

timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
 

def draw_painting(dot_counts):
    for dot in range(1, dot_counts + 1):
        timmy.dot(20, r.choice(colors_rgb)) 
        timmy.forward(50) 
        
        if dot % 10 == 0:
            timmy.setheading(90)
            timmy.forward(50) 
            timmy.setheading(180) 
            timmy.forward(500)
            timmy.setheading(0) 
            


user_choice = int(input("How many dots to draw? : "))
draw_painting(user_choice)
        

canvas.exitonclick() 