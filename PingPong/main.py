from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Ping Pong")
screen.tracer(0)

paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350, 0)


def go_up():
    y_position = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), y_position)


def go_down():
    y_position = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), y_position)


game_is_on = True


while game_is_on:
    screen.update()

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

screen.exitonclick()
