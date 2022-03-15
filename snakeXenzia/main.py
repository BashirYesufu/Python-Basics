from turtle import Screen, Turtle
from snake import Snake
import time
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Xenzia")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

def end_game():
    global  game_is_on
    game_is_on = False
    scoreboard.end_game()

while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    # Detect food collision
    if snake.head.distance(food) < 15:
        food.move()
        scoreboard.increase_score()
        snake.add_snake_part()

    # Detect wall collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        end_game()

    # Detect tail collision
    for part in snake.snake_body:
        if part == snake.head:
            pass
        elif snake.head.distance(part) < 10:
            end_game()

screen.exitonclick()
