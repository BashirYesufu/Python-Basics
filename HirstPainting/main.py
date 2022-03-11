import turtle as t
import heroes
import random

t.colormode(255)

timmy = t.Turtle()
timmy.shape('turtle')
timmy.pensize(20)
timmy.speed(20)
directions = [0, 90, 180, 270]


# Generate random colors using R G B
def get_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


for _ in range(200):
    timmy.color(get_random_color())
    timmy.forward(20)
    timmy.setheading(random.choice(directions))

screen = t.Screen()
screen.exitonclick()


