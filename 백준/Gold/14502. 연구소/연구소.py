import sys
import copy
from collections import deque
from itertools import combinations


def count_safe_area(lab, width, height):
    safe = 0
    for y in range(height):
        for x in range(width):
            if not lab[y][x]:
                safe += 1

    return safe


def extend_virus(lab, width, height):
    q = deque()
    dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for y in range(height):
        for x in range(width):
            if lab[y][x] == 2:
                q.append((x, y))

    while q:
        x, y = q.popleft()
        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height and not lab[ny][nx]:
                lab[ny][nx] = 2
                q.append((nx, ny))

    return lab


def solution(lab, width, height):
    empty_area = []
    for y in range(height):
        for x in range(width):
            if not lab[y][x]:
                empty_area.append((x, y))

    max_safe = 0
    for wall in combinations(empty_area, 3):
        copy_lab = copy.deepcopy(lab)
        for x, y in wall:
            copy_lab[y][x] = 1

        copy_lab = extend_virus(copy_lab, width, height)
        safe = count_safe_area(copy_lab, width, height)
        max_safe = max(max_safe, safe)

    return max_safe


lab = []
h, w = map(int, sys.stdin.readline().strip().split())

for _ in range(h):
    row = list(map(int, sys.stdin.readline().strip().split()))
    lab.append(row)


print(solution(lab, w, h))