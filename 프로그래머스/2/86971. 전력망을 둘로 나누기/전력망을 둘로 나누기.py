def search(start, ignore, graph, count, visited):
    for top in graph[start]:
        if top != ignore and not visited[top]:
            count[0] += 1
            visited[start] = True
            search(top, ignore, graph, count, visited)
            visited[start] = False


def solution(n, wires):
    graph = {}
    visited = [False] * (n + 1)
    
    for wire in wires:
        v1, v2 = wire
        
        if v1 not in graph:
            graph[v1] = []
        if v2 not in graph:
            graph[v2] = [] 
            
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    delta = float("inf")
    for wire in wires:
        v1, v2 = wire
        count = [1]
        count2 = [1]
        search(v1, v2, graph, count, visited)
        search(v2, v1, graph, count2, visited)
        delta = min(delta, abs(count[0] - count2[0]))
    
    return delta