import sys

n = int(sys.stdin.readline())

positions = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    positions.append((x, y))

positions.sort(key=lambda x:(x[0], x[1]))
for x, y in positions:
    sys.stdout.write(f"{x} {y}\n")