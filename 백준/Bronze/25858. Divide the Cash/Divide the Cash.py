import sys


solved = []
n, money = map(int, sys.stdin.readline().strip().split())
for _ in range(n):
    solved.append(int(sys.stdin.readline().strip()))

for i in range(n):
    print(money // sum(solved) * solved[i])