def twolist(a,b):
    if len(a) > len(b):
        n = len(a)
    elif len(b) > len(a):
        n = len(b)
    newlist = []
    for i in range(n):
        if i < len(b):
            newlist.append(b[i])
        if i < len(a):
            newlist.append(a[i])
    return newlist

def newtwolist(a,b):
    newlist = []
    for i in a:
        newlist.append(i)
    for x in b:
        newlist.append(x)
    return newlist

