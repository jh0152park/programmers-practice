def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    
    def dfs(node, computers):
        visited[node] = True
        
        for i in range(n):
            if computers[node][i] == 1 and not visited[i]:
                dfs(i, computers)
    
    
    for i in range(n):
        if not visited[i]:
            answer += 1
            dfs(i, computers)
    
    return answer