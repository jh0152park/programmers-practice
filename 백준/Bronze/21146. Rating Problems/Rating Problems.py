import sys

n, k = map(int, sys.stdin.readline().strip().split())
score = 0
for _ in range(k):
    score += int(sys.stdin.readline().strip())

print((-3 * (n - k) + score) / n, (3 * (n - k) + score) / n)