from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import Scoreboard

POSITIONS = [(350, 0), (-350, 0)]

screen = Screen()
screen.title("Pong - Alexander E. Adarme")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

l_paddle = Paddle(pos=POSITIONS[1])
r_paddle = Paddle(pos=POSITIONS[0])
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(key="Up", fun=r_paddle.go_up)
screen.onkey(key="Down", fun=r_paddle.go_down)

screen.onkey(key="w", fun=l_paddle.go_up)
screen.onkey(key="s", fun=l_paddle.go_down)


game_is_on = True
while game_is_on:
    sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect the collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if (
        ball.distance(r_paddle) < 50
        and ball.xcor() > 320
        or ball.distance(l_paddle) < 50
        and ball.xcor() < -320
    ):
        ball.bounce_x()

    # Detect r paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
