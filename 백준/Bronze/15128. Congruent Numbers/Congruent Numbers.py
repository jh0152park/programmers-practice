import sys


p1, q1, p2, q2 = map(int, sys.stdin.readline().strip().split())
r = p1 * p2 / q1 / q2 / 2

if int(r) == r:
    print("1")
else:
    print("0")