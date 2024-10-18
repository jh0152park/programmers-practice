import sys
import pprint
from collections import deque


def is_whole_good(tomatos, width, height):
    for y in range(height):
        for x in range(width):
            if tomatos[y][x] == 0:
                return False
    return True


def bfs(tomatos, width, height):
    q = deque()
    dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # from 0 day start at begin
    day = 0

    for y in range(height):
        for x in range(width):
            if tomatos[y][x] == 1:
                q.append((x, y, day))
    
    while q:
        x, y, day = q.popleft()

        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height and tomatos[ny][nx] == 0:
                tomatos[ny][nx] = 1
                q.append((nx, ny, day + 1))

    return day


tomatos = []
width, height = map(int, sys.stdin.readline().strip().split())
for _ in range(height):
    row = list(map(int, sys.stdin.readline().strip().split()))
    tomatos.append(row)

day = bfs(tomatos, width, height)
if is_whole_good(tomatos, width, height):
    print(day)
else:
    print("-1")