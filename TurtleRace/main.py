from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Place your bets", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

y_position = -100
for color in colors:
    timmy = Turtle(shape="turtle")
    timmy.color(color)
    timmy.penup()
    timmy.goto(x=-230, y=y_position)
    y_position += 50

screen.exitonclick()
