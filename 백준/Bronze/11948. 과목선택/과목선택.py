import sys

scores = []
for _ in range(6):
    scores.append(int(sys.stdin.readline().strip()))

print(sum(scores[0:4]) - min(scores[0:4]) + max(scores[4:]))