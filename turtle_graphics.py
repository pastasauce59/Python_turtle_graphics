# from turtle import Turtle, Screen
import turtle as t
import random

colors = ['red', 'yellow', 'green', 'blue', 'purple', 'orange', 'skyblue']
directions = ['left', 'right']
tim = t.Turtle()
t.colormode(255)
tim.shape('turtle')
tim.color('skyblue')

def random_color():
    r = random.randint(0, 255)
    g = r = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color =  (r,g,b)
    return random_color

def draw_square():
    rc = random.choice(range(255))
    tim.pencolor((rc,rc,rc))
    for _ in range(4):
        tim.forward(100)
        tim.right(90)

def dashed_line():
    for _ in range(15):
        tim.forward(5)
        tim.pu()
        tim.forward(5)
        tim.pd()

def draw_pentagon():
    degrees = 360 / 5
    for _ in range(5):
        tim.forward(100)
        tim.right(degrees)

def draw_hexagon():
    degrees = 360 / 6
    for _ in range(6):
        tim.forward(100)
        tim.right(degrees)

def draw_heptagon():
    degrees = 360 / 7
    for _ in range(7):
        tim.forward(100)
        tim.right(degrees)

def draw_octogon():
    degrees = 360 / 8
    for _ in range(8):
        tim.forward(100)
        tim.right(degrees)

def draw_nonagon():
    degrees = 360 / 9
    for _ in range(9):
        tim.forward(100)
        tim.right(degrees)

def draw_decagon():
    degrees = 360 / 10
    for _ in range(10):
        tim.forward(100)
        tim.right(degrees)

def draw_shape(num_sides):
    angles = 360 / num_sides

    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angles)

# dashed_line()
# draw_square()
# draw_pentagon()
# draw_hexagon()
# draw_heptagon()
# draw_octogon()
# draw_nonagon()
# draw_decagon()

# draw_shape(3)


#Draw All Shapes
# n = 3
# while n <= 10:
#     tim.color(random.choice(colors))
#     draw_shape(n)
#     n += 1

#Random Walk
def random_walk():
    tim.speed(10)
    tim.pensize(15)
    directions = [0, 90, 180, 270]
    for walk in range(200):
        tim.color(random_color())
        tim.forward(30)
        tim.setheading(random.choice(directions))

random_walk()
        
        





import heroes
print(heroes.gen())


screen = t.Screen()
screen.exitonclick()