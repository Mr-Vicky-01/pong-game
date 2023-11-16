from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def follow_ball(self, ball_y):
        if self.ycor() < ball_y:
            self.go_up()
        elif self.ycor() > ball_y:
            self.go_down()

    def go_up(self):
        if self.ycor() + 20 < 280:
            new_y = self.ycor() + 20
            self.goto(x=self.xcor(), y=new_y)

    def go_down(self):
        if self.ycor() - 20 > -280:
            new_y = self.ycor() - 20
            self.goto(x=self.xcor(), y=new_y)
