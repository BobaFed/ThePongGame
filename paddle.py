from turtle import Turtle


class Paddle(Turtle):
    
    def __init__(self, x):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x)

    def go_up(self):
        if self.ycor() > 220:
            pass
        else:
            new_y = self.ycor() + 40
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() < -220:
            pass
        else:
            new_y = self.ycor() - 40
            self.goto(self.xcor(), new_y)
