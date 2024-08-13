from turtle import Screen
from paddle import Paddle

POSITIONS = [(350, 0), (-350, 0)]

screen = Screen()
screen.title("Pong - Alexander E. Adarme")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)


p_1 = Paddle(pos=POSITIONS[0])
p_2 = Paddle(pos=POSITIONS[1])

screen.listen()

screen.onkey(key="w", fun=p_1.go_up)
screen.onkey(key="s", fun=p_1.go_down)

screen.onkey(key="u", fun=p_2.go_up)
screen.onkey(key="j", fun=p_2.go_down)


game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
