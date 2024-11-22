import sys


n = int(sys.stdin.readline().strip())


min_x = float("inf")
max_x = float("-inf")
min_y = float("inf")
max_y = float("-inf")
for _ in range(n):
    x, y, = map(int, sys.stdin.readline().strip().split())

    min_x = min(min_x, x)
    max_x = max(max_x, x)
    min_y = min(min_y, y)
    max_y = max(max_y, y)

print((max_x - min_x) * (max_y - min_y))