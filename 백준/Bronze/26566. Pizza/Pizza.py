import sys
import math


n = int(sys.stdin.readline().strip())
for _ in range(n):
    a1, p1 = map(int, sys.stdin.readline().strip().split())
    r1, p2 = map(int, sys.stdin.readline().strip().split())

    if a1 / p1 > (r1 ** 2 * math.pi) / p2:
        print("Slice of pizza")
    else:
        print("Whole pizza")