import sys


n, w, h, l = map(int, sys.stdin.readline().strip().split())
limit = (w // l) * (h // l)

if limit > n:
    print(n)
else:
    print(limit)