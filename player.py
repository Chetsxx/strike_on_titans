from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('gif/giphy.gif')
        self.penup()
        self.goto(0, -250)

    def move_right(self):
        self.forward(10)

    def move_left(self):
        self.backward(10)


class Attack(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.shape('gif/duster.gif')
        self.setpos(x, y)
