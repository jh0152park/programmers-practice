def solution(array, commands):
    answer = []
    
    for f,t,i in commands:
        answer.append(sorted(array[f-1:t])[i-1])

    return answer