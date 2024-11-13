import sys


a, b, c, d = map(int, sys.stdin.readline().strip().split())

if a * b > c * d:
    print("M")
elif a * b < c * d:
    print("P")
else:
    print("E")