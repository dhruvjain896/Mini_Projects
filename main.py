import turtle

tim = turtle.Turtle()
screen = turtle.Screen()


def forwards():
    tim.forward(10)


def backwards():
    tim.backward(10)


def counter_clockwise():
    tim.setheading(tim.heading() + 10)


def clockwise():
    tim.setheading(tim.heading() - 10)


def clear_canvas():
    tim.reset()


screen.listen()
screen.onkeypress(key="w", fun=forwards)
screen.onkeypress(key="s", fun=backwards)
screen.onkeypress(key="a", fun=counter_clockwise)
screen.onkeypress(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear_canvas)

screen.exitonclick()
