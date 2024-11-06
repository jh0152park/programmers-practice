import sys


h = int(sys.stdin.readline().strip()) * 100
w = int(sys.stdin.readline().strip()) * 100

print(min(h, w) // 2)