import time
from turtle import Turtle, Screen
from ball import Ball
from paddle import Paddle
from brick import Brick
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)

ball = Ball()
paddle = Paddle((0, -15))
brick = Brick()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle.advance, "Right")
screen.onkey(paddle.retreat, "Left")

brick.setup()

game_is_on = Turtle
while game_is_on:

    ball.move()


    if ball.distance(paddle) < 50 and ball.ycor() == 0:
        ball.y_bounce()


    if ball.xcor() > 280 or ball.xcor() < -280:
        ball.x_bounce()


    if ball.ycor() > 280:
        ball.y_bounce()

    if ball.ycor() < -320:
        paddle.reset()
        ball.reset()
        time.sleep(2)
        ball.y_bounce()
        scoreboard.lives()
        if scoreboard.life == 0:
            scoreboard.lose()
            new_game = input("Restart?")
            if new_game == "yes":
                scoreboard.new_game()
                scoreboard.update_scoreboard()
                for blocks in brick.block:
                    blocks.color("black")
                brick.block.clear()
                brick.setup()



    for blocks in brick.block:
        if blocks.distance(ball) >= 35 and blocks.distance(ball) <= 36:
            ball.x_bounce()
            blocks.color("black")
            brick.block.remove(blocks)
        if blocks.distance(ball) <= 34:
            ball.y_bounce()
            blocks.color("black")
            brick.block.remove(blocks)

    if len(brick.block) == 0:
        scoreboard.win()
        brick.block.clear()
        if ball.counter % 2 == 0:
            ball.reset()
            paddle.reset()
            time.sleep(5)
            scoreboard.next_level()
            brick.setup()
            ball.y_bounce()
        else:
            ball.reset()
            paddle.reset()
            time.sleep(5)
            scoreboard.next_level()
            brick.setup()

screen.exitonclick()
