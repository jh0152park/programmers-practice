import sys


floor = [0]
for _ in range(3):
    floor.append(int(sys.stdin.readline().strip()))

min_move = float("inf")
for i in range(1, 4):
    move = 0
    for j in range(1, 4):
        move += abs(i - j) * 2 * floor[j]
    min_move = min(move, min_move)

print(min_move)