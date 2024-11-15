import sys


t = int(sys.stdin.readline().strip())

for _ in range(t):
    n, a, d = map(int, sys.stdin.readline().strip().split())
    nums = [a]

    for i in range(n - 1):
        nums.append(nums[-1] + d)

    print(sum(nums))