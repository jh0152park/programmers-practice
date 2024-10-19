import sys
import pprint


def fill(paper, x, y):
    for i in range(y, y + 10):
        for j in range(x, x + 10):
            paper[i][j] = 1


paper = [[0] * 101 for _ in range(101)]

n = int(sys.stdin.readline().strip())
for _ in range(n):
    x, y = map(int, sys.stdin.readline().strip().split())
    fill(paper, x, y)

black = 0
for i in range(101):
    black += sum(paper[i])

print(black)