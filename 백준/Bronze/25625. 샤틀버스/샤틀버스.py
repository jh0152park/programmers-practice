import sys


x, y = map(int, sys.stdin.readline().strip().split())

if x < y:
    print(y - x)
else:
    print(x + y)