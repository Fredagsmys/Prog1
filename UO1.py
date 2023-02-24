
import turtle
def jump(t,x,y):
    t.hideturtle()
    t.penup()
    t.goto(x,y)
    t.pendown()
    
def spawn_turtle(x, y,visible=''):
    t = turtle.Turtle()
    jump(t, x, y)
    return t



def rectangle(x, y, width, height, color):
    t = spawn_turtle(x, y)
    t.speed(0)
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

        
def pentagram(x, y, side,color):
    t = spawn_turtle(x, y)
    t.speed(0)
    t.hideturtle()
    t.color(color)
    t.begin_fill()
    t.setheading(270 - 36/2)
    for i in range(5):
        t.forward(side)
        t.left(144)
    t.end_fill()
    
def flag(x,y,h):    
    tricolore(x, y, h)
    turtle.update()
    for p in [y*1.25,y*(-1.5)]:  
        for i in range (5):
            pentagram(i*h*0.5 + (x-h*0.33),p,h*0.2,'green')

flag(-300,-50 ,100)
