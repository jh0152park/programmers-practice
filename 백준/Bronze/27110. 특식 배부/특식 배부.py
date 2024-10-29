import sys


favorite = 0
chicken = int(sys.stdin.readline().strip())
orders = list(map(int, sys.stdin.readline().strip().split()))

for order in orders:
    if chicken > order:
        favorite += order
    else:
        favorite += min(order, chicken)

print(favorite)