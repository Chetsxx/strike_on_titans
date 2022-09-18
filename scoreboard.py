from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", False, align="center", font=("Arial", 12, "bold"))

    def update_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()
        print(self.score)

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER!!!\n Final Score: {self.score}", False, align="center", font=("Arial", 16, "normal"))
