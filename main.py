from turtle import Turtle, Screen
import random

my_t = Turtle()
screen = Screen()
direction = [0, 90, 180, 270]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    random_color = (r, g, b)
    return random_color

my_t.pensize(5)
my_t.speed("fast")
screen.colormode(255)

for _ in range(200):
    my_t.pencolor(random_color())
    print(random_color())
    my_t.forward(20)
    my_t.setheading(random.choice(direction))


screen.exitonclick()
