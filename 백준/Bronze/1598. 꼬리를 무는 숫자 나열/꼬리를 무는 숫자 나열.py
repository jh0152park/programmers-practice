import sys


a, b = map(int, sys.stdin.readline().strip().split())

ax = a // 4
ay = a % 4

if not a % 4:
    ax -= 1
    ay = 4

bx = b // 4
by = b % 4

if not b % 4:
    bx -= 1
    by = 4

print((max(ax, bx) - min(ax, bx)) + (max(ay, by) - min(ay, by)))