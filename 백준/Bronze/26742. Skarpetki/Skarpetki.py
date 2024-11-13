import sys


b = 0
w = 0

S = sys.stdin.readline().strip()
for s in S:
    if s == "B":
        b += 1
    else:
        w += 1

print((b // 2) + (w // 2))