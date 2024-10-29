import sys


x_pos = list(map(int, sys.stdin.readline().strip().split()))
x, _, _ = map(int, sys.stdin.readline().strip().split())

if x in x_pos:
    print(x_pos.index(x) + 1)
else:
    print("0")