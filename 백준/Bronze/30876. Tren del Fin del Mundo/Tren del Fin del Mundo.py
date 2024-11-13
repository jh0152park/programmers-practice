import sys


n = int(sys.stdin.readline().strip())

tx = 0
ty = float("inf")
for _ in range(n):
    x, y = map(int, sys.stdin.readline().strip().split())
    if y < ty:
        tx = x
        ty = y

print(tx, ty)