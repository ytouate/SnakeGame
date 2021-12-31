import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.shapesize(0.5)
        self.speed("fastest")

    def move_food(self):
        random_x = random.randint(-250, 250)
        random_y = random.randint(-250, 250)
        self.penup()
        self.goto(random_x, random_y)
