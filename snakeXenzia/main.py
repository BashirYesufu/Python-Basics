from turtle import Screen, Turtle
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Xenzia")
screen.tracer(0)

snake = Snake()
snake.create_snake()


game_is_on = True
while game_is_on:
    screen.update()

    snake.move()

screen.exitonclick()
