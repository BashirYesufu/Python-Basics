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


def draw_circle(gap_size):
    for _ in range(int(350 / gap_size)):
        timmy.color(get_random_color())
        timmy.circle(100)
        current_heading = timmy.heading()
        timmy.setheading(current_heading + gap_size)


draw_circle(5)
screen = t.Screen()
screen.exitonclick()


