import sys


def factorial(n):
    fact = [1] * (n + 1)

    for i in range(1, n + 1):
        fact[i] *= i * fact[i - 1]

    return fact[n]


n = int(sys.stdin.readline().strip())
fact = factorial(n)

print(fact // (86400 * 7))