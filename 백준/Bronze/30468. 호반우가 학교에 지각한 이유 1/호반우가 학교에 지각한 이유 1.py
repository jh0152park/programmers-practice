import sys


s, d, i, l, n = map(int, sys.stdin.readline().strip().split())

avg = (s + d + i + l) / 4
bless = 0

while avg < n:
    bless += 1
    avg = (s + d + i + l + bless) / 4

print(bless)