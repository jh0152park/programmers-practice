import sys


_ = int(sys.stdin.readline().strip())
nums = list(set(list(map(int, sys.stdin.readline().strip().split()))))
nums.sort()

for n in nums:
    print(n)