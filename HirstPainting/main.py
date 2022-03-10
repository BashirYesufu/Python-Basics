from turtle import Turtle, Screen
import heroes

print(heroes.gen())

timmy = Turtle()
timmy.shape('turtle')
timmy.color("blue")


def draw_shape(num_sides):
    degrees = 360 / num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(degrees)


sides = 3
for _ in range(8):
    draw_shape(sides)
    sides += 1

screen = Screen()
screen.exitonclick()


