import sys

board = []
for _ in range(9):
    row = list(map(int, sys.stdin.readline().strip().split()))
    board.append(row)

m, x, y = -1, 0, 0
for i in range(9):
    for j in range(9):
        if board[i][j] >= m:
            m = board[i][j]
            x = j + 1
            y = i + 1

print(m)
print(y, x)