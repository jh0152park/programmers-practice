def solution(a, b):
    combi = int(str(a) + str(b))
    mul = 2 * a * b
    
    return combi if combi == mul else combi if combi > mul else mul