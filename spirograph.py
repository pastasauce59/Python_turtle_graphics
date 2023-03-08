import turtle as t
import random

spiro = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = r = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r,g,b)
    return random_color

def make_spirograph():
    spiro.speed(0)
    for _ in range(75):
        spiro.color(random_color())
        spiro.circle(120)
        spiro.left(5)

make_spirograph()



screen = t.Screen()
screen.exitonclick()