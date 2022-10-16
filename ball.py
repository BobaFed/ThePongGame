from turtle import Turtle


class Pallo(Turtle):

    def __init__(self):
        super().__init__()
        self.color("deep pink")
        self.shape("circle")
        self.penup()
        self.goherex = 10
        self.goherey = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.goherex
        new_y = self.ycor() + self.goherey
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.goherey *= -1

    def bounce_x(self):
        self.goherex *= -1
        self.move_speed *= 0.9

    def huti(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
