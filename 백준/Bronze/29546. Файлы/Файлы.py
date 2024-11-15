import sys


photo = []

n = int(sys.stdin.readline().strip())
for _ in range(n):
    photo.append(sys.stdin.readline().strip())

m = int(sys.stdin.readline().strip())
for _ in range(m):
    l, r = map(int, sys.stdin.readline().strip().split())
    for i in range(l, r + 1):
        print(photo[i-1])