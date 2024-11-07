import sys


no = 0
t = int(sys.stdin.readline().strip())
score = list(map(int, sys.stdin.readline().strip().split()))

for _ in range(5 - len(score)):
    score.append(0)

if score[0] > score[2]:
    no = (score[0] - score[2]) * 508
else:
    no = (score[2] - score[0]) * 108

if score[1] > score[3]:
    no += (score[1] - score[3]) * 212
else:
    no += (score[3] - score[1]) * 305

if len(score) > 4:
    no += score[4] * 707

no *= 4763

print(no)