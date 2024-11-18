import sys


diff = list(map(int, sys.stdin.readline().strip().split()))
n = int(sys.stdin.readline().strip())

max_score = -1
for _ in range(n):
    score = 0
    for _ in range(3):
        tech = list(map(int, sys.stdin.readline().strip().split()))
        score += (tech[0] * diff[0]) + (tech[1] * diff[1]) + (tech[2] * diff[2])

    max_score = max(max_score, score)

print(max_score)