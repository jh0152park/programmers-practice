import sys

sys.setrecursionlimit(10**7)


def dfs(graph, visited, parents, current_node):
    visited[current_node] = True

    for node in graph[current_node]:
        if not visited[node]:
            visited[node] = True
            parents[node] = current_node
            dfs(graph, visited, parents, node)


parents = {}

n = int(sys.stdin.readline().strip())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(n - 1):
    n1, n2 = map(int, sys.stdin.readline().strip().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

parents[1] = "0"
dfs(graph, visited, parents, 1)

for node in range(2, n + 1):
    sys.stdout.write(f"{parents[node]}\n")