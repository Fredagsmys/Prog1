def smootha(a,n):
    r = []
    intervall = 2*n+1
    for i in range (len(a)):
        if i < n:
            r.append((sum(a[i:i+n+1])+(a[0]*(n-i))) / intervall)
        elif i >= len(a) - n:
            r.append((sum(a[i-n:i+1])+(a[len(a)-1]*(n+i-len(a)+1))) / intervall)
        else:
            r.append(sum(a[i-n:i+n+1]) / intervall)
    return r

def smoothb(a,n):
    r = []
    intervall = 2*n+1
    for i in range (len(a)):
        if i < n:
            r.append((sum(a[0:i+n+1])) / (intervall-(n-i)))
        elif i > len(a) - n-1:
            r.append((sum(a[i-n:i+1+n-len(a)+i+1])) / (intervall - (n-len(a)+i+1)))
        else:
            r.append(sum(a[i-n:i+n+1]) / intervall)
    return r

def round_list(a_list, ndigits):

    r = []
    for i in a_list:
        r.append(round(i,ndigits))

    return r 





list = [1, 2, 6, 4, 5, 0, 1, 2]

print(smootha(list,1))

print(smoothb(list,2))

print(round_list(smootha(list,1),4))
