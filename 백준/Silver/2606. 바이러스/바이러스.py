import sys
from collections import deque

sys.setrecursionlimit(10**7)


def dfs(graph, visited, connected, current_node):
    visited[current_node] = True

    for node in graph[current_node]:
        if not visited[node]:
            visited[node] = True
            connected.append(node)
            dfs(graph, visited, connected, node)


n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())

visited = [False] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    n1, n2 = map(int, sys.stdin.readline().strip().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

connected = []
dfs(graph, visited, connected, 1)
print(len(connected))