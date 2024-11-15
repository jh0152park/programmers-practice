import sys


nums = list(map(int, sys.stdin.readline().strip().split()))
nums.sort()
print(nums[1])