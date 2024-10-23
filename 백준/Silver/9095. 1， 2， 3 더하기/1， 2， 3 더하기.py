import sys


def dfs(target_num, current_num):
    if current_num == target_num:
        return 1
    if current_num > target_num:
        return 0

    ret = 0
    ret += dfs(target_num, current_num + 1)
    ret += dfs(target_num, current_num + 2)
    ret += dfs(target_num, current_num + 3)

    return ret


tc = int(sys.stdin.readline().strip())
for _ in range(tc):
    n = int(sys.stdin.readline().strip())
    print(dfs(n, 0))