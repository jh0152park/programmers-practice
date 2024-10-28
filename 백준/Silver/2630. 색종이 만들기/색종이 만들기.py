# 1 2 4 8 16 32 64 128

import sys
import pprint

BLUE = 0
WHITE = 0


def divide(paper, n):
    global BLUE, WHITE

    s = 0
    for i in range(n):
        s += sum(paper[i])

    if s == 0:
        WHITE += 1
    elif s == n * n:
        BLUE += 1
    else:
        # left top
        div = []
        for i in range(n // 2):
            div.append(paper[i][:n // 2])
        divide(div, n // 2)
        
        # right top
        div = []
        for i in range(n // 2):
            div.append(paper[i][n // 2:])
        divide(div, n // 2)
        
        # left bottom
        div = []
        for i in range(n // 2, n):
            div.append(paper[i][:n // 2])
        divide(div, n // 2)
        
        # right bottom
        div = []
        for i in range(n // 2, n):
            div.append(paper[i][n // 2:])
        divide(div, n // 2)


n = int(sys.stdin.readline().strip())
paper = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

divide(paper, n)
print(WHITE)
print(BLUE)