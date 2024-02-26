from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from turtle import Screen, Turtle
import time

MOVE_TIME = 0.1

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

pen = Turtle(shape="arrow")
pen.hideturtle()
pen.speed(0)


def draw_line(start_x, start_y, end_x, end_y):
    pen.pencolor("white")
    pen.penup()
    pen.goto(start_x, start_y)
    pen.pendown()
    pen.goto(end_x, end_y)
    pen.penup()


draw_line(-290, 290, -290, -290)
draw_line(-290, -290, 290, -290)
draw_line(290, -290, 290, 290)
draw_line(290, 290, -290, 290)


snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.head_left, "Left")
screen.onkey(snake.head_right, "Right")

play_again = True
while play_again:
    play = True
    while play:
        screen.update()
        time.sleep(MOVE_TIME)
        snake.move()

        if snake.head.distance(food) < 10:
            food.refresh()
            scoreboard.increase_score()
            snake.add_segment()
            print("nom")

        if snake.head.xcor() > 290 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            scoreboard.game_over()
            play = False

        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 5:
                scoreboard.game_over()
                play = False

    screen.exitonclick()
    again = input("Would you like to play again? Type 'y' for yes or 'n' for no.").lower()
    if again == "y":
        play_again = True
    else:
        play_again = False
