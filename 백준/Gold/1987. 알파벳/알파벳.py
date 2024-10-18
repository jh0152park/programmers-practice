import sys


def dfs(board, alpha, x, y, width, height):
    dis = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    move = 1
    for dx, dy in dis:
        nx, ny = x + dx, y + dy
        if 0 <= nx < width and 0 <= ny < height:
            alpha_index = ord(board[ny][nx]) - ord("A")
            if not (alpha & (1 << alpha_index)):
                move = max(move, dfs(board, alpha | (1 << alpha_index), nx, ny, width, height) + 1)

    return move


y, x = map(int, sys.stdin.readline().strip().split())
board = [list(map(str, sys.stdin.readline().strip())) for _ in range(y)]

start_alpha = 1 << ord(board[0][0]) - ord("A")
print(dfs(board, start_alpha, 0, 0, x, y))