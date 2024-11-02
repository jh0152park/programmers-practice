import sys


n, x, x_cost, y, y_cost = map(int, sys.stdin.readline().strip().split())

x_need = n // x
y_need = n // y

if n % x > 0:
    x_need += 1
if n % y > 0:
    y_need += 1

print(min(x_cost * x_need, y_cost * y_need))