import sys

chicken = int(sys.stdin.readline().strip())
coke, beer = map(int, sys.stdin.readline().strip().split())

max_chicken = coke // 2 + beer
max_chicken = min(max_chicken, chicken)

print(max_chicken)