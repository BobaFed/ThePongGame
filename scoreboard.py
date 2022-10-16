from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, x):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(x)
        self.paivita_pisteet()
        

    def paivita_pisteet(self,):
        self.clear()
        self.write(f"{self.score}", align="center", font=("Courier", 50, "normal"))

    def lisaa_piste(self):
        self.score += 1
        self.paivita_pisteet()
