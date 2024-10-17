import sys
import pprint

sys.setrecursionlimit(10**7)


def is_range(x, y, width, height):
    return 0 <= x < width and 0 <= y < height


def dfs(farm, visited, x, y, width, height, baechu):
    dis = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    farm[y][x] = 0
    visited[y][x] = 1
    for dx, dy in dis:
        nx, ny = x + dx, y + dy
        if is_range(nx, ny, width, height) and not visited[ny][nx] and farm[ny][nx]:
            visited[ny][nx] = 1
            baechu = dfs(farm, visited, nx, ny, width, height, baechu + 1)

    return baechu


tc = int(sys.stdin.readline().strip())

for t in range(tc):
    width, height, baechu = map(int, sys.stdin.readline().strip().split())
    farm = [[0] * width for _ in range(height)]
    visited = [[0] * width for _ in range(height)]
    
    for _ in range(baechu):
        x, y = map(int, sys.stdin.readline().strip().split())
        farm[y][x] = 1

    warm = 0
    for y in range(height):
        for x in range(width):
            if farm[y][x] == 1:
                warm += 1
                dfs(farm, visited, x, y, width, height, 1)
                
    print(warm)
