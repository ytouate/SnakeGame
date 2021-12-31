from turtle import Turtle

FONT = ("Arial", 10, "bold")
ALIGN = "center"


class Text(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = -1
        self.speed("fastest")
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.update_score()

    def update_score(self):
        self.write(f"score: {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(-80, -20)
        self.write("GAME OVER", font=("Arial", 20, "bold"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
