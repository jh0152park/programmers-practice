import sys

n, m = map(int, sys.stdin.readline().strip().split())
bbang = [sys.stdin.readline().strip() for _ in range(n)]

for _ in range(n):
    sys.stdout.write(f"{bbang[_][::-1]}\n")