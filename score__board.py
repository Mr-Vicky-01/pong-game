from  turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("red")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-150, 200)
        self.write(self.l_score, align="center", font=("courier", 50, "bold"))
        self.goto(150, 200)
        self.write(self.r_score, align="center", font=("courier", 50, "bold"))

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()

    def game_end(self):
        self.goto(0, -50)
        self.color("green")
        self.write("AI WON 😎", align="center", font=("Giddyup Std", 75, "bold"))
