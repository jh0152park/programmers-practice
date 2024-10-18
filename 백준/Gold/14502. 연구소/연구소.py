import sys
import copy
import pprint
from collections import deque


def count_safy_area(board, width, height):
    safe = 0

    for y in range(height):
        for x in range(width):
            if not board[y][x]:
                safe += 1

    return safe


def extend_virus(board, width, height):
    q = deque()
    dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = [[False] * width for _ in range(height)]

    for y in range(height):
        for x in range(width):
            if board[y][x] == 2:
                q.append((x, y))
                visited[y][x] = True

    while q:
        x, y = q.popleft()

        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height and not visited[ny][nx] and not board[ny][nx]:
                q.append((nx, ny))
                visited[ny][nx] = True
                board[ny][nx] = 2

    return board


def wall_install(board, visited, width, height, wall, safe):
    if wall == 3:
        virus_board = extend_virus(copy.deepcopy(board), width, height)
        safe_area = count_safy_area(virus_board, width, height)

        if not safe:
            safe.append(safe_area)
        else:
            safe[0] = max(safe_area, safe[0])
        
        return

    for h in range(height):
        for w in range(width):
            if not board[h][w] and not visited[h][w]:
                board[h][w] = 1
                visited[h][w] = True

                wall_install(board, visited, width, height, wall + 1, safe)

                board[h][w] = 0
                visited[h][w] = False
            
    
board = []
height, width = map(int, sys.stdin.readline().strip().split())
for _ in range(height):
    row = list(map(int, sys.stdin.readline().strip().split()))
    board.append(row)

safe = []
visited = [[False] * width for _ in range(height)]
wall_install(board, visited, width, height, 0, safe)
print(max(safe))