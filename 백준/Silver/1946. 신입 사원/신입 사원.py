import sys


tc = int(sys.stdin.readline().strip())
for _ in range(tc):
    n = int(sys.stdin.readline().strip())
    applies = []

    for _ in range(n):
        u, v = map(int, sys.stdin.readline().strip().split())
        applies.append((u, v))

    applies.sort()

    cnt = 1
    rank = applies[0][1]
    for i in range(1, n):
        if rank > applies[i][1]:
            cnt += 1
            rank = applies[i][1]
    print(cnt)