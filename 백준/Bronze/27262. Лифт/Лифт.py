import sys


n, k, a, b = map(int, sys.stdin.readline().strip().split())
n -= 1
k -= 1
print((k * b) + (n * b), n * a)