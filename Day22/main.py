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
car_manager = CarManager()

game_is_on = True
while game_is_on:
    # Create cars.
    car_manager.create_car()
    # Move each car.
    car_manager.move_cars()

    screen.onkey(key="space", fun=player.move_forward)

    # Check if player crashed againts a car.
    for car in car_manager.car_list[:]:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Check if player is at the finish line.
    if player.check_finish() == True:
        # Updates de score and increases the speed of the cars.
        scoreboard.update_score()
        car_manager.level_up()

    time.sleep(0.1)
    screen.update()

screen.exitonclick()
