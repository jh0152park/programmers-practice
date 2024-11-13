import sys


n = int(sys.stdin.readline().strip())
for _ in range(n):
    a, b = map(float, sys.stdin.readline().strip().split())
    h = 2 * a / b
    print("The height of the triangle is %.2f units"%(h))