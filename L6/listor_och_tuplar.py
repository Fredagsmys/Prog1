
lista = [3,-12,4,5,87,-28]

def mean(list):
    return sum(list)/len(list)

def median(list):
    index = int(len(list)/2)
    #print(index)
    list = sorted(list)
    #print(list)
    if len(list) % 2 == 0:
        index1 = int(len(list)/2+0.5)
        return list[index1]
    return list[index]

def sumneg(list):
    sum = 0
    for i in list:
        if i < 0:
            sum += i
    return sum



def delneg(list):
    newlist= []
    for i in list:
        if i > 0:
            newlist.append(i)
    return newlist

def between(list, low, high):
    newlist = []
    for i in list:
        if i > low and i < high:
            newlist.append(i)
    return newlist

       
def main():
    print(between(lista,0,50))
    print(sumneg(lista))
    print(mean(lista))
    print(median(lista))

main()
        

    
