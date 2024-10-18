import sys
import pprint

sys.setrecursionlimit(10**4)

def dfs(board, x, y, width, height, move):
    dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    board[y][x] = 0
    for dx, dy in dir:
        nx, ny = x + dx, y + dy
        if 0 <= nx < width and 0 <= ny < height and board[ny][nx]:
            board[ny][nx] = 0
            move = dfs(board, nx, ny, width, height, move + 1)

    return move


height, width, k = map(int ,sys.stdin.readline().strip().split())
board = [[1] * width for _ in range(height)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().strip().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            board[i][j] = 0

isolate = 0
area = []

for y in range(height):
    for x in range(width):
        if board[y][x]:
            isolate += 1
            s = dfs(board, x, y, width, height, 1)
            area.append(s)
area.sort()
print(isolate)
print(*area)