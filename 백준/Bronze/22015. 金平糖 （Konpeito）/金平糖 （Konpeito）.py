import sys


need = 0
ate = list(map(int, sys.stdin.readline().strip().split()))
ate.sort()

need += ate[2] - ate[1]
need += ate[2] - ate[0]

print(need)