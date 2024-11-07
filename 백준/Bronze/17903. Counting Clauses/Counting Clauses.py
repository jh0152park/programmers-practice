import sys


n, m = map(int, sys.stdin.readline().strip().split())
for _ in range(n):
    sys.stdin.readline().strip()

if n >= 8:
    print("satisfactory")
else:
    print("unsatisfactory")