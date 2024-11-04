import sys
import math

a1, p1 = map(int, sys.stdin.readline().strip().split())
r1, p2 = map(int, sys.stdin.readline().strip().split())

if a1 / p1 < math.pi * r1 * r1 / p2:
    print("Whole pizza")
else:
    print("Slice of pizza")