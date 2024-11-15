import sys


n, m = map(int, sys.stdin.readline().strip().split())

r = 0
b = 0
for _ in range(n):
    row = sys.stdin.readline().strip()
    r += row.count("0")
    b += row.count("1")

print(min(r, b))