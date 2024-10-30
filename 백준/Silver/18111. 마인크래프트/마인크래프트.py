import sys


n, m, b = map(int, sys.stdin.readline().strip().split())
land = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

min_height = min(map(min, land))
max_height = max(map(max, land))


min_time = float("inf")
height = 0
for h in range(min_height, max_height + 1):
    add_block = 0
    remove_block = 0
    
    for i in range(n):
        for j in range(m):
            # remove
            if land[i][j] > h:
                remove_block += land[i][j] - h
            # add
            else:
                add_block += h - land[i][j]

    if remove_block + b >= add_block:
        time = 2 * remove_block + add_block
        
        if time < min_time:
            min_time = time
            height = h
        elif time == min_time:
            height = max(height, h)

print(min_time, height)