def solution(arr):
    return [n // 2 if n >= 50 and n % 2 == 0 else n * 2 if n < 50 and n % 2 == 1 else n for n in arr]