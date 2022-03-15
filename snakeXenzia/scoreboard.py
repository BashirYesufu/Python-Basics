from turtle import Turtle
# constants
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    # Write on scoreboard as score changes
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    # Print game over to the player once the game play is ended
    def end_game(self):
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER! 🐍", align=ALIGNMENT, font=FONT)

    # Adds a point to score
    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()
