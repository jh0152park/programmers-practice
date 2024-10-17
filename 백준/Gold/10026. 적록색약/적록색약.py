import sys

sys.setrecursionlimit(10**7)


def dfs(grid, visited, n, x, y, color):
    dis = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    grid[y][x] = "-"
    visited[y][x] = True
    for dx, dy in dis:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx] and grid[ny][nx] == color:
            visited[ny][nx] = True
            dfs(grid, visited, n, nx, ny, color)



grid = []
grid_for_blind = []
n = int(sys.stdin.readline().strip())

for _ in range(n):
    raw = sys.stdin.readline().strip()
    raw_for_blind = raw.replace("R", "G")

    grid.append(list(map(str, raw)))
    grid_for_blind.append(list(map(str, raw_for_blind)))

normal = 0
blind = 0

visited = [[False] * n for _ in range(n)]
for y in range(n):
    for x in range(n):
        if not visited[y][x]:
            normal += 1
            dfs(grid, visited, n, x, y, grid[y][x])

visited = [[False] * n for _ in range(n)]
for y in range(n):
    for x in range(n):
        if not visited[y][x]:
            blind += 1
            dfs(grid_for_blind, visited, n, x, y, grid_for_blind[y][x])

print(normal, blind)