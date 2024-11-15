import sys


a, b = map(int, sys.stdin.readline().strip().split())

x = (b + a) * a
x = (x + a) * a
print(x)