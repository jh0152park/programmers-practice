import sys
import pprint

sys.setrecursionlimit(10**7)

def is_range(x, y, widht, height):
    return 0 <= x < widht and 0 <= y < height


def dfs(board, visited, x, y, width, height):
    dis = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, -1), (-1, 1), (1, 1)]

    board[y][x] = 0
    visited[y][x] = True
    for dx, dy in dis:
        nx, ny = x + dx, y + dy
        if is_range(nx, ny, width, height) and not visited[ny][nx] and board[ny][nx]:
            board[ny][nx] = 0
            visited[ny][nx] = True
            dfs(board, visited, nx, ny, width, height)


while True:
    width, height = map(int, sys.stdin.readline().strip().split())
    if not width and not height:
        break

    board = []
    visited = [[False] * width for _ in range(height)]
    for _ in range(height):
        row = list(map(int, sys.stdin.readline().strip().split()))
        board.append(row)

    island = 0
    for y in range(height):
        for x in range(width):
            if board[y][x]:
                island += 1
                dfs(board, visited, x, y, width, height)
    print(island)