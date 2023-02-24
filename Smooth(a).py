def smooth(a):
    b = [a[0]]

    for i in range(1, len(a) - 1):
        b.append(sum(a[i - 1:i + 2]) / 3)
    b.append(a[-1])
    return b


def counter2(x, lista):
    sum = 0
    for i in lista:
        if type(i) != int:
            sum += i.count(x)
    return sum


def counter1(x, lista):
    sum = counter2(x, lista)
    for i in lista:
        if type(i) == int and i == x:
            sum += 1
    return sum


def counter(x, lista):
    res = 0
    for lst in lista:
        if type(lst) == list:
            res += lst.count(x)
        elif lst == x:
            res += 1
    return res


def extend(lista, x):
    for i in x:
        lista.append(i)
    return lista


list = [1, 2, 3]
x = [4, 5, 6]
#print(extend(list, x))


def remove_all(lista, x):
    for i in range(lista.count(x)):
        lista.remove(x)
    return lista


list2 = [3, 2, 4, 5, 3, 3, 2, 3]
nylista = [e for e in list2 if e != x]
#print(nylista)
print(list2)
print(smooth(list2))
