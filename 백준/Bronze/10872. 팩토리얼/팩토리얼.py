import sys


def fact(n):
    if n <= 1:
        return 1

    num = 1
    for i in range(1, n + 1):
        num *= i

    return num


n = int(sys.stdin.readline().strip())

print(fact(n))