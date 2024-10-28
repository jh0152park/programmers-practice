import sys


n = int(sys.stdin.readline().strip())

for _ in range(n):
    x, y = map(int, sys.stdin.readline().strip().split())
    for _ in range(y):
        print("X" * x)
    print("")