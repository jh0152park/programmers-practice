import sys
from collections import deque


def DSLR(f, t):
    q = deque()
    visited = [0] * 10000

    # number, compute
    q.append((f, ""))
    visited[f] = 1

    while q:
        number, compute = q.popleft()
        if number == t:
            return compute

        # D
        if not visited[(number * 2) % 10000]:
            q.append(((number * 2) % 10000, compute + "D"))
            visited[(number * 2) % 10000] = 1
        
        # S
        tmp = 9999 if number - 1 < 0 else number - 1
        if not visited[tmp]:
            q.append((tmp, compute + "S"))
            visited[tmp] = 1

        lnumber = (number % 1000) * 10 + (number // 1000)
        rnumber = (number % 10) * 1000 + (number // 10)
        # L
        if not visited[lnumber]:
            q.append((lnumber, compute + "L"))
            visited[lnumber] = 1
        #R
        if not visited[rnumber]:
            q.append((rnumber, compute + "R"))
            visited[rnumber] = 1

    return -1


n = int(sys.stdin.readline().strip())
for _ in range(n):
    f, t = map(int, sys.stdin.readline().strip().split())
    print(DSLR(f, t))