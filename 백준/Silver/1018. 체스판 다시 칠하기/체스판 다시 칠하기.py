import pprint


def copy_board(x, y, ref):
    board = [[None] * 8 for _ in range(8)]
    for i in range(y, y + 8):
        for j in range(x, x + 8):
            board[i-y][j-x] = ref[i][j]
    return board


def fill_board(ref, board):
    diff = 0
    for i in range(8):
        for j in range(8):
            if ref[i][j] != board[i][j]:
                diff += 1
    return diff


board1 = [[None] * 8 for _ in range(8)]
board2 = [[None] * 8 for _ in range(8)]


fill = False
for i in range(8):
    for j in range(8):
        board1[i][j] = "W" if fill else "B"
        board2[i][j] = "B" if fill else "W"
        fill = not fill
    fill = not fill

board = []
y, x = map(int, input().split())

for _ in range(y):
    row = []
    data = input().strip()
    
    for i in data:
        row.append(i)
    
    board.append(row)



fill = x * y
for i in range(0, y - 7):
    for j in range(0, x - 7):
        fill = min(fill, fill_board(board1, copy_board(j, i, board)))
        fill = min(fill, fill_board(board2, copy_board(j, i, board)))
        
print(fill)