from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.dist = 2
        self.penup()
        self.speed("fast")
        self.color("white")
        p = random.randint(130, 245)
        self.setheading(p)
        self.rallies = 1
        self.buffer_rallies = 0

    def on_collision(self, wall):
        p = self.heading()
        if wall == 1:
            #top and bottom wall
            self.setheading(360 - p)
        else:
            #left and right wall
            self.setheading((180 - p) % 360)

    def increase_speed(self):
        if self.rallies % 4 == self.buffer_rallies:
            self.buffer_rallies = (self.buffer_rallies + 3) % 4
            self.dist = self.dist + 1
        else:
            self.dist = self.dist
