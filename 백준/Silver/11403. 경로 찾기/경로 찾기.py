import sys
import pprint
from collections import deque


def bfs(graph, node, n):
    q = deque()
    connect = []
    visited = [False] * (n + 1)
    
    for node in graph[node]:
        q.append(node)
        visited[node] = True
        connect.append(node)
    
    while q:
        current = q.popleft()

        for near in graph[current]:
            if not visited[near]:
                q.append(near)
                connect.append(near)
                visited[near] = True

    return sorted(connect)
    

n = int(sys.stdin.readline().strip())

graph = [[] for _ in range(n + 1)]
answer = []

for i in range(1, n + 1):
    connect = list(map(int, sys.stdin.readline().strip().split()))
    for j in range(n):
        if connect[j]:
            graph[i].append(j + 1)

for node in range(1, n + 1):
    nears = []
    connect = bfs(graph, node, n)
    for near in range(1, n + 1):
        if near in connect:
            nears.append(1)
        else:
            nears.append(0)
    answer.append(nears)


for _ in range(n):
    print(*answer[_])