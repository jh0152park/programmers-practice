import sys
from collections import deque


def roll_dice(board):
    q = deque()
    visited = [False for _ in range(101)]

    # current position, move
    q.append((1, 0))
    visited[1] = True
    while q:
        # print(q)
        current_position, move = q.popleft()

        if current_position == 100:
            return move

        for dice in range(1, 7):
            if current_position + dice < 101 and not visited[current_position + dice]:
                if board[current_position + dice] == 0:
                    q.append((current_position + dice, move + 1))
                    visited[current_position + dice] = True
                else:
                    q.append((board[current_position + dice], move + 1))
                    visited[board[current_position + dice]] = True
    return -1



board = [0 for _ in range(101)]
ladder, snake = map(int, sys.stdin.readline().strip().split())
for _ in range(ladder + snake):
    f, t = map(int, sys.stdin.readline().strip().split())
    board[f] = t

print(roll_dice(board))