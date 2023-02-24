import math
import os
import random
import re
import sys
results = [0,0]
a = [5,6,7]
b = [3,6,10]
for i in range(3):
    if a[i] > b[i]:
        results[0] += 1

    elif b[i] > a[i]:
        results[1] += 1

print(results)
