import sys
import pprint


BLOCKS = [
    # ㅁㅁㅁㅁ
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    # ㅁㅁ
    # ㅁㅁ
    [(0, 0), (1, 0), (0, 1), (1, 1)],
    # ㅁ
    # ㅁ
    # ㅁㅁ
    [(0, 0), (0, 1), (0, 2), (1, 2)],
    [(0, 0), (1, 0), (2, 0), (0, 1)],
    [(0, 0), (1, 0), (1, 1), (1, 2)],
    [(2, 0), (0, 1), (1, 1), (2, 1)],
    [(1, 0), (1, 1), (0, 2), (1, 2)],
    [(0, 0), (0, 1), (1, 1), (2, 1)],
    [(0, 0), (1, 0), (0, 1), (0, 2)],
    [(0, 0), (1, 0), (2, 0), (2, 1)],
    # ㅁ
    # ㅁㅁ
    #  ㅁ
    [(0, 0), (0, 1), (1, 1), (1, 2)],
    [(1, 0), (0, 1), (1, 1), (0, 2)],
    [(1, 0), (2, 0), (0, 1), (1, 1)],
    [(0, 0), (1, 0), (1, 1), (2, 1)],
    # ㅁ
    # ㅁㅁ
    # ㅁ
    [(0, 0), (0, 1), (1, 1), (0, 2)],
    [(1, 0), (0, 1), (1, 1), (1, 2)],
    [(0, 0), (1, 0), (2, 0), (1, 1)],
    [(1, 0), (0, 1), (1, 1), (2, 1)],
]



y, x = map(int, sys.stdin.readline().strip().split())
board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(y)]


# pprint.pprint(board)
max_sum = 0
for i in range(y):
    for j in range(x):
        for block in BLOCKS:
            block_sum = 0
            for dx, dy in block:
                nx = j + dx
                ny = i + dy 
                if 0 <= nx < x and 0 <= ny < y:
                    block_sum += board[ny][nx]
                else:
                    block_sum = 0
                    break
            max_sum = max(max_sum, block_sum)

print(max_sum)