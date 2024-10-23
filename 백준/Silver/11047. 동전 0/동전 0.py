import sys

n, k = map(int,sys.stdin.readline().strip().split())
coins = [int(sys.stdin.readline().strip()) for _ in range(n)]

need = 0
coins.sort(reverse=True)
for coin in coins:
    if coin <= k and k:
        need += k // coin
        k = k % coin

print(need)