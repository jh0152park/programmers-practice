import sys


n = int(sys.stdin.readline().strip())
for _ in range(n):
    x, y = map(int, sys.stdin.readline().strip().split())
    print((x * y) // 2)