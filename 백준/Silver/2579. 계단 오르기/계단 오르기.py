import sys

n = int(sys.stdin.readline().strip())

dp = [0] * (n + 1)
step = [0] * (n + 1)
for i in range(1, n + 1):
    step[i] = int(sys.stdin.readline().strip())

dp[1] = step[1]
if n > 1:
    dp[2] = step[1] + step[2]
if n > 2:
    dp[3] = max(step[3] + step[2], step[3] + step[1])

for i in range(4, n + 1):
    dp[i] = max(step[i] + dp[i - 2], step[i] + step[i - 1] + dp[i - 3])

print(dp[n])