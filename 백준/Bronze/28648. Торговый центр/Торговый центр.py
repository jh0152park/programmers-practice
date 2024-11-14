import sys


n = int(sys.stdin.readline().strip())

min_time = float("inf")
for _ in range(n):
    t, l = map(int, sys.stdin.readline().strip().split())
    min_time = min(min_time, t + l)

print(min_time)