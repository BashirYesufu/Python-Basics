from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    # Create a fresh snake
    def create_snake(self):
        for _ in range(3):
            x_axis = 0
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(x=x_axis, y=0)
            x_axis -= 20
            self.snake_body.append(new_segment)

    # Add a part to increase the snake
    def add_snake_part(self):
        x_axis = self.snake_body[-1].xcor()
        y_axis = self.snake_body[-1].ycor()
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(x=x_axis, y=y_axis)
        self.snake_body.append(new_segment)

    def reset(self):
        for part in self.snake_body:
            part.goto(1000, 1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]

    # Move snake till game ends
    def move(self):
        for segment_number in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[segment_number - 1].xcor()
            new_y = self.snake_body[segment_number - 1].ycor()
            self.snake_body[segment_number].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # Turn the snake upwards
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    # Turn the snake downwards
    def down(self):
        if not self.head.heading() == UP:
            self.head.setheading(DOWN)

    # Turn the snake left
    def left(self):
        if not self.head.heading() == RIGHT:
            self.head.setheading(LEFT)

    # Turn the snake right
    def right(self):
        if not self.head.heading() == LEFT:
            self.head.setheading(RIGHT)
