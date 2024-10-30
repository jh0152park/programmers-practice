import sys
import pprint
from collections import deque


def bfs(college, x, y, x_limit, y_limit):
    q = deque()
    dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = [[False] * x_limit for _ in range(y_limit)]

    meet = 0
    q.append((x, y))
    visited[y][x] = True
    
    while q:
        x, y = q.popleft()

        if college[y][x] == "P":
            meet += 1

        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if 0 <= nx < x_limit and 0 <= ny < y_limit and college[ny][nx] != "X" and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((nx, ny))


    return meet if meet else "TT"



y, x = map(int, sys.stdin.readline().strip().split())
college = [list(map(str, sys.stdin.readline().strip())) for _ in range(y)]

for i in range(y):
    for j in range(x):
        if college[i][j] == "I":
            meet = bfs(college, j, i, x, y)
            print(meet)
            exit(0)
