import sys


kings = []
n, m, k, a, b, c = map(int, sys.stdin.readline().strip().split())
jof = a * n
rob = b * m
sta = c * k

strongest = max(jof, rob, sta)
if jof == strongest:
    kings.append("Joffrey")
if rob == strongest:
    kings.append("Robb")
if sta == strongest:
    kings.append("Stannis")

kings.sort()
print(*kings)