from turtle import  Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")






game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detecting collision with food
    if snake.segments[0].distance(food) < 15:
        scoreboard.increase_score()
        food.refresh()
        snake.extend()
        scoreboard.refresh()

    #Detect collision with wall
    if snake.segments[0].xcor()>280 or snake.segments[0].xcor()<-280 or snake.segments[0].ycor()>280 or snake.segments[0].ycor()<-280:
       scoreboard.reset()
       snake.reset()


    #Detect collision with tail
    for segment in snake.segments[1:]:
        if segment == snake.segments[0]:
            pass
        elif snake.segments[0].distance(segment) < 10:
           scoreboard.reset()

























screen.exitonclick()