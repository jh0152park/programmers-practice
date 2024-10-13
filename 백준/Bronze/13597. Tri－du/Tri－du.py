import sys


n, m = map(int, sys.stdin.readline().strip().split())

if n == m:
    print(n)
else:
    print(max(n, m))