import sys

s, a = map(int, sys.stdin.readline().strip().split())
print(min(s, a) // 2)