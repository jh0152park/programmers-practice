import sys


vote = list(map(int, sys.stdin.readline().strip().split()))
candidate = 0
for i in range(1, 5):
    if abs(vote[0] - vote[i]) <= 1000:
        candidate += 1

print(candidate)