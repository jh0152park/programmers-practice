import sys

a, b = map(int, sys.stdin.readline().strip().split())

a = a * ((100 - b) * 0.01)
if a >= 100:
    print("0")
else:
    print("1")