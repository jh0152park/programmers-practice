import sys
from collections import deque


def bfs(board, answer, n, m, cur_x, cur_y):
    q = deque()
    dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = [[False] * m for _ in range(n)]

    visited[cur_y][cur_x] = True
    answer[cur_y][cur_x] = 0
    q.append((cur_x, cur_y, 0))

    while q:
        x, y, move = q.popleft()
        
        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx] and board[ny][nx]:
                visited[ny][nx] = True
                answer[ny][nx] = move + 1
                q.append((nx, ny, move + 1))

    for y in range(n):
        for x in range(m):
            if not visited[y][x]:
                if board[y][x] == 0:
                    answer[y][x] = 0
                else:
                    answer[y][x] = -1

    return -1



board = []
answer = []
n, m = map(int, sys.stdin.readline().strip().split())

for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().strip().split())))
    answer.append([0] * m)

run = False

for y in range(n):
    for x in range(m):
        if board[y][x] == 2:
            bfs(board, answer, n, m, x, y)
            run = True
            break
    if run:
        break


for y in range(n):
    print(*answer[y])