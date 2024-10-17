import sys

# 이동 범위 체크 함수
def is_range(x, y, width, height):
    return 0 <= x < width and 0 <= y < height

# DFS 탐색 함수
def dfs(board, x, y, width, height, alpha, cnt):
    dis = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 상하좌우 방향

    ret = cnt  # 현재까지 이동한 칸 수
    for dx, dy in dis:
        nx, ny = x + dx, y + dy
        if is_range(nx, ny, width, height):
            char_idx = ord(board[ny][nx]) - ord('A')  # 알파벳의 인덱스 계산
            if not (alpha & (1 << char_idx)):  # 비트마스킹: 해당 알파벳이 아직 사용되지 않았다면
                ret = max(ret, dfs(board, nx, ny, width, height, alpha | (1 << char_idx), cnt + 1))

    return ret

# 입력 받기
r, c = map(int, sys.stdin.readline().strip().split())
board = [list(sys.stdin.readline().strip()) for _ in range(r)]

# 시작점의 알파벳을 비트마스크에 기록 (A는 0번, Z는 25번 비트)
start_alpha = 1 << (ord(board[0][0]) - ord('A'))

# DFS 호출: 처음 좌표 (0, 0)에서 시작, 현재까지 1칸 이동
print(dfs(board, 0, 0, c, r, start_alpha, 1))
