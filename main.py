import time
from food import Food
from Snake import Snake
from turtle import Screen
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("Black")
screen.title("Snakes Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game = True
while game:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.segment[0].distance(food) < 15 :
        score.score()
        snake.grow()
        food.refresh()

    if snake.segment[0].xcor() > 280 or snake.segment[0].xcor() < -280 or snake.segment[0].ycor() > 280 or snake.segment[0].ycor() < -280:
        game = False
        score.game_over()

    for segment in snake.segment[1:]:
        if snake.segment[0].distance(segment) < 10:
            game = False
            score.game_over()

screen.exitonclick()
