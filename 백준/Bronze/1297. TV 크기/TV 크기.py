import sys


d, h, w = map(int, sys.stdin.readline().strip().split())

d = d ** 2
x = h ** 2 + w ** 2
an = (d / x) ** 0.5

z = int(h * an)
y = int(w * an)

print(z, y)