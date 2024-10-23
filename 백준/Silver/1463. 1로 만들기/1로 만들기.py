import sys
from collections import deque


def solution(n):
    q = deque()
    q.append((n, 0))
    
    while q:
        x, compute = q.popleft()
    
        if x == 1:
            return compute
        
        if not x % 3:
            q.append((x // 3, compute + 1))
        if not x % 2:
            q.append((x // 2, compute + 1))
        q.append((x - 1, compute + 1))

n = int(sys.stdin.readline().strip())
print(solution(n))