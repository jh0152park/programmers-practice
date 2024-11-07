import sys


a, b = map(int, sys.stdin.readline().strip().split())
if a >= b:
    print(b)
elif a < b and b != 0:
    print(a + 1)