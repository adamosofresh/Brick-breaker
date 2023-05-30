from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.life = 3
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-230, -280)
        self.write(f"LEVEL {self.level}", align="center", font=("Courier", 20, "normal"))
        self.goto(230, -280)
        self.write(f"LIVES {self.life}", align="center", font=("Courier", 20, "normal"))


    def next_level(self):
        self.level += 1
        self.update_scoreboard()

    def win(self):
        self.goto(0, 100)
        self.write(f"YOU WIN!\nGET READY FOR LEVEL {self.level+1}!", align="center", font=("Courier", 20, "normal"))

    def lose(self):
        self.goto(0, 100)
        self.write("YOU LOSE!", align="center", font=("Courier", 20, "normal"))


    def lives(self):
        self.life -= 1
        self.update_scoreboard()

    def new_game(self):
        self.life = 3
        self.update_scoreboard()
