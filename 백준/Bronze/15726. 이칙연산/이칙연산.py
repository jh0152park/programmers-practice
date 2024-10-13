import sys

a, b, c = map(int, sys.stdin.readline().strip().split())

n = int(a * b / c)
m = int(a / b * c)

print(max(n, m))