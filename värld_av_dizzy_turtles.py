#klas kollade UO1 UO2 UO3

import turtle
from random import randint
def jump(t,x,y):
    t.speed(0)
    t.penup()
    t.goto(x,y)
    t.pendown()

def spawn_turtle(x,y,color = 'black'):
    t = turtle.Turtle()
    t.color(color)
    jump(t,x,y)
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
    
size = 300

def move_random(t):
    h = t.heading()
    intervall = [h-45,h+45,0,25]
    t.fd(randint(intervall[2],intervall[3]))
    t.seth(randint(int(intervall[0]),int(intervall[1])))
    if t.xcor() < (-size) or  t.xcor() > size or t.ycor() < (-size) or t.ycor() > size:
        origo = t.towards(0,0)
        t.seth(origo)
def dizzy_turtles():
    
    rectangle(-size,-size,2*size,2*size,'lightblue')
    t1 = spawn_turtle(randint(-size,size),randint(-size,size),'green')
    t2= spawn_turtle(randint(-size,size),randint(-size,size),color ='red')
    counter = 0
    for i in range(500):
        
        move_random(t2)
        move_random(t1)
        if t1.distance(t2) < 100:
            t1.write('close')
            counter +=1
    print(counter, 'close calls')

def turtleworld():
    
    rectangle(-size,-size,2*size,2*size,'lightblue')
    spawn = 100
    tlist = [spawn_turtle(size - spawn,size-spawn),
             spawn_turtle(size - spawn,-size+spawn),
             spawn_turtle(-size + spawn,-size+spawn),
             spawn_turtle(-size + spawn,size-spawn)]
    
        
        
    while tlist[0].distance(tlist[1]) > 10:
        for t in tlist:
            t.fd(10)
        
        for i in range(4):
            j = (i + 1) % 4   
            tlist[i].setheading(tlist[i].towards(tlist[j]))

turtleworld()
        



