from turtle import Turtle
import random


color = ["red", "blue", "green", "purple", "yellow"]
x_loc = []
for x_num in range(-279, 279, 46):
    x_loc.append(x_num)

y_loc = []
for y_num in range(140, 280, 26):
    y_loc.append(y_num)


class Brick():
    def __init__(self):
        self.block = []

    def setup(self):
        for x in x_loc:
            for i in range(0, random.randint(1, 5)):
                blocks = Turtle("square")
                blocks.penup()
                blocks.color(random.choice(color))
                blocks.shapesize(stretch_wid=1, stretch_len=2)
                blocks.goto(x=x, y=y_loc[i])
                self.block.append(blocks)







