import sys
import math


n = int(sys.stdin.readline().strip())
dp = [float("inf")] * (n + 1)
dp[0] = 0

for i in range(1, n + 1):
    for k in range(1, int(math.sqrt(i)) + 1):
        dp[i] = min(dp[i], dp[i - k * k] + 1)

print(dp[n])