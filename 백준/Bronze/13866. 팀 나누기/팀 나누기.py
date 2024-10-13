import sys
import math

levels = list(map(int, sys.stdin.readline().strip().split()))
levels.sort()

print(abs((levels[0] + levels[3]) - (levels[1] + levels[2])))