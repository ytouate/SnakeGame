import turtle

from food import Food
import time
from turtle import Screen
from snake import Snake
from text import Text

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
RIGHT_LIMIT = 300
LEFT_LIMIT = -300
DOWN_LIMIT = 300
UP_LIMIT = -300
screen.listen()
screen.onkey(snake.go_up, "Up")
screen.onkey(snake.go_down, "Down")
screen.onkey(snake.go_right, "Right")
screen.onkey(snake.go_left, "Left")
text = Text()


def hit_wall():
    if snake.head.xcor() > RIGHT_LIMIT or snake.head.xcor() < LEFT_LIMIT or snake.head.ycor() < UP_LIMIT \
            or snake.head.ycor() > DOWN_LIMIT:
        return False
    else:
        return True


def collapse():
    for segment in snake.snake_body:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            return False
        else:
            return True


is_on = True
while is_on:
    screen.update()
    time.sleep(0.1)
    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10:
            is_on = False
            text.game_over()
            time.sleep(3)
    if food.distance(snake.head) < 15:
        food.move_food()
        text.increase_score()
        snake.extend_snake()
    if hit_wall():
        snake.move()
    else:
        is_on = False
        text.game_over()
        time.sleep(3)
