from turtle import Turtle


class Kartta(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(270)
        self.color("grey")
        self.goto(0,300)
        self.hideturtle()
        self.areenamid()
        self.areenatop()
        self.areenabot()
        

        

    def areenamid(self):
        for _ in range(16):
            self.pendown()
            self.forward(19)
            self.penup()
            self.forward(19)

    def areenatop(self):
        self.goto(-370, 300)
        self.setheading(0)
        self.pendown()
        self.goto(370, 300)
        self.penup()

    def areenabot(self):
        self.goto(-370,-300)
        self.pendown()
        self.goto(370, -300)
        self.penup()