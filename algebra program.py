import math
tal = 120
heltal=[tal]
for i in range(1, round(tal/2)+1):
    if tal % i == 0:
        heltal.append(i)
print(heltal)
print(len(heltal))