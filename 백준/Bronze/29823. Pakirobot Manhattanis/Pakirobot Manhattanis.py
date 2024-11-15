import sys


n = int(sys.stdin.readline().strip())
walk = sys.stdin.readline().strip()


ns = 0
ew = 0
for dis in walk:
    if dis == "N":
        ns += 1
    elif dis == "S":
        ns -= 1
    elif dis == "E":
        ew += 1
    elif dis == "W":
        ew -= 1

print(abs(ns) + abs(ew))