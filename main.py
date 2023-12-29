from turtle import Screen, Turtle
from paddles import Paddle
from ball import Ball
from Scoreboard import Sb
import time

LENGTH = 1000
WIDTH = 630
GAME = True
MATCH = True
PADDLE_L_X = -490
PADDLE_R_X = 490
DISTANCE = 2

# Setting up the screen
plane = Screen()
plane.setup(1920, 1080)  # The dimensions of the screen
plane.bgcolor("black")
plane.title("Pong")
plane.tracer(0)

# setting up the boundary and the dotted line
boundary = Turtle()
boundary.ht()
boundary.color("white")
boundary.penup()
boundary.speed("fastest")
boundary.goto(-LENGTH / 2, -WIDTH / 2)
boundary.pendown()
for i in range(2):
    boundary.forward(LENGTH)
    boundary.left(90)
    boundary.forward(WIDTH)
    boundary.left(90)

# Setting up the dotted line in between
boundary.setheading(90)
boundary.goto(0, -WIDTH / 2)
boundary.speed("fastest")
for i in range(11):
    boundary.pendown()
    boundary.forward(30)
    boundary.penup()
    boundary.forward(30)

# setting up the title
boundary.goto(0, 320)
boundary.write("PONG", False, align="center", font=('Arial', 30, 'normal'))

# bringing the paddles into the picture
paddle_r = Paddle()
paddle_r.position(PADDLE_R_X)
paddle_l = Paddle()
paddle_l.position(PADDLE_L_X)

# making the paddles react to the keypress
plane.onkeypress(paddle_r.move_up, "Up")
plane.onkeypress(paddle_r.move_down, "Down")
plane.onkeypress(paddle_l.move_up, "w")
plane.onkeypress(paddle_l.move_down, "s")
plane.listen()

sb_l = Sb(-1)
sb_r = Sb(1)

while MATCH:
    # instantiating the ball
    ball = Ball()
    plane.update()
    time.sleep(2)
    while GAME:
        ball.forward(ball.dist)
        plane.update()

        # Ball collision with the walls
        ball_current_y = ball.pos()[1]
        ball_current_x = ball.pos()[0]
        if ball_current_y >= 304 or -304 >= ball_current_y:
            ball.on_collision(1)
        if ball_current_x >= 490 or -490 >= ball_current_x:
            ball.on_collision(0)
            GAME = False
            ball.ht()
        plane.update()

        # Hitting with the paddles
        ball_current_y = ball.pos()[1]
        ball_current_x = ball.pos()[0]
        if (15 <= abs(ball.pos()[0] - PADDLE_L_X) <= 20) and (
                abs(ball.pos()[1] - paddle_l.segments[2].pos()[1]) <= 50) or (
                15 <= abs(ball.pos()[0] - PADDLE_R_X) <= 20) and (
                abs(ball.pos()[1] - paddle_r.segments[2].pos()[1]) <= 50):
            ball.on_collision(0)
            ball.rallies += 1
            ball.increase_speed()
        plane.update()

    if ball.pos()[0] < 0:
        sb_r.score += 1
        sb_r.clear()
        sb_r.write(str(sb_r.score), align='center', font=('Arial', 50, 'normal'))
        GAME = True
    else:
        sb_l.score += 1
        sb_l.clear()
        sb_l.write(str(sb_l.score), align='center', font=('Arial', 50, 'normal'))
        GAME = True

    plane.update()

    if sb_r.score >= 5 or sb_l.score >= 5:
        MATCH = False
        time.sleep(1.5)
        plane.clear()
        plane.bgcolor("black")
        winner = Turtle()
        winner.ht()
        winner.color("white")
        winner.write("GAME OVER!!", align='center', font=('Arial', 50, 'normal'))
        time.sleep(1)
        winner.clear()
        if sb_r.score == 5:
            winner.write("RIGHT PLAYER WINS!", align='center', font=('Arial', 50, 'normal'))
        else:
            winner.write("LEFT PLAYER WINS!", align='center', font=('Arial', 50, 'normal'))

plane.exitonclick()
