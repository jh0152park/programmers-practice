import sys


a, b = map(int, sys.stdin.readline().strip().split())
k, x = map(int, sys.stdin.readline().strip().split())

friends = 0

for solve in range(a, b + 1):
    if abs(solve - k) <= x:
        friends += 1

if friends:
    print(friends)
else:
    print("IMPOSSIBLE")