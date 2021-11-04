from turtle import Turtle
ALIGNMENT = "left"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.goto(-280, 250)
        self.hideturtle()
        self.update_levelboard()

    def update_levelboard(self):
        self.write(arg=f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def increment_level(self):
        self.level += 1
        self.clear()
        self.update_levelboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=FONT)
