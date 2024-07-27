def solution(n, control):
    task = {
        "w": 1,
        "s": -1,
        "d": 10,
        "a": -10
    }
    
    for order in control:
        n += task[order]
    
    return n