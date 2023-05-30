from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.y_move = 7
        self.x_move = 5
        self.speed(2)
        self.counter = 1


    def move(self):
        y_move = self.ycor() + self.y_move
        x_move = self.xcor() + self.x_move
        self.goto(x_move, y_move)


    def y_bounce(self):
        self.y_move *= -1
        self.counter += 1

    def x_bounce(self):
        self.x_move *= -1

    def reset(self):
        self.goto(0, 0)




