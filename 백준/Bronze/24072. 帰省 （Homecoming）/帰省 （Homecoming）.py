import sys


a, b, c = map(int, sys.stdin.readline().strip().split())

if a <= c < b:
    print("1")
else:
    print("0")