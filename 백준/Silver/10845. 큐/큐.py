import sys
from collections import deque

q = deque()
n = int(input())

for _ in range(n):
    data = list(map(str, sys.stdin.readline().split()))
    if data[0] == "push":
        q.append(data[1])
    elif data[0] == "pop":
        if q:
            print(q.popleft())
        else:
            print("-1")
    elif data[0] == "size":
        print(len(q))
    elif data[0] == "empty":
        if q:
            print("0")
        else:
            print("1")
    elif data[0] == "front":
        if q:
            print(q[0])
        else:
            print("-1")
    else:
        if q:
            print(q[-1])
        else:
            print("-1")