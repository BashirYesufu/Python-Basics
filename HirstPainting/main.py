import turtle as t
import random

t.colormode(255)

timmy = t.Turtle()


# Generate random colors using R G B
def get_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


timmy.speed(20)
while not timmy.heading() == 350:
    timmy.color(get_random_color())
    timmy.circle(100)
    current_heading = timmy.heading()
    timmy.setheading(current_heading + 10)

screen = t.Screen()
screen.exitonclick()


