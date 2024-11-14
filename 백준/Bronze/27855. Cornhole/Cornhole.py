import sys
import math


p1 = 0
p2 = 0

h1, b1 = map(int, sys.stdin.readline().strip().split())
h2, b2 = map(int, sys.stdin.readline().strip().split())

p1 = h1 * 3 + b1
p2 = h2 * 3 + b2

if p1 == p2:
    print("NO SCORE")
else:
    if p1 > p2:
        print(f"1 {p1-p2}")
    else:
        print(f"2 {p2-p1}")