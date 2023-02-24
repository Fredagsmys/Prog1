import turtle

'''
class snake:
    def __init__(self):
        self.var = []
    def __Str__(self):
        pass
    def jump(self,t,x,y):
        t.penup()
        t.goto(x,y)
        t.pendown()
        return t
    def summon_turtle(self,t,x,y):
        t = turtle.Turtle()
        self.s = snake().jump(t,x,y)
        return self.s
    
        




def main():
    list = ('t','y','u')
    list2 = (0,100,200)
    for i in list:
        snake().summon_turtle(i,list2[clock],list2[clock])
        clock +=1
    
main()
'''
import random as r

'''
while True:
    print(f'dice number: {r.randint(1,6)}')
    inputt = input('wanna go again? (enter or ´stop`) ')
    if inputt == 'stop':
        break
'''
'''
score = 0
def game():
    global score
    intervall = (1,5)
    number = r.randint(intervall[0],intervall[1])
    print(f'number is between {intervall[0]} and {intervall[1]}')
    guess = int(input('guess the number: '))
    while True:
        if guess == number:
            guess = print('correct guess!')
            score+=10
            print()
            break
        elif guess < number:
            guess = int(input('guess higher: '))
            score -=5
        elif guess >number:
            guess = int(input('guess lower: '))
            score -=5


for i in range(4):
    print(f'current score: {score}')
    game()
    
print(f'final score: {score}')

'''


def guessing_game_2():
    intervall = [1, 100]
    guess = intervall[1] / 2
    counter = 10
    counter2 = 0
    while True:

        print(guess)
        hol = input('higher or lower or correct? (h/l(c) ')

        if hol == 'l':
            guess = r.randint(guess - counter, guess)
            counter2 += 1
        elif hol == 'h':
            guess = r.randint(guess, guess + counter)
            counter2 += 1
        elif hol == 'c':
            break
        if counter > 2:
            counter -= 2
    print(f'it took me {counter2} tries ot guess your number')


guessing_game_2()
