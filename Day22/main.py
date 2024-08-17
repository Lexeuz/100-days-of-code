import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    screen.onkey(key="w", fun=player.move_forward)
    player.check_finish()
    time.sleep(0.1)
    screen.update()
