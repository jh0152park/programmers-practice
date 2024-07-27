def solution(numbers):
    numbers.sort()
    
    head = numbers[0] * numbers[1]
    tail = numbers[-1] * numbers[-2]
    
    return head if head > tail else tail