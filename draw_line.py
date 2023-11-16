from turtle import Turtle


class Line(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 300)
        self.make_line()

    def make_line(self, length=30, turn=90):
        self.right(turn)
        for n in range(length):
            self.pendown()
            self.fd(10)
            self.penup()
            self.fd(10)

    def make_box(self):
        self.goto(-280, 60)
        self.pendown()
        self.width(3)
        self.color("green")
        self.make_line(turn=270, length=27)
        self.make_line(turn=90, length=6)
        self.make_line(turn=90, length=27)
        self.make_line(turn=90, length=6)

    def clear_line(self):
        self.clear()
