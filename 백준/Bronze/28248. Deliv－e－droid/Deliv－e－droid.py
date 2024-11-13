import sys


p = int(sys.stdin.readline().strip())
c = int(sys.stdin.readline().strip())

point = (p * 50) - (c * 10)
if p > c:
    point += 500

print(point)