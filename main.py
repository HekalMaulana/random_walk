from turtle import Turtle, Screen
import random

my_t = Turtle()
screen = Screen()
direction = [0, 90, 180, 270]
colours = ['red', 'green', 'blue', 'yellow']

my_t.pensize(5)
my_t.speed("fast")

for _ in range(200):
    my_t.color(random.choice(colours))
    my_t.forward(20)
    my_t.setheading(random.choice(direction))


screen.exitonclick()