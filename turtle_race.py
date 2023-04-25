import turtle
from turtle import Turtle, Screen
import random

# tim = Turtle(shape="turtle")
# tim.penup()
screen = Screen()
screen.setup(width=500, height=400)
user_bet= screen.textinput(title="make your bet", prompt="who will win and enter its a color?")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y = -90
n_turtle = []
for i in range(6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[i])
    tim.goto(-240, y)
    y += 30
    n_turtle.append(tim)

is_race = False
if user_bet:
    is_race=True


while is_race:
    for i in n_turtle:
        if i.xcor() >= 230:
            is_race = False
            col = i.pencolor()
        dist = random.randint(0, 10)
        i.forward(dist)

if col == user_bet:
    print("you win")
else:
    print(f"you loose the winner is {col}")



screen.exitonclick()
