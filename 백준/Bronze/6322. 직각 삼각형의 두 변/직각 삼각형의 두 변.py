import sys
import math


tc = 0
while True:
    tc += 1
    a, b, c = map(int, sys.stdin.readline().strip().split())
    if not a and not b and not c:
        break

    if c == -1:
        print(f"Triangle #{tc}")
        print("c = %.3f\n"%(math.sqrt(a ** 2 + b ** 2)))
    elif b == -1 and a < c:
        print(f"Triangle #{tc}")
        print("b = %.3f\n"%(math.sqrt(c ** 2 - a ** 2)))
    elif a == -1 and b < c:
        print(f"Triangle #{tc}")
        print("a = %.3f\n"%(math.sqrt(c ** 2 - b ** 2)))
    else:
        print(f"Triangle #{tc}")
        print("Impossible.\n")