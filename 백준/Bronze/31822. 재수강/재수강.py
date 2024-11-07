import sys


course_code = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())

cnt = 0
for _ in range(n):
    code = sys.stdin.readline().strip()
    if code[:5] == course_code[:5]:
        cnt += 1

print(cnt)