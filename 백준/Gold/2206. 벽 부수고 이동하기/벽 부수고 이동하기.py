import sys
import pprint
from collections import deque


def bfs(board, width, height):
    q = deque()
    dis = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = [[[False] * 2 for _ in range(width)] for _ in range(height)]

    q.append((0, 0, 1, 0))
    visited[0][0][0] = True

    while q:
        x, y, move, broken = q.popleft()

        if x == width - 1 and y == height - 1:
            return move

        for dx, dy in dis:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height:
                if not visited[ny][nx][broken] and board[ny][nx] == 0:
                    visited[ny][nx][broken] = True
                    q.append((nx, ny, move + 1, broken))
                if broken == 0 and board[ny][nx] == 1 and not visited[ny][nx][1]:
                    visited[ny][nx][1] = True
                    q.append((nx, ny, move + 1, 1))
    
    return -1


height, width = map(int, sys.stdin.readline().strip().split())
board = [list(map(int, sys.stdin.readline().strip())) for _ in range(height)]
print(bfs(board, width, height))