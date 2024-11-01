import sys


tc = int(sys.stdin.readline().strip())

for _ in range(tc):
    n = int(sys.stdin.readline().strip())
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().strip().split())
        print(a + b, a * b)