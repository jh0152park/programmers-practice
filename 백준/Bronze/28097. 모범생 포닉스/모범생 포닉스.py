import sys


n = int(sys.stdin.readline().strip())
schedule = list(map(int, sys.stdin.readline().strip().split()))

total_time = sum(schedule) + ((n - 1) * 8)
d = total_time // 24
h = total_time % 24

print(d, h)