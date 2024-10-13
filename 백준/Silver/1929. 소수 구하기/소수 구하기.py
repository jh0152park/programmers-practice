import sys


def is_prime(num):
    if num < 2:
        return False

    n = 2
    while n ** 2 <= num:
        if not num % n:
            return False
        n += 1

    return True


m, n = map(int, sys.stdin.readline().strip().split())

for num in range(m, n + 1):
    if is_prime(num):
        sys.stdout.write(f"{num}\n")