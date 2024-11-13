import sys


"""
3 4
WBBW
BBBB
WBBW

BWWW
WWWB
BWWB
"""

origin = []
reverse = []
h, w = map(int, sys.stdin.readline().strip().split())

for _ in range(h):
    origin.append(list(map(str, sys.stdin.readline().strip())))

sys.stdin.readline()

for _ in range(h):
    reverse.append(list(map(str, sys.stdin.readline().strip())))

wrong = 0
for i in range(h):
    for j in range(w):
        if reverse[i][j] == origin[i][j]:
            wrong += 1

print(wrong)