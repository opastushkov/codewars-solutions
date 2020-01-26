from math import log

def zeros(n):
    if not n: return 0
    k = int(log(n, 5))
    return sum([n//5**x for x in range(1, k + 1)])
    
    