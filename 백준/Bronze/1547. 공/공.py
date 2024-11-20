import sys


cup = [1, 0, 0]
n = int(sys.stdin.readline().strip())
for _ in range(n):
    x, y = map(int, sys.stdin.readline().strip().split())
    cup[x-1], cup[y-1] = cup[y-1], cup[x-1]

print(cup.index(1) + 1)