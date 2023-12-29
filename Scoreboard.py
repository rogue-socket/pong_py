from turtle import Turtle


class Sb(Turtle):

    def __init__(self, x):
        super().__init__()
        self.score = 0
        self.ht()
        self.penup()
        self.color("white")
        self.goto(x*100, 200)
        self.write(str(self.score), align='center', font=('Arial', 50, 'normal'))
