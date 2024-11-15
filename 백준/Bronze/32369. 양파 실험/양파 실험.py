import sys


n, a, b = map(int, sys.stdin.readline().strip().split())
good = 1
bad = 1

for i in range(n):
    good += a
    bad += b

    if bad > good:
        bad, good = good, bad
    elif bad == good:
        bad -= 1

print(good, bad)