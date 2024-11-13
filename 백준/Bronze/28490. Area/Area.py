import sys


max_mul = 0
n = int(sys.stdin.readline().strip())
for _ in range(n):
    h, w = map(int, sys.stdin.readline().strip().split())
    max_mul = max(max_mul, h * w)

print(max_mul)