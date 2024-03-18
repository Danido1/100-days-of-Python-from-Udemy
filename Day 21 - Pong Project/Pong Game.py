from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((370, 0))
l_paddle = Paddle((-370, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.ball_move()

    # Detect collision with the ball
    if ball.ycor() == 290 or ball.ycor() == -290:
        ball.bounce_y()

    # Detect collision with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 345 or ball.distance(l_paddle) < 50 and ball.xcor() < -345:
        ball.bounce_x()
        print(ball.move_speed)
    # Detect when paddle misses
    if ball.xcor() > 375:
        scoreboard.r_point()
        scoreboard.update_scoreboard()
        ball.ball_reset()
    if ball.xcor() < -375:
        scoreboard.l_point()
        scoreboard.update_scoreboard()
        ball.ball_reset()

screen.exitonclick()

