from turtle import Turtle, Screen
import heroes
import random

print(heroes.gen())

timmy = Turtle()
timmy.shape('turtle')
timmy.pensize(20)
timmy.speed(20)
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]


for _ in range(200):
    timmy.color(random.choice(colors))
    timmy.forward(20)
    timmy.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()


