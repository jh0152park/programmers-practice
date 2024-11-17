import sys


alpha = {}
for c in range(ord("A"), ord("Z") + 1):
    alpha[chr(c)] = c

n = int(sys.stdin.readline())
prev = sys.stdin.readline().strip()
mine = sys.stdin.readline().strip()

move = 0
for i in range(n):
    up = alpha[prev[i]] - alpha[mine[i]]
    down = alpha[mine[i]] - alpha[prev[i]]

    if up < 0:
        up += 26
    if down < 0:
        down += 26

    move += min(up, down)

print(move)