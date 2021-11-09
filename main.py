from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from block_manager import BlockManager
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=800)
screen.title("Pong")
screen.tracer(0)

screen.listen()


def start_game():
    screen.resetscreen()
    paddle = Paddle((0, -350))
    manager = BlockManager()
    ball = Ball()

    screen.onkey(paddle.go_left, "Left")
    screen.onkey(paddle.go_right, "Right")

    game_is_on = True
    while game_is_on:
        screen.update()
        #time.sleep(0.0005)

        if ball.ycor() < -380:
            game_over = Turtle()
            game_over.penup()
            game_over.goto(0, -40)
            game_over.pendown()
            game_over.pencolor("white")
            game_over.hideturtle()
            game_over.write("GAME OVER!", font=("Arial", 11, "normal"), align="center")
            game_over.penup()
            game_over.goto(0, -60)
            game_over.pendown()
            game_over.write("Press 'Y' to play again", font=("Arial", 11, "normal"), align="center")

            game_is_on = False

            screen.update()
            screen.onkey(start_game, "y")

        ball.move()

        # Detect collision with obstacle
        if manager.check_hit(position=ball.position()):
            ball.bounce_y()

        # Detect collision with wall
        if ball.xcor() > 380 or ball.xcor() < -380:
            ball.bounce_x()
        if ball.ycor() > 380:
            ball.bounce_y()

        # Detect collision with paddle
        if ball.distance(paddle) < 100 and ball.ycor() < -320:
            ball.bounce_y()


start_game()

screen.exitonclick()
