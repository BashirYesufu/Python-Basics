from turtle import Turtle, Screen
import heroes

print(heroes.gen())

timmy  = Turtle()
timmy.shape('turtle')
timmy.color("blue")
for _ in range(10):
    timmy.forward(10)
    timmy.color("white")
    timmy.forward(10)
    timmy.color("blue")


screen = Screen()
screen.exitonclick()


