def solution(n):
    return sum([i for i in list(range(2, n+1)) if i % 2 == 0])