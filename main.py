from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(fun=snake.move_up, key="Up")
screen.onkey(fun=snake.move_down, key="Down")
screen.onkey(fun=snake.move_left, key="Left")
screen.onkey(fun=snake.move_right, key="Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_forward()
    if snake.head.distance(food) < 12:
        food.refresh()
        snake.extend()
        scoreboard.score_counting()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        scoreboard.reset()
        food.refresh()
        snake.reset()
    for square in snake.snake_body[1:]:
        if snake.head.distance(square) < 8:
            scoreboard.reset()
            food.refresh()
            snake.reset()

screen.exitonclick()
