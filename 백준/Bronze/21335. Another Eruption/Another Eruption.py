import sys
import math


area = int(sys.stdin.readline().strip())
r = math.sqrt(area / math.pi)
print(2 * math.pi * r)