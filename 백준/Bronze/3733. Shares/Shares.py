import sys

while True:
    q = list(map(int, sys.stdin.readline().split()))
    if not q:
        break
    print(q[1] // (q[0] + 1))