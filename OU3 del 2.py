import re
import keyword
infil = open('test3.py', 'r')
line = infil.readline()
freq = []
keywords = keyword.kwlist
unikaord = []
for i in range(1,16):
    print(i,'   ',line, end='')    
    freq.append(line)
    line = infil.readline()
    
infil.close()

list = []
for i in freq:
    wordlist = re.findall(r'[a-zA-ZåäöÅÄÖ]+', i)
    list.append(wordlist)
#list = lista med listor som element av varje rad
for c in list:
    for i in c:
        if i not in unikaord and i not in keywords:
            unikaord.append(i)
            
index = 0
radnummer = 1
radnum = []
for uord in unikaord:
    radnummer = 1
    radnum.append([])
    for rad in list:
        if rad.count(f'{uord}') > 0:
           radnum[index].append(radnummer)
        radnummer +=1
    index+=1
print()
print('referenslista:')
line_width = 30
for i in range(len(unikaord)):
    print(''.ljust(7),unikaord[i].ljust(line_width),radnum[i])



    
