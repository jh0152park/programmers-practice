import sys


x, n = map(int, sys.stdin.readline().strip().split())

for t in range(n):
    if x % 2:
        x = (x << 1) ^ 6
    else:
        x = (x >> 1) ^ 6

print(x)