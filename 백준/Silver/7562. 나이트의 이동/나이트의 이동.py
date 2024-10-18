import sys
from collections import deque


def bfs(board, l, x, y, tx, ty):
    q = deque()
    visited = [[False] * l for _ in range(l)]
    dir = [(-2, -1), (-1, -2), (1, -2), (2, -1), (-2, 1), (-1, 2), (2, 1), (1, 2)]
    

    q.append((x, y, 0))
    visited[y][x] = True

    while q:
        x, y, move = q.popleft()
        if x == tx and y == ty:
            return move

        for dx, dy in dir:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < l and 0 <= ny < l and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((nx, ny, move + 1))
    

tc = int(sys.stdin.readline().strip())
for t in range(tc):
    l = int(sys.stdin.readline().strip())
    board = [[0] * l for _ in range(l)]
    cx, cy = map(int, sys.stdin.readline().strip().split())
    tx, ty = map(int, sys.stdin.readline().strip().split())

    print(bfs(board, l, cx, cy, tx, ty))