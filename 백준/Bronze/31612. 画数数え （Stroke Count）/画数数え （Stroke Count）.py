import sys


n = int(sys.stdin.readline().strip())
S = sys.stdin.readline().strip()

move = 0
for s in S:
    if s == "o":
        move += 1
    else:
        move += 2

print(move)