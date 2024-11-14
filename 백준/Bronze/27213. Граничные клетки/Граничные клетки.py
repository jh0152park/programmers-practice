import sys


m = int(sys.stdin.readline().strip())
n = int(sys.stdin.readline().strip())


if m >= 3 and n >= 3:
    print((m * n) - ((m - 2) * (n - 2)))
else:
    print(m * n)