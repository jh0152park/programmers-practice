import sys


a, b = map(int, sys.stdin.readline().strip().split())

print(max(a + b, a - b))
print(min(a + b, a - b))