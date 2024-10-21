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


m = int(sys.stdin.readline().strip())
n = int(sys.stdin.readline().strip())

primes = []
for num in range(m, n + 1):
    if is_prime(num):
        primes.append(num)

if not primes:
    sys.stdout.write("-1")
else:
    sys.stdout.write(f"{sum(primes)}\n")
    sys.stdout.write(f"{primes[0]}")