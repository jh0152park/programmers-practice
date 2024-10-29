import sys


d, h, m = map(int, sys.stdin.readline().strip().split())

dd = d - 11
dh = h - 11
dm = m - 11

dd *= 24 * 60
dh *= 60
dm += dd + dh

if dm < 0:
    print("-1")
else:
    print(dm)