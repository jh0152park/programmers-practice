def solution(n, k):
    return [n for n in range(1, n+1) if n % k == 0]