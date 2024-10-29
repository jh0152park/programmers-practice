import sys


my_mbti = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())

same = 0
for _ in range(n):
    mbti = sys.stdin.readline().strip()
    if mbti == my_mbti:
        same += 1

print(same)