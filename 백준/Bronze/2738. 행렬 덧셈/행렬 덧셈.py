import sys

board = []
n, m = map(int, sys.stdin.readline().strip().split())

for _ in range(n):
    row = list(map(int, sys.stdin.readline().strip().split()))
    board.append(row)

for _ in range(n):
    row = list(map(int, sys.stdin.readline().strip().split()))
    for i in range(m):
        board[_][i] += row[i]

for i in range(n):
    print(*board[i])