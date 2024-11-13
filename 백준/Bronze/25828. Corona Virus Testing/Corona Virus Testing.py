import sys


g, p, t = map(int, sys.stdin.readline().strip().split())

if g * p < g + (t * p):
    print("1")
elif g * p > g + (t * p):
    print("2")
else:
    print("0")