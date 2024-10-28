import sys
import bisect


n = int(sys.stdin.readline().strip())
x_pos = list(map(int, sys.stdin.readline().strip().split()))
dots = sorted(list(set(x_pos)))


for x in x_pos:
    sys.stdout.write(f"{bisect.bisect_left(dots, x)} ")