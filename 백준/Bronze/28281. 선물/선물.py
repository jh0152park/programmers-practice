import sys


min_cost = float("inf")
n, x = map(int, sys.stdin.readline().strip().split())
prices = list(map(int, sys.stdin.readline().strip().split()))


for i in range(0, n - 1):
    cost = (prices[i] * x) + (prices[i + 1] * x)
    min_cost = min(min_cost, cost)

print(min_cost)