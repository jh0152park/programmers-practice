import sys


nums = []
for _ in range(10):
    nums.append(int(sys.stdin.readline().strip()))

print(sum(nums) // 2)