import sys
import copy
import pprint

sys.setrecursionlimit(10**7)


def flood(board, height, n):
    flood_board = copy.deepcopy(board)

    for i in range(n):
        for j in range(n):
            if flood_board[i][j] <= height:
                flood_board[i][j] = 0

    return flood_board


def dfs(board, visited, x, y, n):
    dis = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    board[y][x] = 0
    visited[y][x] = True
    for dx, dy in dis:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx] and board[ny][nx] != 0:
            visited[ny][nx] = True
            board[ny][nx] = 0
            dfs(board, visited, nx, ny, n)


board = []
n = int(sys.stdin.readline().strip())

min_height = float("inf")
max_height = float("-inf")
for _ in range(n):
    row = list(map(int, sys.stdin.readline().strip().split()))
    min_height = min(min_height, min(row))
    max_height = max(max_height, max(row))
    board.append(row)

# ain't flood whole area is default
max_safe_area = 1

# no need to try flood max height.
# because whold field gonna be flood then no safe area.
for height in range(min_height, max_height):
    flood_board = flood(board, height, n)
    visited = [[False] * n for _ in range(n)]

    safe_area = 0
    for y in range(n):
        for x in range(n):
            if flood_board[y][x] and not visited[y][x]:
                safe_area += 1
                dfs(flood_board, visited, x, y, n)

    max_safe_area = max(max_safe_area, safe_area)

print(max_safe_area)