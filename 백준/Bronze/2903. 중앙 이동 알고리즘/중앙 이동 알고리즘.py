import sys
import math


n = int(sys.stdin.readline().strip())
dot_per_side = 2 ** n + 1
total_dot = dot_per_side ** 2
print(total_dot)