
import turtle
def jump(t,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    
def spawn_turtle(x,y):
    t = turtle.Turtle()
    t.goto(x,y)
    return t



def rectangle(x, y, width, height,color):
    t = turtle.Turtle()
    jump(t,x,y)
    form = [width, height, width, height]
    t.color(color)
    t.begin_fill()
    for i in form:
        t.forward(i)
        t.left(90)
        
    t.end_fill()

rectangle(400, -300, 300, 100, 'red')
