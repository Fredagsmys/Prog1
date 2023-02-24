from random import randint
import turtle
def random_turtle(side = 500):
    t = turtle.Turtle()
    randint(0,499)
    t.goto(randint(-side*0.5,side*0.5),randint(-side*0.5,side*0.5))
    t.setheading(randint(0,359))
random_turtle()
    
    
