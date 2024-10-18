import sys

# 촌수를 계산하는 DFS 함수
def dfs(jokbo, visited, now, target, chonsoo):
    if now == target:
        return chonsoo  # 목표 노드를 찾으면 촌수를 반환
    
    visited[now] = True  # 방문 표시

    for someone in jokbo[now]:
        if not visited[someone]:
            result = dfs(jokbo, visited, someone, target, chonsoo + 1)
            if result != -1:  # 목표를 찾았다면 반환
                return result
    
    return -1  # 목표를 찾지 못하면 -1을 반환

# 입력
n = int(sys.stdin.readline().strip())
p1, p2 = map(int, sys.stdin.readline().strip().split())
m = int(sys.stdin.readline().strip())

jokbo = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

# 관계 입력
for _ in range(m):
    n1, n2 = map(int, sys.stdin.readline().strip().split())
    jokbo[n1].append(n2)
    jokbo[n2].append(n1)

# DFS 호출
result = dfs(jokbo, visited, p1, p2, 0)
print(result)
