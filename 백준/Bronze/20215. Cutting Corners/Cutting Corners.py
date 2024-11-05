import sys
import math


w, h = map(int, sys.stdin.readline().strip().split())
diagonal = math.sqrt(w**2 + h**2)

print(w + h - diagonal)
