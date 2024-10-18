import sys
from collections import deque


def bfs(graph, n):
    color = [-1] * (n + 1)


    for i in range(1, n + 1):
        if color[i] == -1:
            q = deque()
            
            q.append(i)
            color[i] = 0
            while q:
                node = q.popleft()
                
                for near in graph[node]:
                    if color[near] == -1:
                        color[near] = 1 - color[node]
                        q.append(near)
                    elif color[near] == color[node]:
                        return "NO"
    return "YES"


tc = int(sys.stdin.readline())
for t in range(tc):
    n, e = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(e):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    print(bfs(graph, n))