import sys


max_score = float("-inf")
n = int(sys.stdin.readline().strip())
for _ in range(n):
    a, d, g = map(int, sys.stdin.readline().strip().split())
    score = a * (d + g)
    if a == (d + g):
        score *= 2

    max_score = max(max_score, score)

print(max_score)