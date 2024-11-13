import sys


cost1, cost2 = map(int, sys.stdin.readline().strip().split())
n = int(sys.stdin.readline().strip())

for _ in range(n):
    cost = 0
    kw = int(sys.stdin.readline().strip())

    if kw > 1000:
        cost = ((kw - 1000) * cost2) + (cost1 * 1000)
    else:
        cost = kw * cost1

    print(kw, cost)