import math
def is_twin_prime (n):
    limit = int(math.sqrt(n) +1)
    for i in range(2,limit):
        if n%i == 0 or (n+2)%i == 0:
            return False
    return True

print(is_twin_prime(10))
