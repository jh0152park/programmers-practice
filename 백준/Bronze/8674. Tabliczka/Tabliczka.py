import sys


x, y = map(int, sys.stdin.readline().strip().split())


delta1 = ((x * y) - (x * (y // 2))) - (x * (y // 2))
delta2 = ((x * y) - (y * (x // 2))) - (y * (x // 2))

print(min(delta1, delta2))