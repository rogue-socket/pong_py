from turtle import Turtle


class Paddle:
    width = 20

    def __init__(self):
        self.starting_x = 0
        self.starting_y = 0
        self.segments = []
        self.create_paddle()

    def create_paddle(self):
        for i in range(2, -3, -1):
            tim = Turtle(shape="square")
            tim.color("white")
            tim.penup()
            tim.goto(0, 0 + i * self.width)
            self.segments.append(tim)

    def position(self, x):
        for elem in self.segments:
            y = elem.pos()[1]
            elem.goto(x, y)

    def move_up(self):
        # Limits on the movement of the paddle
        if self.segments[0].pos()[1] >= 280:
            pass
        else:
            for elem in self.segments:
                elem.setheading(90)
                elem.forward(25)

    def move_down(self):
        # Limits on the movement of the paddle
        if self.segments[-1].pos()[1] <= -280:
            pass
        else:
            for elem in self.segments:
                elem.setheading(270)
                elem.forward(25)
