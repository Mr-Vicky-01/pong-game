from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import Scoreboard
from draw_line import Line
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
line = Line()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
# screen.onkey(l_paddle.go_up, "w")
# screen.onkey(l_paddle.go_down, "s")

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Automate left paddle - make it follow the ball's y-coordinate
    if ball.xcor() < 0:
        l_paddle.follow_ball(ball.ycor())

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()

    if scoreboard.l_score == 1:
        line.clear_line()
        line.make_box()
        scoreboard.game_end()
        is_game_on = False


screen.exitonclick()
