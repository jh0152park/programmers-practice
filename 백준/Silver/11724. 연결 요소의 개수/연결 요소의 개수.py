import sys

sys.setrecursionlimit(10**7)


def dfs(graph, visited, current_node):
    visited[current_node] = True
    for node in graph[current_node]:
        if not visited[node]:
            visited[node] = True
            dfs(graph, visited, node)


node, line = map(int, sys.stdin.readline().strip().split())
graph = [[] for _ in range(node + 1)]
visited = [False] * (node + 1)

for _ in range(line):
    n1, n2 = map(int, sys.stdin.readline().strip().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

component = 0
for n in range(1, node + 1):
    if not visited[n]:
        component += 1
        dfs(graph, visited, n)

print(component)