n = int(input())
visited = [];

def dfs():
    if len(visited) == n:
        print(*visited)
        return;

    for i in range(1, n + 1):
        if i not in visited:
            visited.append(i);
            dfs();
            visited.remove(i);
    
dfs()