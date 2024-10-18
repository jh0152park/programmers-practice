import sys
from collections import deque


def catch(n, k):
    q = deque()
    visited = [0] * 100001

    q.append((n, 0))
    while q:
        position, sec = q.popleft()
        visited[position] = 1
        if position == k:
            return sec
        
        if position * 2 < 100001 and not visited[position * 2]:
            q.append((position * 2, sec + 1))
        if position - 1 >= 0 and not visited[position - 1]:
            q.append((position - 1, sec + 1))
        if position + 1 < 100001 and not visited[position + 1]:
            q.append((position + 1, sec + 1))
        

n, k = map(int, sys.stdin.readline().strip().split())
print(catch(n, k))