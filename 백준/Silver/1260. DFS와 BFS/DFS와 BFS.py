import sys
from collections import deque

sys.setrecursionlimit(10**7)


def dfs(graph, visited, s):
    sys.stdout.write(f"{s} ")

    visited[s] = True
    for node in sorted(graph[s]):
        if not visited[node]:
            dfs(graph, visited, node)


def bfs(graph, s):
    q = deque()
    visited = [False] * (len(graph) + 1)

    q.append(s)
    visited[s] = True

    while q:
        current_node = q.popleft()
        sys.stdout.write(f"{current_node} ")
        for node in sorted(graph[current_node]):
            if not visited[node]:
                visited[node] = True
                q.append(node)


n, m, v = map(int, sys.stdin.readline().strip().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (len(graph) + 1)

for _ in range(m):
    n1, n2 = map(int, sys.stdin.readline().strip().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

dfs(graph, visited, v)
print("")
bfs(graph, v)