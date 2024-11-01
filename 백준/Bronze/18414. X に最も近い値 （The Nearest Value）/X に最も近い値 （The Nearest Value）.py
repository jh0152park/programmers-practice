import sys


x, l, r = map(int, sys.stdin.readline().strip().split())

delta = float("inf")
target = 0
for n in range(l, r + 1):
    if abs(x - n) < delta:
        delta = abs(x - n)
        target = n

print(target)