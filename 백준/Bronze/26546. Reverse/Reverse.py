import sys


n = int(sys.stdin.readline().strip())
for _ in range(n):
    s, i, j = map(str, sys.stdin.readline().strip().split())
    print(s[:int(i)] + s[int(j):])