import pprint
import sys
from collections import deque

sys.setrecursionlimit(10**7)


def dfs(board, x, y, n, visited, town):
    dis = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    visited[y][x] = True
    board[y][x] = 0
    for dx, dy in dis:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx] and board[ny][nx] != 0:
            visited[ny][nx] = True
            board[ny][nx] = 0
            town = dfs(board, nx, ny, n, visited, town + 1)
    return town


n = int(sys.stdin.readline().strip())
board = []

for _ in range(n):
    row = list(map(int, sys.stdin.readline().strip()))
    board.append(row)

village = []
for y in range(n):
    for x in range(n):
        if board[y][x] == 1:
            visited = [[False] * n for _ in range(n)]
            town = dfs(board, x, y, n, visited, 1)
            village.append(town)

village.sort()
print(len(village))
for n in village:
    print(n)
