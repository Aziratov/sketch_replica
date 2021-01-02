# Etch a Sketch

from turtle import Turtle, Screen

turtle_img = Turtle()
turtle_img.pensize(5)
turtle_img.shape("turtle")
screen = Screen()


def move_forward():
    turtle_img.forward(10)


def turn_right():
    heading = turtle_img.heading() - 10
    turtle_img.setheading(heading)


def turn_left():
    heading = turtle_img.heading() + 10
    turtle_img.setheading(heading)


def move_backwards():
    turtle_img.backward(10)


def board_clear():
    turtle_img.reset()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=board_clear)
screen.exitonclick()
