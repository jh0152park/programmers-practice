import sys


immun = 0
v1, j1 = map(int, sys.stdin.readline().strip().split())
v2, j2 = map(int, sys.stdin.readline().strip().split())
v, d, j = map(int, sys.stdin.readline().strip().split())

immun += v * d * j * v1 * j1
immun += v * d * j * v2 * j2
print(immun)