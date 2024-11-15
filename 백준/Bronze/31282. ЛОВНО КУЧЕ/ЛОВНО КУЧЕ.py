import sys


n, m, k = map(int, sys.stdin.readline().strip().split())

n *= -1
jump = 0
rabbit = 0

while n < rabbit:
    jump += 1
    n += k
    rabbit += m

print(jump)