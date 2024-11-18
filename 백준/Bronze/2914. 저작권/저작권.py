import sys
import math


song, avg = map(int, sys.stdin.readline().strip().split())

melody = 0
while True:
    if math.ceil(melody / song) == avg:
        break
    melody += 1

print(melody)