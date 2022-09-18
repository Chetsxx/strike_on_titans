from turtle import Turtle
import random
class Titan:
    def __init__(self):
        self.all_titans = []
        self.head = None
        self.bottom = None
        self.x = -250

    def create_titan(self):
        for t in range(8):
            titan = Turtle()
            titan.penup()
            titan.shape('gif/titan.gif')
            titan.goto(self.x, 230)
            self.x += 50
            self.all_titans.append(titan)
        self.head = self.all_titans[0]
        self.bottom = self.all_titans[-1]


    def move_back(self):
        for t in self.all_titans:
            t.setheading(180)

    def move_front(self):
        for t in self.all_titans:
            t.setheading(0)

    def move(self):
        for t in self.all_titans:
            t.forward(10)


class TitanAttack:
    def __init__(self):
        self.all_rock = []

    def create_rock(self):
        random_chance = random.randint(1, 20)
        if random_chance == 6:
            rock = Turtle()
            rock.penup()
            rock.setheading(270)
            rock.shape("gif/rock.gif")
            rock.goto(random.randint(-250, 250), 230)
            self.all_rock.append(rock)

    def move_rock(self):
        for r in self.all_rock:
            r.forward(10)

