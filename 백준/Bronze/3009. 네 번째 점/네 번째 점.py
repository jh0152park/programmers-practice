import sys


x_pos = []
y_pos = []

for _ in range(3):
    x, y = map(int, sys.stdin.readline().strip().split())
    x_pos.append(x)
    y_pos.append(y)

x_pos.sort()
y_pos.sort()

x = x_pos[2] if x_pos[0] == x_pos[1] else x_pos[0]
y = y_pos[2] if y_pos[0] == y_pos[1] else y_pos[0]

print(x, y)