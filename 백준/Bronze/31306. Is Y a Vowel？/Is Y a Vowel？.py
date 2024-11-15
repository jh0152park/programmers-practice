import sys


op1 = ["a", "e", "i", "o", "u"]
op2 = ["a", "e", "i", "o", "u", "y"]

cnt1 = 0
cnt2 = 0

S = sys.stdin.readline().strip()
for s in S:
    if s in op1:
        cnt1 += 1
    if s in op2:
        cnt2 += 1

print(cnt1, cnt2)