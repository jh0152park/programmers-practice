def get_div(n):
    cnt = 1
    for i in range(2, n + 1):
        if not n % i:   cnt += 1
    return cnt

def solution(n):
    return sum([1 for i in range(1, n + 1) if get_div(i) >= 3])