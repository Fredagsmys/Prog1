import turtle

def jump(t,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def spawn_turtle(x,y):
    t = turtle.Turtle()
    t.hideturtle()
    jump(t,x,y)
    return t

def rectangle(x, y, width, height, color):
    t = spawn_turtle(x, y)
    t.hideturtle()
    t.fillcolor(color)
    t.begin_fill()
    for dist in [width, height, width, height]:
        t.forward(dist)
        t.left(90)
    t.end_fill()
    
def tricolore(x, y, h):
    w = h/2  
    rectangle(x, y, w, h, 'blue')
    rectangle(x+w, y, w, h, 'white')
    rectangle(x+2*w, y, w, h, 'red')

def pentagram(x, y, side):
    t = spawn_turtle(x, y)
    t.hideturtle()
    t.setheading(270 - 36/2)
    t.color('yellow')
    t.begin_fill()
    for i in range(5):
        t.forward(side)
        t.left(180-36)
    t.end_fill()

def vienamese_flag(x, y, height):
    rectangle(x,y,height*1.5,height,'red')
    pentagram(x+height*0.75,y+height*0.75,height*0.4)

vienamese_flag(0,0,300)





