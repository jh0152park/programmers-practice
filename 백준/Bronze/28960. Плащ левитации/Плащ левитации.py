import sys


h, l, a, b = map(int, sys.stdin.readline().strip().split())

if (a <= l and b <= 2*h) or (b <= l and a <= 2*h):
    print("YES")
else:
    print("NO")