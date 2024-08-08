import colorgram
import random
from turtle import Turtle, Screen

# Extract colors from the image.
colors = colorgram.extract("image.jpg", 20)
rgb_colors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

# print(rgb_colors)

# # Project - The Hirst Painting Project.
screen = Screen()
screen.colormode(255)

tim = Turtle()
tim.penup()
tim.hideturtle()
tim.speed("fastest")

pos_x = -230
pos_y = -230
tim.setx(pos_x)
tim.sety(pos_y)

count = 0
for _ in range(100):
    tim.color(random.choice(rgb_colors))
    tim.dot(20)
    tim.forward(50)
    count += 1
    if count >= 10:
        pos_y += 50
        tim.setpos(pos_x, pos_y)
        count = 0

screen.exitonclick()
