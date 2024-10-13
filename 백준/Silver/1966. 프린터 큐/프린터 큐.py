import sys
from collections import deque


def do_print(q, ti, priority):
    work = 0
    while q:
        prio, idx = q.popleft()
        if sum(priority[prio+1:]) > 0:
            q.append((prio, idx))
        else:
            work += 1
            priority[prio] -= 1
            if idx == ti:
                break
    return work
    


tc = int(sys.stdin.readline().strip())

for i in range(tc):
    q = deque()
    priority = [0] * 11
    
    n, ti = map(int, sys.stdin.readline().strip().split())
    printer = list(map(int, sys.stdin.readline().strip().split()))

    for j in range(n):
        priority[printer[j]] += 1
        q.append((printer[j], j))

    print(do_print(q, ti, priority))
    