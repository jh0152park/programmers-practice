import sys


n = int(sys.stdin.readline().strip())
for _ in range(n):
    d, n, s, p = map(int, sys.stdin.readline().strip().split())

    if s * n > n * p + d:
        print("parallelize")
    elif s * n < n * p + d:
        print("do not parallelize")
    else:
        print("does not matter")