import heapq
import sys

input = sys.stdin.read
INF = float('inf')

def dijkstra(start, graph, N):
    distances = [INF] * (N + 1)
    distances[start] = 0
    pq = [(0, start)]  # (거리, 노드)
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances


# 입력 처리
data = input().splitlines()
N, M = map(int, data[0].split())

graph = [[] for _ in range(N + 1)]

for i in range(1, M + 1):
    u, v, w = map(int, data[i].split())
    graph[u].append((v, w))
    graph[v].append((u, w))  # 무방향 그래프

X, Z = map(int, data[M + 1].split())
P = int(data[M + 2])
middle_nodes = list(map(int, data[M + 3].split()))

# 1. X에서 모든 노드까지의 최단 경로 계산
dist_from_X = dijkstra(X, graph, N)

# 2. Z에서 모든 노드까지의 최단 경로 계산
dist_from_Z = dijkstra(Z, graph, N)

# 3. 중간 정점들 중 적어도 하나를 반드시 거쳐야 한다.
# 중간 정점 중 하나를 거치는 최단 경로를 찾기
min_total_distance = INF
for Y in middle_nodes:
    if dist_from_X[Y] == INF or dist_from_Z[Y] == INF:
        continue
    total_distance = dist_from_X[Y] + dist_from_Z[Y]
    min_total_distance = min(min_total_distance, total_distance)

# 결과 출력
if min_total_distance == INF:
    print(-1)
else:
    print(min_total_distance)

