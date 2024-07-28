def is_odd(num):
    return num % 2

def solution(a, b):
    answer = 0
    
    if is_odd(a) and is_odd(b):
        return a ** 2 + b ** 2
    
    if not is_odd(a) and not is_odd(b):
        return abs(a - b)
    
    return (a + b) * 2