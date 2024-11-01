import sys


n = int(sys.stdin.readline().strip())
for _ in range(n):
    mul, sign = map(str, sys.stdin.readline().strip().split())
    print(sign * int(mul))