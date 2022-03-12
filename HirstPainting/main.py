import random
import turtle as t

t.colormode(255)

timmy = t.Turtle()
timmy.speed('fastest')
timmy.hideturtle()

color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123),
              (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
              (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
              (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64),
              (107, 127, 153), (176, 192, 208), (168, 99, 102), (66, 64, 60), (219, 178, 183), (178, 198, 202),
              (112, 139, 141), (254, 194, 0)]

timmy.setheading(225)
timmy.penup()
timmy.forward(350)
timmy.setheading(0)


def go_forward():
    for _ in range(10):
        timmy.dot(20, random.choice(color_list))
        timmy.forward(50)
        timmy.dot(20, random.choice(color_list))
    timmy.setheading(90)
    timmy.forward(50)
    timmy.setheading(180)


def go_backwards():
    for _ in range(10):
        timmy.dot(20, random.choice(color_list))
        timmy.forward(50)
        timmy.dot(20, random.choice(color_list))
    timmy.setheading(90)
    timmy.forward(50)
    timmy.setheading(0)


for _ in range(5):
    go_forward()
    go_backwards()


screen = t.Screen()
screen.exitonclick()

