import math

def triangle_area(a, b, c):
        s = (a + b + c)/2
        t = s*(s-a)*(s-b)*(s-c)
        r = math.sqrt(t)
        return r
def errmess():
        print('\n*** invalid input.')
        print('try again')   
    
def input():
        a = float(input('input side a: '))
        b = float(input('input side b: '))
        c = float(input('input side c: '))
        return a,b,c



while True:
        input(a,b,c)
        try:
                if triangle_area(a,b,c) == 0:
                    print('area cant be 0')
                else:
                    print ('area= ', triangle_area(a,b,c),)
                    break
        except ValueError:
                    errmess()
        
            
            

