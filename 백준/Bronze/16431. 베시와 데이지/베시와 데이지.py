import sys
from collections import deque


def bessie(jx, jy, bx, by):
    q = deque()
    dir = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, 1), (1, -1)]

    farm = [[0] * 1001 for _ in range(1001)]
    visited = [[False] * 1001 for _ in range(1001)]

    farm[jy][jx] = 1
    visited[by][bx] = True
    q.append((bx, by, 0))

    while q:
        x, y, move = q.popleft()

        if farm[y][x] == 1:
            return move

        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 1001 and 0 <= ny < 1001 and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((nx, ny, move + 1))

    return -1


def daisy(jx, jy, dx, dy):
    q = deque()
    dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    farm = [[0] * 1001 for _ in range(1001)]
    visited = [[False] * 1001 for _ in range(1001)]

    farm[jy][jx] = 1
    visited[dy][dx] = True
    q.append((dx, dy, 0))

    while q:
        x, y, move = q.popleft()

        if farm[y][x] == 1:
            return move

        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 1001 and 0 <= ny < 1001 and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((nx, ny, move + 1))

    return -1



by, bx = map(int, sys.stdin.readline().strip().split())
dy, dx = map(int, sys.stdin.readline().strip().split())
jy, jx = map(int, sys.stdin.readline().strip().split())

bessie_move = bessie(jx, jy, bx, by)
daisy_move = daisy(jx, jy, dx, dy)

print("daisy" if bessie_move > daisy_move else "bessie" if bessie_move < daisy_move else "tie")