import sys


p, k = map(int, sys.stdin.readline().strip().split())
primes = list(range(0, k))

possible = []
for i in range(2, k):
    if primes[i] != 0:
        possible.append(i)
        for j in range(i*2, len(primes), i):
            primes[j] = 0

for prime in possible:
    if not p % prime:
        print(f"BAD {prime}")
        exit(0)

print("GOOD")