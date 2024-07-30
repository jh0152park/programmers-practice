import math

def solution(n):
    fact = []
    delta = []
    
    for i in range(1, 11):
        fact.append(math.factorial(i))

    for f in fact:
        if n - f >= 0:
            delta.append(n - f)
    
    return delta.index(min(delta)) + 1