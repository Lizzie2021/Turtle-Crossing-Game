import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()
screen.tracer(0)
screen.listen()
screen.onkey(player.move, "Up")
loop_count = 0
car_generate_gap = 6
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if loop_count % car_generate_gap == 0:
        car_manager.create_car()
    car_manager.move_cars(scoreboard.level)
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
    if player.is_at_finish_line():
        player.go_to_start()
        scoreboard.level_up()
        if car_generate_gap > 1:
            car_generate_gap -= 1
    loop_count += 1
screen.exitonclick()
