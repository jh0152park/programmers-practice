import sys


num1, num2 = map(int, sys.stdin.readline().strip().split())

a = 100 - num1
b = 100 - num2
c = 100 - (a + b)
d = a * b
q = d // 100
r = d % 100

print(a, b, c, d, q, r)
print(c + q, r)