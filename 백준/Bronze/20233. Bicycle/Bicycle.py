import sys


a = int(sys.stdin.readline().strip())
x = int(sys.stdin.readline().strip())
b = int(sys.stdin.readline().strip())
y = int(sys.stdin.readline().strip())
t = int(sys.stdin.readline().strip())

cost_a = a
cost_b = b

if t - 30 > 0:
    cost_a += (t - 30) * x * 21
if t - 45 > 0:
    cost_b += (t - 45) * y * 21

print(cost_a, cost_b)