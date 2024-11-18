import sys


alpha = {}
for c in range(ord("A"), ord("Z") + 1):
    alpha[chr(c)] = c - ord("A")

S = sys.stdin.readline().strip()

rotate = 0
current = 0
for s in S:
    rotate1 = current - alpha[s]
    rotate2 = alpha[s] - current
    if rotate1 < 0:
        rotate1 += 26
    if rotate2 < 0:
        rotate2 += 26

    current = alpha[s]
    rotate += min(rotate1, rotate2)

print(rotate)