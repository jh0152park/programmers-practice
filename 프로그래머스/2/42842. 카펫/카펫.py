def solution(brown, yellow):
    answer = []
    total = brown + yellow
    
    for x in range(2, total):
        if total % x == 0:
            y = total / x
            if ((x-2) * (y-2)) == yellow:
                return [y, x]                
