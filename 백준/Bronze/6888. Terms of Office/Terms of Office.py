import sys
import math


x = int(sys.stdin.readline().strip())
y = int(sys.stdin.readline().strip())

for year in range(x, y + 1, math.lcm(2, 4, 3, 5)):
    print(f"All positions change in year {year}")