from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.snake_body = []
        self.snakes = 3
        self.create_snake()
        self.head = self.snake_body[0]
        self.snakes = 3

    def create_snake(self):
        for position in POSITIONS:
            self.add_tail(position)

    def add_tail(self, position):
        snake = Turtle()
        snake.color("white")
        snake.shape("square")
        snake.speed("slowest")
        snake.shapesize(1)
        snake.penup()
        self.snake_body.append(snake)
        snake.goto(position)

    def extend_snake(self):
        self.add_tail(self.snake_body[-1].position())

    def move(self):
        for move in range(len(self.snake_body) - 1, 0, -1):
            x = self.snake_body[move - 1].xcor()
            y = self.snake_body[move - 1].ycor()
            self.snake_body[move].goto(x, y)
        self.head.forward(20)

    def go_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def go_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def go_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def go_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
