import sys


prices = []
n = int(sys.stdin.readline().strip())

for _ in range(n):
    prices.append(float(sys.stdin.readline().strip()))

prices.sort()
print("%.2f"%(prices[1]))