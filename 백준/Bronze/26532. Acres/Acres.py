import sys


w, h = map(int, sys.stdin.readline().strip().split())
corn = w * h // 4840 // 5

if w * h % 4840:
    corn += 1

print(corn)