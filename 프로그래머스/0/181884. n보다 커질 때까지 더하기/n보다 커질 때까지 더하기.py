def solution(numbers, n):
    answer = 0
    
    for num in numbers:
        if answer > n: break
        answer += num
    
    return answer