import sys


n = int(sys.stdin.readline().strip())

for _ in range(n):
    i, f = map(int, sys.stdin.readline().strip().split())
    if (i <= 1 and f <= 2) or (i <= 2 and f <= 1):
        print("Yes")
    else:
        print("No")