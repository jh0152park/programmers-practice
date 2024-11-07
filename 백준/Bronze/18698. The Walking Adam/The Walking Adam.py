import sys


n = int(sys.stdin.readline().strip())
for _ in range(n):
    walk = 0
    history = sys.stdin.readline().strip()

    for w in history:
        if w == "D":
            break
        walk += 1

    print(walk)