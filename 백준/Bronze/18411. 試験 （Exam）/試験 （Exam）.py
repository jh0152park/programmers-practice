import sys


scores = list(map(int, sys.stdin.readline().strip().split()))
scores.sort()

print(sum(scores[1:]))