def solution(n):
    if n % 2:
        return sum([i for i in range(n + 1) if i % 2])
    return sum([i**2 for i in range(n + 1) if not i % 2])