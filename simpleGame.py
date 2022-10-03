import turtle
import winsound
import random

Genshape = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(300, 800)
player = turtle.Turtle()
player.hideturtle()
player.color("red")
player.pencolor("black")
player.penup()
player_speed = 100
player.turtlesize(3)
player.shape("circle")
player.goto(0, -350)
player.direction = "none"
player.showturtle()


def moving_object(move):
    # to fill the color in ball
    move.fillcolor('orange')

    # start color filling
    move.begin_fill()

    # draw circle
    move.circle(20)

    # end color filling
    move.end_fill()

def generate_shapes():
    ran_shapes = ["circle", "square", "triangle", "turtle"]
    ran_color = ["yellow", "red", "blue", "pink", "yellow"]
    ran_pos = [0, 100, -100]
    Genshape.hideturtle()
    Genshape.penup()
    Genshape.color(ran_color[random.randint(0, 4)])
    Genshape.speed(0)
    Genshape.width(2)
    Genshape.shape(ran_shapes[random.randint(0, 3)])
    Genshape.setpos(ran_pos[random.randint(0,2)],350)
    Genshape.turtlesize(3)
    Genshape.pencolor("black")
    Genshape.showturtle()


def move_left():
    if player.xcor() == 100:
        winsound.Beep(200, 100)
        player.setx(0)
    elif player.xcor() == 0:
        winsound.Beep(200, 100)
        player.setx(-100)


def move_right():
    if player.xcor() == -100:
        player.setx(0)
        winsound.Beep(200, 100)
    elif player.xcor() == 0:
        winsound.Beep(200, 100)
        player.setx(100)

generate_shapes()
screen.listen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(generate_shapes, "g")

while True:
    Genshape.clear()
    screen.update()
    Genshape.sety(Genshape.ycor() - 60)
    if Genshape.ycor() < -352:
        generate_shapes()
turtle.done()

