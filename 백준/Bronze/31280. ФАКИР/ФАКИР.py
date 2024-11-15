import sys


mouse = list(map(int, sys.stdin.readline().strip().split()))
mouse.sort()
print(sum(mouse[1:]) + 1)