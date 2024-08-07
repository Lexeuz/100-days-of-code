from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.colormode(255)

tim.color("blue")
tim.pencolor("green")
# # Drawing a square.
# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)

# tum = Turtle()
# tum.color("purple")
# tum.pencolor("purple")
# for _ in range(4):
#     tum.forward(100)
#     tum.right(90)

# tom = Turtle()
# tom.color("purple")
# tom.pencolor("orange")
# for _ in range(4):
#     tom.backward(100)
#     tom.left(90)

# tem = Turtle()
# tem.color("red")
# tem.pencolor("blue")

# for _ in range(4):
#     tem.backward(100)
#     tem.right(90)

# # Drawing a dashed line.
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


# # Drawing different shapes.
# def draw_shape(sides, color):
#     angle = 360 / sides
#     tim.color(color)
#     for _ in range(sides):
#         tim.forward(100)
#         tim.left(angle)


# colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown"]
# count = 0
# for i in range(3, 11):
#     draw_shape(i, colors[count])
#     count += 1


# # Random walk.
# tim.pensize(10)
def random_color():  # Use method screen.colormode(255) when using random colors in hex.
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


# direction = ["right", "left"]
# angles = [0, 90, 180, 270]
# tim.speed("fastest")
# while True:
#     tim.forward(25)
#     tim.color(random_color())
#     tim.setheading(random.choice(angles))

# # Draw a Spirograph.
tim.speed("fastest")
for _ in range(75):
    tim.color(random_color())
    tim.circle(180)
    tim.right(5)


screen.exitonclick()
