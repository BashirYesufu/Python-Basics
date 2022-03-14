from turtle import Turtle


class Snake:
    def __init__(self):
        self.x_axis = 0
        self.snake_body = []
        self.create_snake()
        self.move()

    def create_snake(self):
        for _ in range(3):
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(x=self.x_axis, y=0)
            self.x_axis -= 20
            self.snake_body.append(new_segment)

    def move(self):
        for segment_number in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[segment_number - 1].xcor()
            new_y = self.snake_body[segment_number - 1].ycor()
            self.snake_body[segment_number].goto(new_x, new_y)
        self.snake_body[0].forward(20)
