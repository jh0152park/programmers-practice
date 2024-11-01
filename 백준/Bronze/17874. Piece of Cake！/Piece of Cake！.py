import sys


cake = []
n, h, v = map(int, sys.stdin.readline().strip().split())

cake.append(h * v * 4)
cake.append(h * (n - v) * 4)
cake.append((n - h) * v * 4)
cake.append((n - h) * (n - v) * 4)

print(max(cake))