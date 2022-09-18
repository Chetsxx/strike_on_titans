from turtle import Screen
from player import Player, Attack
from titan import Titan, TitanAttack
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(700, 600)
screen.bgcolor("black")
screen.title("Attack on Titans")
screen.tracer(0)
screen.register_shape('gif/giphy.gif')
screen.register_shape('gif/duster.gif')
screen.register_shape('gif/titan.gif')
screen.register_shape('gif/rock.gif')
player = Player()
titan = Titan()
titan_attack = TitanAttack()
titan.create_titan()
scoreboard = ScoreBoard()
atk = Attack(player.xcor(), player.ycor())
game_on = True

def shoot():
    global shooting
    atk.setpos(player.xcor(), player.ycor())
    atk.showturtle()
    atk.setheading(90)
    shooting = True

def was_hit():
    for t in titan.all_titans:
        if atk.distance(t) < 15:
            t.hideturtle()
            t.setpos(x=-290, y=230)
            atk.hideturtle()
            return True

def attack_hit():
    for r in titan_attack.all_rock:
        if r.distance(player) < 15:
            scoreboard.game_over()
            return True


screen.listen()
screen.onkeypress(player.move_right, "Right")
screen.onkeypress(player.move_left, "Left")
screen.onkeypress(shoot, "Up")


shooting = False

while game_on:
    time.sleep(0.1)
    screen.update()
    titan.move()
    titan_attack.create_rock()
    titan_attack.move_rock()

    if shooting:
        atk.forward(10)

    if titan.bottom.xcor() > 300:
        titan.move_back()
    if titan.head.xcor() < - 300:
        titan.move_front()

    if was_hit():
        scoreboard.update_score()

    if scoreboard.score == len(titan.all_titans):
        scoreboard.game_over()
        game_on = False

    if attack_hit():
        game_on = False






screen.exitonclick()