from turtle import Turtle, Screen
import heroes
import random

print(heroes.gen())

timmy = Turtle()
timmy.shape('turtle')
timmy.color("blue")
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


def draw_shape(num_sides):
    degrees = 360 / num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(degrees)


for sides in range(3, 11):
    timmy.color(random.choice(colors))
    draw_shape(sides)

screen = Screen()
screen.exitonclick()


