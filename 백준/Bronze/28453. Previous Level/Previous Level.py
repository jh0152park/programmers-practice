import sys


def get_sector(lv):
    if lv >= 300:
        return 1
    if 275 <= lv < 300:
        return 2
    if 250 <= lv < 275:
        return 3
    return 4

n = int(sys.stdin.readline().strip())
levels = list(map(int, sys.stdin.readline().strip().split()))

sector = []
for i in range(n):
    sector.append(get_sector(levels[i]))

print(*sector)