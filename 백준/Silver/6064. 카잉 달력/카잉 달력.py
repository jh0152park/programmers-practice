import sys
import math


def compute_year(M, N, x, y):
    lcm = math.lcm(M, N)

    year = x
    while year <= lcm:
        if (year - 1) % N + 1 == y:
            return year
        year += M

    return -1


n = int(sys.stdin.readline().strip())
for _ in range(n):
    M, N, x, y = map(int, sys.stdin.readline().strip().split())
    print(compute_year(M, N, x, y))