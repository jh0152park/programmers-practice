import sys


def fact(n):
    if n < 2:
        return 1

    f = 1
    for i in range(1, n + 1):
        f *= i

    return f % 10


n = int(sys.stdin.readline().strip())
for _ in range(n):
    num = int(sys.stdin.readline().strip())
    print(fact(num))