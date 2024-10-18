import sys
import pprint
from collections import deque


def bfs(tomatos, M, N, H):
    # 상 하 좌 우 위 아래
    # x, y, z
    dis = [(0, -1, 0), (0, 1, 0), (-1, 0, 0), (1, 0, 0), (0, 0, -1), (0, 0, 1)]
    
    q = deque()
    
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if tomatos[h][n][m] == 1:
                    # z, y, x
                    q.append((h, n, m, 0))
    day = 0
    while q:
        h, n, m, day = q.popleft()

        for dx, dy, dz in dis:
            nx = m + dx
            ny = n + dy
            nz = h + dz
            if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M:
                if tomatos[nz][ny][nx] == 0:
                    q.append((nz, ny, nx, day + 1))
                    tomatos[nz][ny][nx] = 1

    for h in range(H):
        for n in range(N):
            for m in range(M):
                if tomatos[h][n][m] == 0:
                    return -1
    return day

tomatos = []
M, N, H = map(int, sys.stdin.readline().strip().split())

for h in range(H):
    layer = []
    for n in range(N):
        row = list(map(int, sys.stdin.readline().strip().split()))
        layer.append(row)
    tomatos.append(layer)

print(bfs(tomatos, M, N, H))