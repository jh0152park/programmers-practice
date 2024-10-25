import sys


n, m = map(int, sys.stdin.readline().strip().split())

psum = [0]
nums = list(map(int, sys.stdin.readline().strip().split()))
for i in range(n):
    psum.append(psum[-1] + nums[i])

for _ in range(m):
    i, j = map(int, sys.stdin.readline().strip().split())
    sys.stdout.write(f"{psum[j] - psum[i-1]}\n")
