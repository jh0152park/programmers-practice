import math

n = int(input())
shirts = list(map(int, input().split()))
t, p = map(int, input().split())

T = 0
for shirt in shirts:
    T += math.ceil(shirt / t)

print(T)
print(n // p, n % p)