import random
import turtle
'''
class Dice:
    def __init__(self, sides):
        self.sides = sides
        self.value = random.randint(1, self.sides)
				
    def __str__(self):
        return f'Sidor: {self.sides:2d}, värde: {self.value:2d}'    

    def roll(self):
        self.value = random.randint(1, self.sides)    


d1 = Dice(6)
d2 = Dice(12)

for i in range(5):
    d1.roll()
    d2.roll()
    print(f'{d1.value:2d}, {d2.value:2d}')


class PokerDice:

    def __init__(self,number_of_dices):
        self.dice_list = [Dice(6) for i in range(number_of_dices)]

    def __str__(self):
        res = []
        for d in self.dice_list:
            res.append(d.value)
        return str(sorted(res))

        
    def roll(self):
        for d in self.dice_list:
            d.roll()      # Använder rollmetoden i Dice

    def number_of_dice(self):
        return len(self.dice_list)
        
print('Pokertärningar:') 
pd = PokerDice(10)
for i in range(10):
    pd.roll()
    print(pd)
print(pd.number_of_dice())

'''
class Rectangle:
    def __init__(self,width, height,x,y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    def __str__(self):
        return str((self.height * self.width))

    def draw(self):
        format = [self.width,self.height,self.width,self.height]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.setpos(self.x,self.y)
        t.pendown()
        for i in format:
            t.fd(i)
            t.left(90)
            

Rec = Rectangle(200,200,-500,300)
print(Rec)
Rec.draw()














