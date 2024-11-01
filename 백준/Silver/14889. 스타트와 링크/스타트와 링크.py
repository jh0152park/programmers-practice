import sys
from itertools import combinations


n = int(sys.stdin.readline().strip())
members = [_ for _ in range(n)]
ability = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

delta = float("inf")
for start in combinations(members, n // 2):
    link = [member for member in members if member not in start]
    
    start_team = 0
    link_team = 0

    for i, j in combinations(start, 2):
        start_team += ability[i][j] + ability[j][i]
    for i, j in combinations(link, 2):
        link_team += ability[i][j] + ability[j][i]

    delta = min(delta, abs(start_team - link_team))
   
print(delta)