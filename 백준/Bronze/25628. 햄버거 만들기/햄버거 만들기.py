import sys


bread, meat = map(int, sys.stdin.readline().strip().split())
print(min(bread // 2, meat))