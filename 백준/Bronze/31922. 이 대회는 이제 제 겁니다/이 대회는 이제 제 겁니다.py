import sys


a, p, c = map(int, sys.stdin.readline().strip().split())
print(max(a + c, p))