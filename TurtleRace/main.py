from turtle import Turtle, Screen
import random

keep_racing = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Place your bets", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

y_position = -70
for color in colors:
    new_turtle = Turtle(shape="car")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position)
    y_position += 30
    turtles.append(new_turtle)

if user_bet:
    keep_racing = True

while keep_racing:
    for turtle in turtles:
        distance = random.randint(0, 10)
        turtle.forward(distance)


screen.exitonclick()
