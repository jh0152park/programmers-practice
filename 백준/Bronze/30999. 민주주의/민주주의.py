import sys


n, m = map(int, sys.stdin.readline().strip().split())

problem = 0
for _ in range(n):
    result = sys.stdin.readline().strip()
    if result.count("O") >= m // 2 + 1:
        problem += 1

print(problem)