import sys
from collections import deque



def bfs(board, x, y, width, height):
    q = deque()
    dis = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visied = [[False] * width for _ in range(height)]

    visied[y][x] = True
    q.append((x, y, 1))
    while q:
        x, y, move = q.popleft()
        if x == width - 1 and y == height - 1:
            return move

        for dx, dy in dis:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height and not visied[ny][nx] and board[ny][nx]:
                visied[ny][nx] = True
                q.append((nx, ny, move + 1))
    return -1


board = []
height, width = map(int, sys.stdin.readline().strip().split())
for _ in range(height):
    row = list(map(int, sys.stdin.readline().strip()))
    board.append(row)

print(bfs(board, 0, 0, width, height))