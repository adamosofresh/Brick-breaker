from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=.5, stretch_len=2.5)
        self.goto(position)

    def advance(self):
        self.penup()
        self.forward(35)

    def retreat(self):
        self.penup()
        self.backward(30)

    def reset(self):
        self.goto(0, -15)