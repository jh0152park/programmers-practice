import sys


n, m = map(int, sys.stdin.readline().strip().split())

if n > 7:
    print(n - 7)
else:
    print(m + 7)