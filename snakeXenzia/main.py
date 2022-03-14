from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Xenzia")
screen.tracer(0)

x_axis = 0
y_axis = 0
snake_body = []

for _ in range(3):
    new_segment = Turtle("square")
    new_segment.penup()
    new_segment.color("white")
    new_segment.goto(x=x_axis, y=y_axis)
    x_axis -= 20
    snake_body.append(new_segment)

game_is_on = True
while game_is_on:
    screen.update()
    for segment in snake_body:
        segment.forward(20)

screen.exitonclick()