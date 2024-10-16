from collections import deque

def find(q, priority, target):
    work = 0
    while q:
        p, idx = q.popleft()
        if sum(priority[p+1:]) > 0:
            q.append((p, idx))
        else:
            work += 1
            priority[p] -= 1
            if idx == target:
                break
    return work


def solution(priorities, location):
    q = deque()
    priority = [0] * 10
    
    for i in range(len(priorities)):
        priority[priorities[i]] += 1
        q.append((priorities[i], i))
    
    return find(q, priority, location)