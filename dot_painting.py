from extract import rpg_color as rpg_col
import turtle, random

tom = turtle.Turtle()
turtle.colormode(255)


def ran_color(l):
    color = random.choice(l)
    return color


def add_point():
    tom.pendown()
    tom.dot(20, ran_color(rpg_col))
    tom.penup()
    tom.forward(50)
    tom.pendown()


def start():
    tom.right(90)
    tom.penup()
    tom.forward(50)
    tom.right(90)
    tom.forward(50)
    tom.pendown()


def end():
    tom.left(90)
    tom.penup()
    tom.forward(50)
    tom.left(90)
    tom.forward(50)
    tom.pendown()


i = 0
while i < 10:
    if i != 0:
        if i % 2 == 0:
            print("start")
            start()
        elif i % 2 != 0:
            print("end")
            end()
    else:
        tom.setheading(225)
        tom.penup()
        tom.forward(100)
        tom.pendown()
        tom.setheading(0)
    j = 0
    while j < 10 :
        add_point()
        j += 1
    i += 1

# while j < 3:
#     i=0
#     while i < 2:
#         tom.forward(20)
#         tom.penup()
#         tom.forward(50)
#         tom.pendown()
#         i += 1
#     tom.left(90)
#     tom.forward(10)
#     tom.left(90)
#     j += 1

screen = turtle.Screen()
screen.exitonclick()
