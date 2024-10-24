import sys

# 계단 수 입력
n = int(sys.stdin.readline().strip())
step = [0] * (n + 1)

# 각 계단의 점수 입력
for i in range(1, n + 1):
    step[i] = int(sys.stdin.readline().strip())

# dp 배열 초기화
dp = [0] * (n + 1)

# 초기 조건 설정
dp[1] = step[1]
if n > 1:
    dp[2] = step[1] + step[2]
if n > 2:
    dp[3] = max(step[1] + step[3], step[2] + step[3])

# dp 계산
for i in range(4, n + 1):
    dp[i] = max(dp[i - 2] + step[i], dp[i - 3] + step[i - 1] + step[i])

# 결과 출력
print(dp[n])
