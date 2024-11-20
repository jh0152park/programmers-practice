import sys


x, y, w, h = map(int, sys.stdin.readline().strip().split())

print(min(abs(x - 0), abs(x - w), abs(y - 0), abs(y - h)))