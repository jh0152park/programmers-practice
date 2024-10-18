import sys


def dfs(jokbo, parents, visited, me, target, now, chonsoo, answer):
    if not parents.get(me) and not parents.get(target):
        answer.append(0)
        return 0
    
    # if parents[me] == parents[target]:
    #     answer.append(0)
    #     return 0

    if now == target:
        answer.append(chonsoo)
        return chonsoo
    
    visited[now] = True
    for someone in jokbo[now]:
        if not visited[someone] and not visited[target]:
            visited[someone] = True
            dfs(jokbo, parents, visited, me, target, someone, chonsoo + 1, answer)



n = int(sys.stdin.readline().strip())
p1, p2 = map(int, sys.stdin.readline().strip().split())
m = int(sys.stdin.readline().strip())

parents = {}
jokbo = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
for _ in range(m):
    n1, n2 = map(int, sys.stdin.readline().strip().split())
    jokbo[n1].append(n2)
    jokbo[n2].append(n1)
    parents[n2] = n1

chonsoo = []
dfs(jokbo, parents, visited, p1, p2, p1, 0, chonsoo)
if not chonsoo:
    print("-1")
else:
    print(chonsoo[0])