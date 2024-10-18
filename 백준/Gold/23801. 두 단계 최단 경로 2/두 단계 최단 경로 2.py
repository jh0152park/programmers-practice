import sys
import heapq


def dijkstra(graph, n, start):
    q = []
    distances = [float("inf")] * (n + 1)
    
    distances[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        current_distance, current_node = heapq.heappop(q)

        if current_distance > distances[current_node]:
            continue

        for node, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[node]:
                distances[node] = distance
                heapq.heappush(q, (distance, node))

    return distances


n, m = map(int, sys.stdin.readline().strip().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w  = map(int, sys.stdin.readline().strip().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

x, z = map(int, sys.stdin.readline().strip().split())
p = int(sys.stdin.readline().strip())
mid_point = list(map(int, sys.stdin.readline().strip().split()))

distance_from_x = dijkstra(graph, n, x)
distance_from_z = dijkstra(graph, n, z)

min_distance = float("inf")

for mid in mid_point:
    start_x = distance_from_x[mid]
    start_z = distance_from_z[mid]

    if start_x == float("inf") or start_z == float("inf"):
        continue
    
    min_distance = min(min_distance, start_x + start_z)

if min_distance == float("inf"):
    min_distance = -1

print(min_distance)
